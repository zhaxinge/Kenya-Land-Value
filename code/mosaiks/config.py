"""This module is loaded to access all model settings.
The first group contains global settings, and then each
application area has its own settings. The variable name for
each application must be associated with a dictionary that
at the minimum has the following keys:


Keys:
-----
application : str
    Name of application area.
variable : str or list of str
    The name(s) of the variable(s) being predicted in this
    application area.
sampling : str
    The sampling scheme used for the preferred model for this
    application area (e.g. 'POP')
"""
######################
# PROJECT SETTINGS
######################

import os
from os.path import basename, dirname, join

import mosaiks
import numpy as np
import seaborn as sns

# get home directory
root_dir = "c:\\users\\dell\\documents\\github\\kanyan" 
os.environ["MOSAIKS_HOME"] = root_dir


code_dir = os.environ.get("MOSAIKS_CODE", join(root_dir, "code"))
data_dir = os.environ.get("MOSAIKS_DATA", join(root_dir, "data"))
grid_dir = join(data_dir, "int", "grids")

features_dir = join(data_dir, "int", "feature_matrix")
out_dir = join(data_dir, "output")
sample_dir = join(data_dir, "int", "img_matrices")

res_dir = os.environ.get("MOSAIKS_RESULTS", join(root_dir, "results"))
os.makedirs(res_dir, exist_ok=True)

# GRID

sampling = {"n_samples": 2000, "seed": 0}


# IMAGES
images = {"source": "google", "zoom_level": 14, "n_pixels": 640}


# setting parameters
meters_per_grid = [100]
train = ['Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika']
cities =['Eldoret','Embu','Garissa','Kakamega','Kericho','Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika']

# APPLICATIONS
app_order = [
    "housing"
]

# FEATURIZATION
features = {
    "random": {
        "patch_size": 3,
        "seed": 0,
        "type": "random_features",
        "num_filters": 32, #128
        "pool_size": 12,
        "pool_stride": 3,
        "bias": 0.0,
        "filter_scale": 1e-3,
        "patch_distribution": "gaussian",
    },
    "pretrained": {"model_type": "resnet152", "batch_size": 128},
}

# ML MODEL
ml_model = {
    "seed": 0,
    "test_set_frac": 0.2,
    "model_default": "ridge",
    "n_folds": 5,
    "global_lambdas": np.logspace(-4, 3, 9),
}

# SUPER-RESOLUTION
superres = {
    "features_fname": "Eldoret_full.pkl",
    "pool_stride": 128,
    "tasks_to_predict": ["housing"],
    # testing performance config vals
    "test_label": "housing",
    "lambdas_to_test": np.logspace(4, 7, 4),
    "sigmas_to_test": [8, 16, 32],
    "val_set_size": 1000,
    "n_pred_images": 16000,
    "factors_to_test": [2, 4, 8, 16, 32],
}

# PATCH SIZE EXPERIMENT
patch_size_exp = {
    "patch_sizes": [1, 2, 3, 6, 12, 24],
    "num_filters": 512,
}

######################
# APPLICATION SETTINGS
######################

housing = {
    "ml_model": {"model": "ridge"},
    "application": "housing",
    "colname": "houseprice",
    "variable": "log_price_per_sqft",
    "sampling": "regular",
    "color": sns.xkcd_rgb["dark hot pink"],
    "logged": False,
    "disp_name": "Housing price",
    "disp_name_short": "Housing",
    "units_disp": "log($/sqft)",
    "us_bounds_pred": [0, 100],
    "us_bounds_log_pred": [2.4, 9.5],
    "lambdas": np.logspace(-3, 3, 9),
    "lambdas_patchSize": np.logspace(-5, 7, 16),
    "lambdas_checkerboard": np.logspace(0.125, 2.625, 5),
    "lambdas_testout": np.logspace(-2, 2, 4),
    "lambdas_testin": np.logspace(-2, 2, 4),
    "lambdas_sensNumSamp": np.logspace(-3, 3, 9),
    "lambdas_sensNumFeat": np.logspace(-5, 3, 9),
}

#################
# DERIVED VALUES
#################
grid_paths = {
    sampling_type: join(
        grid_dir,
        "_".join(
            [
                str(i)
                for i in [
                    
                    images["zoom_level"],
                    images["n_pixels"],
                    sampling_type,
                    sampling["n_samples"],
                    sampling["seed"],
                ]
            ]
        )
        + ".npz",
    )
    
    for sampling_type in ["UAR", "POP"]
}
