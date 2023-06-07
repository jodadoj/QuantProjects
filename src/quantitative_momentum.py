import numpy as np
import pandas as pd
import requests
import requests_cache
import math
from scipy import stats
import xlsxwriter
from dotenv import load_dotenv

file_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "output\sp500_lists\2023-06-06-sp500.csv"
)
stocks = pd.read_csv(file_path)
load_dotenv()
