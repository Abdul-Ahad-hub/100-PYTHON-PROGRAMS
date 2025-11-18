import csv
import json

def read_file_csv():
    with open("Stuff/test.csv", "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def read_file_json():
    with open("Stuff/test.json", "r") as file:
        data = json.load(file)
    print(data)


read_file_csv()
read_file_json()