import os
import sys
from src.exception import CustomException 
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig 



@dataclass
class DataIngetionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv') 
    raw_data_path: str=os.path.join('artifacts','data.csv') 

class DataIngetion:
    def __init__(self):
        self.ingetion_config = DataIngetionConfig() 

    def initiate_data_ingetion(self):
        logging.info('Entered the data ingetion method or component')
        try:
            df =pd.read_csv('notebook/data/stud.csv')
            logging.info('Reading the dataset as dataframe') 

            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)

            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingetion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingetion_config.test_data_path,index=False,header=True) 

            logging.info('Ingetion of the data is successfull') 

            return(
                self.ingetion_config.train_data_path,
                self.ingetion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj = DataIngetion()
    train_data,test_data = obj.initiate_data_ingetion()  

    data_transformation =DataTransformation() 
    data_transformation.initiate_data_transformation(train_data,test_data)  
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data) 
    