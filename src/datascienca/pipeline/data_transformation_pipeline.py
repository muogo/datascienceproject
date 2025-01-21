from src.datascienca.config.configuration import ConfigurationManager
from src.datascienca.components.data_transformation import DataTransformation
from src.datascienca import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            
            else:
                raise Exception("Schema data anda tidak valid")
        
        except Exception as e:
            print(e)
        
        