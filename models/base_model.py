import json
import os
from datetime import datetime

class BaseModel:
    """Base model class for simple file-based data storage"""
    
    def __init__(self):
        self.data_dir = 'data'
        self.ensure_data_dir()
    
    def ensure_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def get_file_path(self, filename):
        return os.path.join(self.data_dir, f"{filename}.json")
    
    def save_data(self, filename, data):
        filepath = self.get_file_path(filename)
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2, default=str)
    
    def load_data(self, filename):
        filepath = self.get_file_path(filename)
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def generate_id(self, data_list):
        if not data_list:
            return 1
        return max(item.get('id', 0) for item in data_list) + 1