from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger


if __name__ == "__main__":
    try:
        # Pipeline-level config
        training_pipeline_config = TrainingPipelineConfig()

        # Data ingestion config
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        # Data ingestion execution
        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config
        )

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        logger.info(
            f"Data Ingestion completed successfully: {data_ingestion_artifact}"
        )

        print(data_ingestion_artifact)

    except NetworkSecurityException as e:
        logger.error(f"Error during data ingestion: {e}")
        print(f"An error occurred during data ingestion: {e}")
