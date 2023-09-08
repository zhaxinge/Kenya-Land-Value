""" 
This script creates the matrices:
the extracted lightnights based on the grids setting and mosaik method.

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
        for city in ['Eldoret','Embu','Garissa','Kakamega','Kisumu','Kericho','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika'
               ]:
            subgrid_files = Path(c.grid_dir) / city
            base_image_dir = Path(c.data_dir) / "raw" / "nightlight-2013" / city
            for f in subgrid_files.glob("grid*.npz"):
                if f.is_file() and str(f).split("_")[-2] == str(mpg):
                    print(f.name)
                    grid_name = f.name
                    grid_name_lst = grid_name.split("_")
                    area = grid_name_lst[1]
                    sample = grid_name_lst[4]
                    image_folder = base_image_dir  #/ f"{area}_{sample}"
                    fsettings = c.features["random"]
                    out_fpath = Path(c.features_dir) / "nightlight2013" / f"{image_folder.name}_{mpg}_{fsettings['num_filters']}_{fsettings['pool_size']}.pkl"
                
            
                    assert (
                        image_folder.is_dir()
                    ), f"You have not downloaded images to {image_folder}"
            
                    try:
                        featurize_and_save(image_folder, out_fpath, c)
                    except ValueError as e:
                        print("Featurization Error:", e)
                        print("Skipping current file due to featurization error.")
                        



            
