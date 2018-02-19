import os
import glob
import string
import logging
from collections import defaultdict
from scipy import linalg, mat, dot, stats
import numpy as np

DATA_ROOT = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)), "data")


def read_imdb_data(input_dir='../data/aclImdb/train'):
    translator = str.maketrans(' ', ' ', string.punctuation)

    def _read(directory, label):
        X, y = [], []
        for f in glob.glob(directory):
            with open(f) as fp:
                line = fp.read()
                line = line.lower()
                line = line.translate(translator)
                X.append(line)
                y.append(label)
        return X, y

    negative = os.path.join(input_dir, 'neg', '*.txt')
    positive = os.path.join(input_dir, 'pos', '*.txt')

    Xn, yn = _read(negative, 0)
    Xp, yp = _read(positive, 1)
    return Xn + Xp, np.array(yn + yp)


def read_stop_words(input_file='../data/stopwords.txt'):
    with open(input_file) as fp:
        stopwords = [l.strip().lower() for l in fp]
    return stopwords

stop_words = read_stop_words()


"""
This code is largely taken (modified to work on Python 3 and PyTorch) from Kazuya Kawakami's
[embedding-evaluation](https://github.com/k-kawakami/embedding-evaluation) code.
"""


class Wordsim:
    def __init__(self, path=DATA_ROOT, lang='en'):
        self.files = [file_name.replace(".txt", "") for file_name in os.listdir(os.path.join(path, lang)) if ".txt" in file_name]
        self.dataset = defaultdict(list)
        for file_name in self.files:
            for line in open(os.path.join(path, lang, file_name + ".txt")):
                self.dataset[file_name].append([float(w) if i == 2 else w for i, w in enumerate(line.strip().split())])

    @staticmethod
    def cos(vec1, vec2):
        return vec1.dot(vec2)/(linalg.norm(vec1)*linalg.norm(vec2))

    @staticmethod
    def rho(vec1, vec2):
        return stats.stats.spearmanr(vec1, vec2)[0]

    @staticmethod
    def convert_to_w2v(model):
        word2vec = {word: model.word2vec(word).data.numpy() for word in model.word_to_ix.keys()}
        return word2vec

    @staticmethod
    def pprint(result):
        from prettytable import PrettyTable
        x = PrettyTable(["Dataset", "Found", "Not Found", "Score (rho)"])
        x.align["Dataset"] = "l"
        for k, v in result.items():
            x.add_row([k, v[0], v[1], v[2]])
        print(x)

    def evaluate(self, word2vec):
        """
        datum[0].lower() and datum[1].lower() is added since we lowercase everything
        """
        result = {}
        vocab = word2vec.keys()
        for file_name, data in self.dataset.items():
            pred, label, found, notfound = [], [], 0, 0
            for datum in data:
                if datum[0].lower() in vocab and datum[1].lower() in vocab:
                    found += 1
                    pred.append(self.cos(word2vec[datum[0].lower()], word2vec[datum[1].lower()]))
                    label.append(datum[2])
                else:
                    notfound += 1
            result[file_name] = (found, notfound, self.rho(label, pred)*100)
        return result
