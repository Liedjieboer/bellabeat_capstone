import pandas as pd
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

        # Check for duplicates and drop them if there are any
        if df.duplicated().sum() > 0:
            df.drop_duplicates(keep="first", inplace=True)

        # Check to see if ActivityDate column has the correct dtype and change it if not
        if not pd.api.types.is_datetime64_any_dtype(df["ActivityDate"]):
            df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], errors="coerce")
        # print(df.dtypes) # Check dtype change was successful

        # Define a function to convert camelCase or PascalCase to snake_case
        def camel_to_snake(name):
            # Add an underscore before each capital letter followed by a lowercase letter, then lowercase everything
            return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

        # Apply this function to all column names
        df.columns = [camel_to_snake(col) for col in df.columns]
        # print("Cleaned information:")
        # # print(df.info())
        # print(f"Number of duplicate rows: {df.duplicated().sum()}")
        # print(f"Column names: {df.columns}")

        return df

    def get_activity_level(self):

        # Get data and assign it to df
        df = Activities().clean_data()

        # Calculate activity_level for each user
        activity_level = df.groupby('id')['total_steps'].mean().reset_index()
        activity_level = activity_level.rename(columns={'total_steps': 'activity'})

        # Now, categorize user activity level
        bins = [0, 4999, 7499, 9999, float('inf')]
        labels = ['sedentary', 'slightly_active', 'fairly_active', 'very_active']
        activity_level['activity_level'] = pd.cut(activity_level['activity'], bins=bins, labels=labels)

        # Merge the categorized activity level back into the original DataFrame
        return df.merge(activity_level[['id', 'activity_level']], on='id', how='left')

    def get_activity_category(self):
        df = Activities.clean_data(self)

        # Calculate the mean activity metrics for each user
        user_activity_mean = df.groupby('id').mean().reset_index()

        # Define thresholds (adjust as needed for average values across days)
        runner_distance_threshold = 3.0  # Mean very active distance threshold for runners
        runner_minutes_threshold = 20    # Mean very active minutes threshold for runners
        walker_distance_threshold = 2.0  # Mean moderately or light active distance threshold for walkers
        walker_minutes_threshold = 20    # Mean fairly active minutes threshold for walkers

        # Create a function to classify each user based on their mean activity
        def classify_user(row):
            if row['very_active_distance'] >= runner_distance_threshold and row['very_active_minutes'] >= runner_minutes_threshold:
                return 'runner'
            elif (row['moderately_active_distance'] >= walker_distance_threshold or
                row['light_active_distance'] >= walker_distance_threshold) and row['fairly_active_minutes'] >= walker_minutes_threshold:
                return 'walker'
            else:
                return 'non-exerciser'

        # Apply the classification function to each user in the grouped data
        user_activity_mean['activity_type'] = user_activity_mean.apply(classify_user, axis=1)

        # Step 5: Merge the classification back into the original DataFrame if desired
        return user_activity_mean

    def get_activities_data(self):
        """
        Returns a clean DataFrame (without NaN), with the following columns:
        ['id', 'activity_date', 'total_steps', 'total_distance',
        'tracker_distance', 'logged_activities_distance',
        'very_active_distance', 'moderately_active_distance',
        'light_active_distance', 'sedentary_active_distance',
        'very_active_minutes', 'fairly_active_minutes',
        'lightly_active_minutes', 'sedentary_minutes', 'calories',
        'activity_level', 'activity_type']
        """

        df = Activities().get_activity_level()

        return df.merge(Activities.get_activity_category(self)[['id', 'activity_type']], on='id', how='left')
