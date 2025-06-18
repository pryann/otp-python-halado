import csv


# Generator to read a CSV file and yield each row
def read_scv_from_gen(file):
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row
