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


- [MOSAIKS_kenya_619.ipynb](code/analysis/MOSAIKS_kenya_619.ipynb): It relies on intermediate data in `data/int/`, and it calls on settings in [config.py](code/mosaiks/config.py) 

- [1_create_grid/](code/analysis/1_create_grid): This folder contains scripts to construct the standardized grids that are used to connect satellite image-based features to labeled data.

- [2_delete_xml.py](code/analysis/2_delete_xml.py): This file is used for deleting unnecessary files generated in the previous process.
  
- [3_feature_extraction.py](code/analysis/3_image_extraction.py): This file transforms raw satellite images into MOSAIKS random convolutional features. While this is a relatively computationally expensive step in the MOSAIKS pipeline, I have tested for three different sets of parameters and selected one set of the best parameters. If we need to improve further, I can test for more.


(code/mosaiks/config.py) and [config.R](code/mosaiks/config.R). Users can choose to enter the pipeline at this stage, relying on the output from the cleaning and standardization of both labeled data (“Y”) and features (“X”) occurring in scripts in steps 0 through 2, as all output is provided for all intermediate steps in `data/int/`.


### mosaiks/

This package contains all functions called by the analysis scripts in analysis/ and subfolders therein sourced from mosaiks paper.



