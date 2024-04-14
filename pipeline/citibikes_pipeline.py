import pandas as pd
import requests
import io
import zipfile
from os import path
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from mage_ai.io.bigquery import BigQuery
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.data_preparation.decorators import data_loader  
from mage_ai.data_preparation.decorators import transformer  
from mage_ai.data_preparation.decorators import data_exporter
    
    
@data_loader
def load_data_from_aws(zip_file_url):
    response = requests.get(zip_file_url)
    zip_file = io.BytesIO(response.content)
    with zipfile.ZipFile(zip_file) as zip_file:
        file_content = zip_file.open(zip_file.namelist()[0])
        df = pd.read_csv(
        file_content, parse_dates=['started_at', 'ended_at'],
        dtype={'ride_id': str, 'start_station_id': str, 'end_station_id': str,
               'start_station_name': str, 'end_station_name': str, 'rideable_type': str,
               'member_casual': str, 'start_lat': float, 'start_lng': float, 'end_lat': float,
               'end_lng': float}
        )
    return df

@transformer
def drop_duplicate_rows(df):
    df = df.drop_duplicates()
    return df

@data_exporter
def export_data_to_datalake(df, bucket_name, file_name):
    GoogleCloudStorage.with_config(ConfigFileLoader(path.join(get_repo_path(), 'io_config.yaml'), 'default')).export(
        df, bucket_name, file_name
    )
    
@data_loader
def load_from_datalake(bucket_name, file_name):
    return GoogleCloudStorage.with_config(ConfigFileLoader(path.join(get_repo_path(), 'io_config.yaml'), 'default')).load(
        bucket_name, file_name
    )

@data_exporter
def export_data_to_datawarehouse(df, table_name):
    BigQuery.with_config(ConfigFileLoader(path.join(get_repo_path(), 'io_config.yaml'), 'default')).export(
        df, table_name, if_exists='replace'
    )

if __name__ == "__main__":
    zip_file_url = 'https://s3.amazonaws.com/tripdata/JC-201602-citibike-tripdata.csv.zip'
    
    # Load data from AWS
    df = load_data_from_aws(zip_file_url)
    
    # Execute transformer action
    df = drop_duplicate_rows(df)
    
    # Export data to datalake
    export_data_to_datalake(df, 'citibike_trips_data_bucket', '201602_citibike_trips.parquet')
    
    # Export data to datawarehouse
    export_data_to_datawarehouse(df, 'citibikes_db.citibikies_data.rides_data')