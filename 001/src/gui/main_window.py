import tkinter as tk
from tkinter import messagebox
from src.data_ingestion.data_loader import DataLoader
from src.data_cleaning.cleaner import DataCleaner
from src.data_transformation.normalizer import DataNormalizer
from src.feature_extraction.feature_engineer import FeatureEngineer

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Preprocessing Tool")

        self.data_loader = DataLoader()
        self.cleaner = DataCleaner()
        self.normalizer = DataNormalizer()
        self.feature_engineer = FeatureEngineer()

        self.create_widgets()

    def create_widgets(self):
        load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        load_button.pack()

        clean_button = tk.Button(self.root, text="Clean Data", command=self.clean_data)
        clean_button.pack()

        normalize_button = tk.Button(self.root, text="Normalize Data", command=self.normalize_data)
        normalize_button.pack()

        feature_button = tk.Button(self.root, text="Engineer Features", command=self.engineer_features)
        feature_button.pack()

    def load_data(self):
        # Add logic to load data
        messagebox.showinfo("Info", "Data loaded successfully!")

    def clean_data(self):
        # Add logic to clean data
        messagebox.showinfo("Info", "Data cleaned successfully!")

    def normalize_data(self):
        # Add logic to normalize data
        messagebox.showinfo("Info", "Data normalized successfully!")

    def engineer_features(self):
        # Add logic to engineer features
        messagebox.showinfo("Info", "Features engineered successfully!")

    def launch(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.launch()
