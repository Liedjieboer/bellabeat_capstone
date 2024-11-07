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

    def clean_data(self):
        """
        Returns a clean dataframe with all datatypes as it should be and no NaNs
        """

        # Get data and assign it to df
        df = Bellabeat().get_data()['Activity']

        # Show information about df
        print("Initial information:")
        print(df.info())

        # Check to see if ActivityDate column has the correct dtype and change it if not
        if not pd.api.types.is_datetime64_any_dtype(df["ActivityDate"]):
            df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], errors="coerce")
        print(df.dtypes) # Check dtype change was successful

        return df

    

    def get_activities_data(self):
        """
        Returns a clean DataFrame (without NaN), with the following columns:
        ['Id', 'ActivityDate', 'TotalSteps', 'TotalDistance',
        'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance',
        'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes',
        'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']
        """

        df = Bellabeat().get_data()['Activity']
        return df
