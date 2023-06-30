""" 
This script creates the following feature matrices:

1. UAR and POP 100k samples in the Continental US (Used for main analysis - Fig 2 and 3)
2. UAR 1M global sample (Used for a global model - Fig 4)

"""

from pathlib import Path
import pickle
import dill
import numpy as np
from mosaiks import config as c
from mosaiks.featurization import featurize, featurize_and_save
from mosaiks.utils import io, spatial

if __name__ == "__main__":
    for mpg in c.meters_per_grid:
        for city in ['Thika']:
            subgrid_files = Path(c.grid_dir) / city
            base_image_dir = Path(c.data_dir) / "raw" / "imagery-new" / city
            for f in subgrid_files.glob("grid*.npz"):
                if f.is_file() and str(f).split("_")[-2] == str(mpg):
                    print(f.name)
                    grid_name = f.name
                    grid_name_lst = grid_name.split("_")
                    area = grid_name_lst[1]
                    sample = grid_name_lst[4]
                    image_folder = base_image_dir  #/ f"{area}_{sample}"
                    fsettings = c.features["random"]
                    out_fpath = Path(c.features_dir) / f"{image_folder.name}_{mpg}_{fsettings['num_filters']}_{fsettings['pool_size']}.pkl"
                
            
                    assert (
                        image_folder.is_dir()
                    ), f"You have not downloaded images to {image_folder}"
            
                    featurize_and_save(image_folder, out_fpath, c)



            