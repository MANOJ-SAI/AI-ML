import data_loader

class DataProcessor:
    def __init__(self,data_load):
        self.data = data_load

    def remove_empty_records(self):
        data_dic= self.data.read_csv()
        return [record for record in data_dic if all(record_object not in ("", None) for record_object in record.values())]
