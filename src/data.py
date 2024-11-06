import os
from pathlib import Path
import pandas as pd

class Bellabeat:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'activity', 'calories', 'intensities' and 'steps'
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Build csv_path as "absolute path" in order to call this method from anywhere.
        # Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        # root_dir = os.path.dirname(os.path.dirname(__file__))
        # csv_path = os.path.join(root_dir, "data", "csv")
        # If __file__ is available, use it; otherwise, fall back to current working directory
        try:
            root_dir = Path(__file__).resolve().parent.parent
        except NameError:
            root_dir = Path.cwd()

        csv_path = root_dir / "data" / "csv"
        # print(f"CSV Path: {csv_path}")

        file_names = [f for f in os.listdir(csv_path) if f.endswith(".csv")]

        key_names = [
            key_name.replace("daily", "").replace("_merged", "").replace(".csv", "")
            for key_name in file_names
        ]

        # Create the dictionary
        data = {}
        for k, f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
