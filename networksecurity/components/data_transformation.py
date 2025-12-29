import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constant.training_pipeline import (
    TARGET_COLUMN,
    DATA_TRANSFORMATION_IMPUTER_PARAMS
)
from networksecurity.entity.artifact_entity import (
    DataValidationArtifact,
    DataTransformationArtifact
)
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.utils.main_utils.utils import (
    save_numpy_array_data,
    save_object
)


class DataTransformation:
    def __init__(
        self,
        data_validation_artifact: DataValidationArtifact,
        data_transformation_config: DataTransformationConfig
    ):
        self.data_validation_artifact = data_validation_artifact
        self.data_transformation_config = data_transformation_config

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    def get_data_transformer_object(self) -> Pipeline:
        imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
        return Pipeline([("imputer", imputer)])

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        train_df = self.read_data(self.data_validation_artifact.valid_train_file_path)
        test_df = self.read_data(self.data_validation_artifact.valid_test_file_path)

        if TARGET_COLUMN not in train_df.columns:
            raise NetworkSecurityException(f"{TARGET_COLUMN} not found")

        X_train = train_df.drop(columns=[TARGET_COLUMN])
        y_train = train_df[TARGET_COLUMN].replace(-1, 0)

        X_test = test_df.drop(columns=[TARGET_COLUMN])
        y_test = test_df[TARGET_COLUMN].replace(-1, 0)

        preprocessor = self.get_data_transformer_object()
        X_train_arr = preprocessor.fit_transform(X_train)
        X_test_arr = preprocessor.transform(X_test)

        train_arr = np.c_[X_train_arr, y_train]
        test_arr = np.c_[X_test_arr, y_test]

        save_numpy_array_data(
            self.data_transformation_config.transformed_train_file_path,
            train_arr
        )
        save_numpy_array_data(
            self.data_transformation_config.transformed_test_file_path,
            test_arr
        )

        os.makedirs("final_model", exist_ok=True)
        save_object(
            self.data_transformation_config.transformed_object_file_path,
            preprocessor
        )

        return DataTransformationArtifact(
            transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
            transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
            transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
        )
