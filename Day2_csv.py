#Method
from pathlib import Path
csv_path = "annual-enterprise-survey-2024-financial-year-provisional.csv"
import csv
import os

# if os.path.isfile(csv_path):
#     print("Exists")


#Read CSV file
with open(csv_path, newline='') as csvfile:
    file_data = csv.reader(csv_path, delimiter=' ', quotechar='|')
    for row in file_data:
        print(','.join(row))

