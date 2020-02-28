import csv
import os.path
from models.Transaction import Transaction


class DataService:

    # function reads csv file and returns list of created objects
    def read_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "bakery100.csv")

        received_objects = []

        with open(path) as csv_file:
            values = list(csv.reader(csv_file))
            transactions_num = len(values) - 1
            first_line = True
            products = []
            currentId = 1
            for obj in values:
                if (first_line):
                    first_line = False
                    continue

                if 'NONE' in obj:
                    continue

                if int(obj[2]) == currentId:
                    products.append(obj[3])
                else:
                    received_objects.append(Transaction(obj[0], products))
                    products = []
                    products.append(obj[3])
                    currentId += 1

        return transactions_num, received_objects

