# src/data_pipeline.py
from src.data_processing import clean_data, compute_derived_features
import pandas as pd

class SolarDataPipeline:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)

    def process_data(self):
        self.df = clean_data(self.df)
        self.df = compute_derived_features(self.df)

    def export_data(self, output_path):
        self.df.to_csv(output_path, index=False)
