import os
from src.datascienca import logger
from sklearn.model_selection import train_test_split
from src.datascienca.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config= config
        
    ## Catatan: Anda dapat menambahkan berbagai teknik transformasi data seperti Scaler, PCA, dan lain-lain
    #Anda dapat melakukan semua jenis EDA dalam siklus ML di sini sebelum meneruskan data ini ke model
    # Saya hanya menambahkan train_test_spliting karena data ini sudah dibersihkan
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Membagi data menjadi set pelatihan dan pengujian. (0,75, 0,25) dibagi.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
    
