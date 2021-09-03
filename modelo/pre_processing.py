# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

class PreProcessing:
    # Função para gerar valores de classes para o cut.
    def geraClasses(inicio, fim, intervalo, adiciona):
      # Intervalo para as faixas.
      classes_faixas = []
      classes_faixas = list(range(inicio, fim, intervalo))
      #classes_renda.append(1000000)
      classes_faixas.append(adiciona)
      #print("Classes: ", classes)
    return classes_faixas
  
    
'''   
    # Função para gerar labels das classes para o cut.
    def geraFaixasClasse(classe):
      # Labels para as faixas de renda.
      labels_faixas = classe.copy()
      labels_faixas.remove(0)
      #print("Labels Faixas: ", labels_faixas)
      #return classes, labels_faixas
      #rangeForText(classe, labels_faixas)
      return labels_faixas
      
    # Função para gerar labels das classes para gráficos.
    def rangeForTextInGraph(classe, labels_faixas):
      faixas = []
      contador = 0
    
      for i, ii in zip(classe, labels_faixas):
        if contador < 1:
          faixas.append("{} a {}".format(i, ii))
          contador += 1
        else:
          faixas.append("{} a {}".format(i+1, ii))
    
      return faixas
  
    # Função para gerar valor da faixa no DataFrame.
    def FaixasAtTheData(dados, coluna:str, classes, faixas):
      dados[coluna + "_BIN"] = pd.cut(x = dados[coluna], 
                                      bins = classes, 
                                      labels = faixas)
      return dados[coluna + "_BIN"]
    
    # Função para gerar faixa no DataFrame para plotar no gráfico.
    def FaixasForGraphAtTheData(dados, coluna:str, classes, faixas):
      dados[coluna + "_TEXT"] = pd.cut(x = dados[coluna], 
                                      bins = classes, 
                                      labels = faixas)
      return dados[coluna + "_TEXT"]
    
    # Função para transformar valor em string.
    def rangeForText(dados, coluna):
      dados[coluna+"_TEXT_TESTE"] = dados[coluna].apply(lambda x:str(x))
      return dados[coluna+"_TEXT_TESTE"] '''