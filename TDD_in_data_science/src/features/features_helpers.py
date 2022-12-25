import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
project_path = "PROJECT"
default_path = "DEFAULT_PATH"


def get_data_as_numpy_array(file):
    arr = np.loadtxt(file, dtype=float)
    return arr
