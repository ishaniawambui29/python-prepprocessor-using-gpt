import os
import tkinter as tk
from tkinter import filedialog

def create_file(path):
    with open(path, 'w') as f:
        pass  # Creates an empty file

def create_directory_structure(root_path):
    structure = {
        "data/raw": [],
        "data/interim": [],
        "data/processed": [],
        "docs": ["setup_instructions.md", "usage_guide.md"],
        "src": ["main.py"],
        "src/data_ingestion": ["__init__.py", "data_loader.py", "data_validator.py"],
        "src/data_cleaning": ["__init__.py", "cleaner.py", "noise_removal.py"],
        "src/data_transformation": ["__init__.py", "normalizer.py", "scaler.py"],
        "src/feature_extraction": ["__init__.py", "feature_selector.py", "feature_engineer.py"],
        "src/gui": ["__init__.py", "main_window.py", "widgets.py"],
        "src/api": ["__init__.py", "endpoints.py", "request_handlers.py"],
        "src/utils": ["__init__.py", "logger.py", "config_parser.py"],
        "tests": ["__init__.py", "test_data_loader.py", "test_cleaner.py", "test_normalizer.py", "test_gui.py"],
        "notebooks": [],
        "static/images": [],
        "static/styles": [],
        "templates": ["main_page.html"]
    }

    for directory, files in structure.items():
        full_dir_path = os.path.join(root_path, directory)
        os.makedirs(full_dir_path, exist_ok=True)
        for file in files:
            full_file_path = os.path.join(full_dir_path, file)
            create_file(full_file_path)

    print(f"File structure with files created in {root_path}")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Show the dialog and get the folder
    if folder_selected:
        create_directory_structure(folder_selected)
    else:
        print("Folder selection cancelled.")

if __name__ == "__main__":
    select_folder()
