from faker import Faker
import csv
import random


class DatasetGenerator:
    def __init__(self,filename,num_rows):
        self.fake = Faker()
        self.fieldnames = ["name","age","salary"]
        self.num_rows = num_rows
        self.filename = filename


    def generate_rows(self):
        rows = []
        for _ in range(self.num_rows):
            rows.append({
                "name": self.fake.name(),
                "age": random.randint(22, 50),
                "salary": random.choice(range(200000, 2000000, 100000))
            })
        return rows

    def write_csv(self, filename,rows=None):
        rows = self.generate_rows() if rows is None else rows

        with open(filename,"w",newline="") as csvfile:
            csvwriter = csv.DictWriter(csvfile,self.fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(rows)

    def generate_and_add_missing_values(self):
        rows= self.generate_rows()
        for row_num,row in enumerate(rows):
            if row_num%2==0:
                row["age"]=None
        return rows

    def generate_csv(self):
        rows=self.generate_and_add_missing_values()
        self.write_csv(self.filename,rows)