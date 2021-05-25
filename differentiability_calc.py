  
import pandas as pd
import statsmodels.api as sm
import numpy as np
from copy import deepcopy

from dateutil.relativedelta import relativedelta

import warnings

# from .Utils.Utils import *

class PecoraDiff():
    """
        Functional class to calculate Pecora Differentiability measure between two time series, to detect causality between two time series
        
    """
    def __init__(self, ):
        """
        Args :
            DF      - (DataFrame) Time series data for X and Y 
            endog   - (string)
            exog    - (string)
            lag     - (integer) time delay between coordiate of points
            dim     - (integer) the dimension of shadow manifold
        """
    
