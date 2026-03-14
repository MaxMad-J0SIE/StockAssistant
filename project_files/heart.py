import csv

class Heart:
    """
    Heart of the project
    All the backend happens here
    """
    def __init__(self):
        self.csv_file_location = "../project_data/stocks.csv"
        self.csv_file = self.file_opening()
        self.csv_file_read = []

    def file_opening(self):
        try:
            temp_csv_file = open(self.csv_file_location, mode='r')
            return temp_csv_file
        except FileNotFoundError:
            print("File not found")

    def file_close(self):
        self.file.close()

    def read_data(self):
        temp_read = csv.reader(self.csv_file, delimiter=',')
        for row in temp_read:
            self.csv_file_read.append(row)
        return self.csv_file_read