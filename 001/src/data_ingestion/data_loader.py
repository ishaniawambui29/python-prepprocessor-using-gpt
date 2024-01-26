# data_loader.py
import os
import pdfplumber

class DataLoader:
    def __init__(self, data_directory='data/raw/'):
        self.data_directory = data_directory

    def load_data(self):
        texts = []
        for filename in os.listdir(self.data_directory):
            if filename.endswith('.pdf'):
                path = os.path.join(self.data_directory, filename)
                with pdfplumber.open(path) as pdf:
                    for page in pdf.pages:
                        texts.append(page.extract_text())
        return texts
