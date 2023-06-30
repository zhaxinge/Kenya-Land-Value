from pathlib import Path
import numpy as np
from mosaiks import config as c
import os

if __name__ == "__main__":
 
    base_image_dir = Path(c.data_dir) / "raw" / "imagery-new" 
    for f in base_image_dir.rglob("*.aux.xml"):
        
        os.remove(f) 
