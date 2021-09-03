# -*- coding: utf-8 -*-

import pandas as pd

class Model():
    def __init__(self):
        self.df_ap = pd.read_csv("./dados/application_record.csv")
        self.df_cr = pd.read_csv("C:/Users/rafhael.martins/Documents/Aulas_Thiago-Russo/Práticas/Credit_Card_Approval_Prediction1/Credit_Card_Approval_Prediction/dados/credit_record.csv")
        
    def read_files(self):
        print(self.df_ap.head())
        print(self.df_ap.info(memory_usage='deep'))
        

Model.read_files(Model())