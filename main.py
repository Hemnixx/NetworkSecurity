from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation   
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
    DataValidationConfig,
    DataTransformationConfig
)
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(
            trainingpipelineconfig
        )

        data_ingestion = DataIngestion(dataingestionconfig)

        logger.info("Initiate the data ingestion")

        dataingestionartifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logger.info("Data Ingestion Completed")
        print(dataingestionartifact)

        # ---- Data Validation ----
        data_validation_config = DataValidationConfig(
            trainingpipelineconfig
        )
        data_validation = DataValidation(
            dataingestionartifact,
            data_validation_config
        )

        logger.info("Data Validation Started")

        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        logger.info("Data Validation Completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        DataTransformation_artifact=data_transformation.initiate_data_transformation()
        logger.info("Data Transformation Completed")
        print(DataTransformation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
