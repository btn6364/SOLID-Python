from abc import ABC, abstractmethod

class DataSource(ABC): 
    
    @abstractmethod
    def get_data(self): 
        pass

class DataFromDatabase(DataSource): 
    def get_data(self):
        return "Data from the database"

class DataFromAPI(DataSource):
    def get_data(self):
        return "Data from the API"

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)
    
front_end = FrontEnd(DataFromDatabase())
front_end.display_data()

front_end = FrontEnd(DataFromAPI())
front_end.display_data()