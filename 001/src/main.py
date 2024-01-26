# main.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.data_ingestion.data_loader import DataLoader
from src.data_cleaning.cleaner import DataCleaner
from src.data_transformation.normalizer import DataNormalizer
from src.feature_extraction.feature_engineer import FeatureEngineer

def main():
    # Initialize components
    data_loader = DataLoader()
    cleaner = DataCleaner()
    normalizer = DataNormalizer()
    feature_engineer = FeatureEngineer()

    # Load, clean, normalize, and feature engineer data
    raw_data = data_loader.load_data()
    cleaned_data = cleaner.clean(raw_data)
    normalized_data = normalizer.normalize(cleaned_data)
    features = feature_engineer.engineer_features(normalized_data)

    # Here, features can be saved or passed directly to a machine learning model

if __name__ == "__main__":
    main()
