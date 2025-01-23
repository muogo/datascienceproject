from src.datascienca.config.configuration import ConfigurationManager
from src.datascienca.components.model_evaluation import ModelEvaluation
from src.datascienca import logger


STAGE_NAME = "Data Validation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_model_evaluation_config()
        data_validation = ModelEvaluation(config=data_validation_config)
        data_validation.log_into_mlflow()


