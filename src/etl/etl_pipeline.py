from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data

def etl_pipeline():
    df = extract_data()
    df_transformed = transform_data(df)
    load_data(df_transformed)

if __name__ == "__main__":
    etl_pipeline()
