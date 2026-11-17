import pandas as pd
import os

def load_and_clean_vgsales(csv_path: str = "data/raw/vgsales.csv") -> pd.DataFrame:
    """Loads the video game sales dataset and drops rows with missing global sales."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at {csv_path}. Please place vgsales.csv in data/raw/")
    
    df = pd.read_csv(csv_path)
    df_cleaned = df.dropna(subset=["Global_Sales"]).reset_index(drop=True)
    return df_cleaned
