from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig
)
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

    except Exception as e:
        raise NetworkSecurityException(e)
