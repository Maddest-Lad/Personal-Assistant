"""
 Python Script:
  Combine/Merge multiple CSV files using the Pandas library
"""
import os

import pandas as pd


# Produce a single CSV after combining all files
def combine(list_of_files, file_out):
    try:
        # Consolidate all CSV files into one object
        result_obj = pd.concat([pd.read_csv(file, engine='python') for file in list_of_files])
        # Convert the above object into a csv file and export
        result_obj.to_csv(file_out, index=False, encoding="utf-8", )
    except:
        pass


# Move to the path that holds our CSV files
csv_file_path = "C:/Users/samha/Desktop/Texts"
os.chdir(csv_file_path)
list_of_files = os.listdir(csv_file_path)

file_out = "ConsolidateOutput.csv"
combine(list_of_files, file_out)
