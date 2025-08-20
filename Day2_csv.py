#Method
import csv
import os
from pathlib import Path
csv_path = "annual-enterprise-survey-2024-financial-year-provisional.csv"
new_path = "result1.csv"


#Read CSV file
with open(csv_path, newline='') as csvfile:
    file_data = csv.reader(csv_path, delimiter=' ', quotechar='|')
    for row in file_data:
        print(','.join(row))


header = ["id", "name", "age"]
rows = [
    [1, "Alice", 25],
    [2, "Bob", 30],
]

file_exist = os.path.isfile(csv_path)
with open(new_path, 'a', newline="") as csvfile:
    file = csv.writer(csvfile)

    if not file_exist:
        file.writerow(header)

    file.writerow(rows)


#Method2
fieldnames = ["id", "name", "age"]
rows = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

path_exists = os.path.isfile(new_path)
with open(new_path, mode = 'a', newline="") as f:
    file = csv.DictWriter(f, fieldnames=fieldnames)

    if not path_exists:
        file.writeheader()

    file.writerows(rows)


#Method3
import pandas as pd
header = ["id", "name", "age"]
rows = [
    [3, "Charlie", 28],
    [4, "Diana", 32],
]

df =pd.DataFrame(rows, columns = header)

if os.path.exists(new_path):
    df.to_csv(new_path,index=False)
else:
    df.to_csv(new_path, mode='a',header = False,index=False)



