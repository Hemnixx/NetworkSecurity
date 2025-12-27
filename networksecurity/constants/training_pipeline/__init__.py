import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN:str= "Result"
PIPELINE_NAME:str= "network_security"
ARTIFACT_DIR:str= "artifact"
FILE_NAME:str= "phising_data.csv"

TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str= "test.csv"

DATA_INGESTON_COLLECTION_NAME:str= "phishing_Data"
DATA_INGESTION_DATABASE_NAME:str= "network_security"
DATA_INGESTION_DIR_NAME:str= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str= "feature_store"
DATA_INGESTION_INGESTED_DIR:str= "ingested"
DATA_INGESTION_TRAIN_SPLIT_RATIO:float= 0.2

