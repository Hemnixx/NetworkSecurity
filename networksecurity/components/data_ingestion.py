import os
import sys
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split
from typing import Tuple
from dotenv import load_dotenv
import certifi

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            logger.info("Data Ingestion component initialized")
        except Exception as e:
            raise NetworkSecurityException(e)

    def export_collection_as_dataframe(self):
        try:
            client = pymongo.MongoClient(
                MONGO_DB_URL, tlsCAFile=ca
            )
            collection = client[
                self.data_ingestion_config.database_name
            ][self.data_ingestion_config.collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            df.replace("na", pd.NA, inplace=True)
            logger.info(f"Dataframe shape: {df.shape}")

            return df
        except Exception as e:
            raise NetworkSecurityException(e)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame) -> str:
        try:
            os.makedirs(
                os.path.dirname(
                    self.data_ingestion_config.feature_storea_file_path
                ),
                exist_ok=True
            )

            dataframe.to_csv(
                self.data_ingestion_config.feature_storea_file_path,
                index=False
            )

            logger.info(
                f"Feature store saved at "
                f"{self.data_ingestion_config.feature_storea_file_path}"
            )

            return self.data_ingestion_config.feature_storea_file_path
        except Exception as e:
            raise NetworkSecurityException(e)

    def split_data_as_train_test(
        self, dataframe: pd.DataFrame
    ) -> Tuple[str, str]:
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
            )

            os.makedirs(
                os.path.dirname(
                    self.data_ingestion_config.training_file_path
                ),
                exist_ok=True
            )

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False
            )

            return (
                self.data_ingestion_config.training_file_path,
                self.data_ingestion_config.testing_file_path,
            )
        except Exception as e:
            raise NetworkSecurityException(e)

    def initiate_data_ingestion(self):
        try:
            df = self.export_collection_as_dataframe()

            feature_store_path = self.export_data_into_feature_store(df)

            train_path, test_path = self.split_data_as_train_test(df)

            artifact = DataIngestionArtifact(
                feature_store_file_path=feature_store_path,
                train_file_path=train_path,
                test_file_path=test_path
            )

            logger.info("Data ingestion completed successfully")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e)
