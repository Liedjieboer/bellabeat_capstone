import pandas as pd
import numpy as np
import datetime
from data import Bellabeat

class Activities:
    '''
    DataFrames containing user id's as index,
    and tracking data as columns for the activities table
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Activities
        self.data = Bellabeat().get_data()

    def get_activities_data(self):
        """
        Returns a clean DataFrame (without NaN), with the following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_products', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """

        df = Bellabeat().get_data()['Activity']
        return df
