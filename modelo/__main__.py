# -*- coding: utf-8 -*-
# Importando Bibliotecas.
import pandas as pd
import numpy as np
import pre_processing

# Classe para o modelo.
class Model:
    def __init__(self):
        self.df_ap = pd.read_csv("../dados/application_record.csv")
        self.df_cr = pd.read_csv("../dados/credit_record.csv")
        
    def PreparingData(self):
        #print(pre_processing.PreProcessing.geraClasses(0, 525000, 25000, np.Infinity))
        classes_renda = Model.generates_classes(0, 525000, 25000)
        #print(classes_renda)
        return(self, classes_renda)
        
    # Função para gerar valores de classes para o cut.
    def generates_classes(inicio, fim, intervalo):
        adiciona = np.Infinity
        classes_faixas = []
        classes_faixas = list(range(inicio, fim, intervalo))
        classes_faixas.append(adiciona)
        return classes_faixas
        

#Model.PreparingData(Model())
Model.generates_classes(Model(0, 525000, 25000))