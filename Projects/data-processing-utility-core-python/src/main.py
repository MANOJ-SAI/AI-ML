import dataset_generator
import data_loader
import data_processor

class Main:
    def __init__(self, file_path):
        self.filePath = file_path
        self.data=[]
        self.dataset_generator = dataset_generator.DatasetGenerator(file_path, 2)
        self.data_loader = data_loader.DataLoader(file_path)
        self.data_processor = data_processor.DataProcessor(self.data_loader)
        self.processed_data= None

    def generate_dataset(self):
        self.dataset_generator.generate_csv()
        print("data generated")

    def data_loading(self):
        self.data =  self.data_loader.read_csv()
        print("data loaded")

    def data_processing(self):
        self.processed_data = self.data_processor.remove_empty_records()
        print("data processed")

    def save_processed_data(self):
        self.dataset_generator.write_csv("processed_data.csv",self.processed_data)
        print("data saved")

    def execute(self):
        self.generate_dataset()
        self.data_loading()
        self.data_processing()
        self.save_processed_data()

if "__main__" == __name__:
    main = Main("../data/input_data.csv")
    main.execute()