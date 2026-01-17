import csv

class DataLoader:
    def __init__(self, file_path):
        self.filePath= file_path

    def read_csv(self):
        with open(self.filePath,"r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            return list(csvreader)