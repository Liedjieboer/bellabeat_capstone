import pandas as pd
import numpy as np
import datetime
from src.data import Bellabeat

class Activities:
    '''
    DataFrames containing user id's as index,
    and tracking data as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Bellabeat().get_data()
