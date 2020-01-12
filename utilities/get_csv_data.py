import csv


def getCsvData(file_name):
    # create an empty list
    rows = []
    # open csv file
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # skip the header
        next(reader)
        # add rows from reader to list
        for row in reader:
            rows.append(row)
        return rows
