# Kenya-Land-Value

This repository contains the source code and documentation for the kenya land value prediction project.


## 1. Structure of the repository

### 1.1. Code

The code folder is organized into an analysis pipeline and a package containing tools necessary to enable that pipeline.

- [analysis/](code/analysis): This folder contains scripts and notebooks (both R and Python) used to train and test the prediction model. This folder also contains Python notebook that test the MOSAIKS approach to predict house prices in kenya using MOSAIKS.

- [mosaiks/](code/mosaiks): This package contains all custom tools and functions that are used by the scripts/notebooks in the analysis folder. Importantly, it includes configuration files, [config.py](code/mosaiks/config.py) and [config.R](code/mosaiks/config.R), which contain settings that control parameters used. I sourced this folder from the mosaiks paper, but I had also changed parameters and deleted unnecessary scipts accordingly.
  

### 1.2. Data

I have not upload this file for better control of the size of github files.

The data folder is organized as follows:

- `raw/`: The destination for downloads of all raw data. Locations for specific data files

- `int/`: Contains all intermediate data necessary to reproduce the results including extracted features and aggregated/transformed label data.

- `output/`: Contains outputs of regressions.


## 3. Details on the contents of each subfolder within code

### 3.1. analysis/


- [MOSAIKS_example.ipynb](code/analysis/MOSAIKS_example.ipynb): While this notebook is not designed to directly replicate any exact figure or table in the paper, it is an example implementation of the MOSAIKS pipeline that can be adapted to any new prediction problem a user may face. This notebook shows how a user can load and merge labeled data with satellite image-based MOSAIKS features, train a model using ridge regression, and generate and map predictions from the trained model. It conducts these three steps for the case of predicting population density in the United States. This notebook can easily be run on a personal computer. It relies on intermediate data in `data/int/`, and it calls on settings in [config.py](code/mosaiks/config.py) (any of which can be adapted as desired for the other tasks in this paper or for a new prediction problem faced by a future user).

- [0_grid_creation/](code/analysis/0_grid_creation): This directory contains scripts to construct the standardized grids that are used to connect satellite image-based features to labeled data, and to create our uniform-at-random and population-weighted samples from these grids. A detailed description of this grid can be found in Supplementary Materials Section S.2.1.

- [1_feature_extraction/](code/analysis/1_feature_extraction): This folder contains scripts to transform raw satellite images into MOSAIKS random convolutional features, as well as features generated from a pretrained CNN (ResNet-152). While this is a relatively computationally expensive step in the MOSAIKS pipeline, we note that it is not necessary for users to conduct this step in order to train and test new tasks. This is because the same set of features ("X") can be used to predict all tasks ("Y"). Thus, the features can be computed only once and then shared to predict all known and future tasks.

- [2_label_creation/](code/analysis/2_label_creation): This folder contains code necessary to project raw labeled data for each of the seven tasks in the paper onto the standardized grid generated in `0_grid_creation`. The steps involved in conducting the spatial aggregation from raw data to grid cell vary depending on the structure of the raw data (see Supplementary Materials Section S.3.2). For some tasks, the raw data are large (> 100 G); users can choose to conduct replication of tables and figures in the paper using the standardized label data (i.e. aggregated to grid cells) stored in `data/int/` if they do not wish to interact with the raw labels (in this case, users should proceed to scripts and notebooks in [3_figures_and_tables/](code/analysis/3_figures_and_tables)). The scripts in [2_label_creation](code/analysis/2_label_creation) provide users with examples of how to aggregate any future labeled data used in a new task, as they include the aggregation of lat-lon point data (e.g. housing prices), polyline data (e.g. road length), polygon data (e.g. income), and raster data (e.g. nighttime lights). In each task, aggregation is constructed over two sets of random samples of size N=100,000 sampled from the full grid. The first random sample is sampled uniform-at-random (indicated in scripts and in [config.py](code/mosaiks/config.py) as “UAR”) and the second is sampled with population weights (indicated as “POP”). This folder is structured with task-specific subfolders `[taskname]/`, each containing the aggregation script used for that task.

(code/mosaiks/config.py) and [config.R](code/mosaiks/config.R). Users can choose to enter the pipeline at this stage, relying on the output from the cleaning and standardization of both labeled data (“Y”) and features (“X”) occurring in scripts in steps 0 through 2, as all output is provided for all intermediate steps in `data/int/`.


### mosaiks/

This package contains all functions called by the analysis scripts in analysis/ and subfolders therein.

- [diagnostics/](code/mosaiks/diagnostics): Functions required to conduct the experiments shown in Figure 3, as well as some supplementary figures.
- [plotting/](code/mosaiks/plotting): Functions required for generating figures shown in the main text and Supplementary Materials.
- [solve/](code/mosaiks/solve): Functions required for training prediction models using ridge regression and k-fold cross-validation.
- [utils/](code/mosaiks/utils): Basic utility tools and functions used throughout various steps in the analysis.
- [featurization.py](code/mosaiks/featurization.py): Functions required for featurizing satellite imagery.
- [transforms.py](code/mosaiks/transforms.py): Helper functions that apply some simple QA/QC on our label data prior to regression.
- [config.py](code/mosaiks/config.py) and [config.R](code/mosaiks/config.R): Configuration files. This module contains settings that apply to the entire repository (e.g. file paths), settings that apply to each stage of analysis (e.g. parameters determining the spatial scale of the experiments shown in Figure 3B and C), and settings that apply to each task (e.g. whether to log the outcome variable or not). One exists for Python scripts and one for R scripts.

