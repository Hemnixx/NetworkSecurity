import os
import pandas as pd
from scipy.stats import ks_2samp

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_validation_config = data_validation_config
        self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        return len(dataframe.columns) == len(self._schema_config["columns"])

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        status = True
        report = {}

        for col in base_df.columns:
            ks_result = ks_2samp(base_df[col], current_df[col])
            drift = ks_result.pvalue < threshold
            report[col] = {
                "p_value": float(ks_result.pvalue),
                "drift_status": drift
            }
            if drift:
                status = False

        os.makedirs(
            os.path.dirname(self.data_validation_config.drift_report_file_path),
            exist_ok=True
        )

        write_yaml_file(
            self.data_validation_config.drift_report_file_path,
            report
        )

        return status

    def initiate_data_validation(self) -> DataValidationArtifact:
        train_df = self.read_data(self.data_ingestion_artifact.train_file_path)
        test_df = self.read_data(self.data_ingestion_artifact.test_file_path)

        if not self.validate_number_of_columns(train_df):
            raise NetworkSecurityException("Train column mismatch")

        if not self.validate_number_of_columns(test_df):
            raise NetworkSecurityException("Test column mismatch")

        self.detect_dataset_drift(train_df, test_df)

        os.makedirs(
            os.path.dirname(self.data_validation_config.valid_train_file_path),
            exist_ok=True
        )

        train_df.to_csv(self.data_validation_config.valid_train_file_path, index=False)
        test_df.to_csv(self.data_validation_config.valid_test_file_path, index=False)

        return DataValidationArtifact(
            valid_train_file_path=self.data_validation_config.valid_train_file_path,
            valid_test_file_path=self.data_validation_config.valid_test_file_path,
            invalid_train_file_path=None,
            invalid_test_file_path=None,
            drift_report_file_path=self.data_validation_config.drift_report_file_path
        )
