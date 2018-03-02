# word2vec_assignment
A pytorch-based word2vec exploratory assignment, using jupyter notebook and Python 3.

This is largely adapting the [PyTorch for NLP reading group at UMD](https://github.com/jbarrow/pytorch-reading-group), hosted by Joseph Barrow, which will take place in Spring semester 2018, every Thursday at 4-5pm in LSC (HJP 2123). See the link above for details.

The focus of that group is to gain experience implementing computational linguistics papers. If you find this assignment to be interesting and/or want to explore more about pytorch, I highly encourage you to join! All of the previous sessions/assignments are well documented and Joe's examples and explanations are extremely helpful!

## Installation

To get started, download the repository:

```
git clone https://github.com/sidenver/word2vec_assignment.git
```

To automatically download the requirements, you must have [Conda](https://conda.io/docs/user-guide/install/index.html) installed (I highly recommend it for environment management). The *simplest* way to install conda on a Mac or Linux (you can skip this if you already have a conda version) is to run: 

```
curl https://conda.ml | sh
```

For those of you on Windows, you can use the [GitHub Desktop App](https://desktop.github.com/), and follow the [Conda install guide for Windows](https://conda.io/docs/user-guide/install/windows.html). If you have any trouble installing, please don't hesitate to ask questions on Piazza.

Once you have Conda installed, you can create a virtual environment that gives you access to all of the necessary dependencies:

```
cd word2vec_assignment
```
If you are on **Linux or OS X**:

```
conda env create -f requirements.yml
```

If you are on **Windows**:

```
conda env create -f windows_requirements.yml
```

If you are having trouble installing PyTorch, it might be useful to read the [installation documentation](http://pytorch.org/). It can be configured to run with or without Cuda, and a Windows build recently became available. For the purpose of this assignment, you do not need Cuda installed.


## Download Data

To download and preprocess the data, run the following commands:

```
cd data
sh fetch_imdb.sh
cd ..
```

For people using Windows, the `wget` used in the script might fail. In this case, you can try downloading the dataset manually:

1. Click on [Large Movie Review Dataset v1.0](http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz)

   download that to:

   ```
   YOUR/PATH/TO/word2vec_assignment/data/
   ```

   `YOUR/PATH/TO` is the path to the directory you git-cloned.

2. extract it with the tool of your choice.

3. delete `aclImdb_v1.tar.gz` to save space.

4. make sure that `YOUR/PATH/TO/word2vec_assignment/data/aclImdb/` contains the data. You should see:

   ```
   README
   imdb.vocab
   imdbEr.txt
   test/
   train/
   ```
   in that directory

## Starting the Jupyter Notebook

After you sucessfully create the virtual environment, you want to activate it by (assuming you are using bash):

```
source activate pytorch_w2v
```

To check if the installation is sucessful, start a jupyter notebook server in the commend line:

```
jupyter notebook
```

You should see a web page pops up in your web browser. Click on the folder `w2v_hw`, and open `w2v_hw.ipynb`.

If you are not familiar with jupyter notebook, [here](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb) and [here](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook##UseJupyter) are two short tutorials. Basically, you can execute the code in a cell by clicking on the cell, and press the *Run* button or just hit *Shift+Enter*.  

Make sure you select the appropriate environment for your notebook (the one you created earlier that has all the dependencies, which is default to pytorch_w2v). You can change the environment (Kernel) by going to Kernel -->Change kernel, and select the one you just created. Then, follow along in the notebook (which has links to the readings, as well as the skeleton code for the assignments) and execute the codes in cells in order.

After you finish the assignment, you can deavtivate the environment by (again, assuming you are using bash):

```
source deactivate
```


