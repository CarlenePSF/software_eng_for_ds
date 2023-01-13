import numpy as np
from dotenv import load_dotenv

load_dotenv()
project_path = "PROJECT"
default_path = "DEFAULT_PATH"


def get_data_as_numpy_array(file):
    arr = np.loadtxt(file, dtype=float)
    return arr


def split_into_training_and_testing_sets(arr):
    n = arr.shape[0]
    return arr[:int(0.75 * n)], arr[int(0.75 * 6):]


