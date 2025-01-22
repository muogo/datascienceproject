from src.datascienca.config.configuration import ConfigurationManager
from src.datascienca.components.model_tranier import ModelTrainer
from src.datascienca import logger


STAGE_NAME = "Model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

