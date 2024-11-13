import pandas as pd
import numpy as np
import re
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
        Returns a clean dataframe with date column as datetime datatyp,
        no NaNs or duplicates.
        """

        # Get data and assign it to df
        df = Bellabeat().get_data()['Activity']

        # Show information about df
        print("Initial information:")
        # print(df.info())
        print(f"Number of duplicate rows: {df.duplicated().sum()}")
        print(f"Column names: {df.columns}")

        # Check for duplicates and drop them if there are any
        if df.duplicated().sum() > 0:
            df.drop_duplicates(keep="first", inplace=True)

        # Check to see if ActivityDate column has the correct dtype and change it if not
        if not pd.api.types.is_datetime64_any_dtype(df["ActivityDate"]):
            df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], errors="coerce")
        print(df.dtypes) # Check dtype change was successful

        # Define a function to convert camelCase or PascalCase to snake_case
        def camel_to_snake(name):
            # Add an underscore before each capital letter followed by a lowercase letter, then lowercase everything
            return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

        # Apply this function to all column names
        df.columns = [camel_to_snake(col) for col in df.columns]
        print("Cleaned information:")
        # print(df.info())
        print(f"Number of duplicate rows: {df.duplicated().sum()}")
        print(f"Column names: {df.columns}")

        return df

    def get_activity_level(self):

        # Get data and assign it to df
        df = Activities().clean_data()

        # Calculate activity_level for each user
        activity_level = df.groupby('id')['total_steps'].mean().reset_index()
        activity_level = activity_level.rename(columns={'total_steps': 'activity_level'})

        # Now, categorize user activity level
        bins = [0, 4999, 7499, 9999, float('inf')]
        labels = ['sedentary', 'slightly_active', 'fairly_active', 'very_active']
        activity_level['activity_category'] = pd.cut(activity_level['activity_level'], bins=bins, labels=labels)

        # Merge the categorized activity level back into the original DataFrame
        return df.merge(activity_level[['id', 'activity_category']], on='id', how='left')

    def get_activities_data(self):
        """
        Returns a clean DataFrame (without NaN), with the following columns:
        ['id', 'activity_date', 'total_steps', 'total_distance',
        'tracker_distance', 'logged_activities_distance',
        'very_active_distance', 'moderately_active_distance',
        'light_active_distance', 'sedentary_active_distance',
        'very_active_minutes', 'fairly_active_minutes',
        'lightly_active_minutes', 'sedentary_minutes', 'calories',
        'activity_category']
        """



        df = Activities().get_activity_level()




        return df
