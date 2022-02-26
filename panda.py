import pandas as pd
import numpy as np
import wget
#df = pd.read_excel('teste.xlsx')
#print(df)
#print(df['Idade']*2) # é possível fazer operações com as colunas também!!!
#print(df.describe()) #retorna estatísticas sobre os valores numéricos (média, desvio padrão, valor min e max,

#SERIES
#lista_serie = np.linspace(0,1000,101)
#print(lista_serie)
#serie = pd.Series(lista_serie) #retorna uma coluna com os valores da lista
#print(serie)

#DATAFRAME
#dic_df = {'coluna 1': [1,2,3,4,5,6,7,8,9,10], 'coluna 2':[11,12,13,14,15,16,17,18,19,20]}
#df = pd.DataFrame(dic_df)
#print(df)
#print(df.head()) #mostra só os primeiros 5 dados da 'tabela'
#print(df.tail()) #mostra os 5 últimos dados da tabela
#print(df.shape) #dimensão da tabela

#IMPORTAÇÃO DE ARQUIVO CSV
site_url = 'https://raw.githubusercontent.com/laderast/cvdNight1/master/data/fullPatientData.csv'
file_name = wget.download(site_url)
df = pd.read_csv('fullPatientData.csv')
#print(df.head())

#OPERAÇÕES COM DATAFRAME
#print(df.info()) #retorna info gerais sobre os dados (obs:object, na maioria das vezes, significa str)
#print(df.describe()) #info estatísticas das colunas numéricas
#print(df.columns) #lista as colunas
#print(df.duplicated()) #mostra os valores duplicados
#print(df['patientID'].nunique()) #mostra quantos valores unicos existem na coluna
#print(df.isnull().sum())
#print(df.corr())

#Seleção, extração e slicing de dados
#print(df.age.head()) #mostra a coluna age do dataframe
#print(df['numAge'].mean()) #média dos valores da coluna 'age'
#print(df['race'].unique()) #valores únicos da coluna "race"
#print(df['race'].value_counts()) #conta os valores únicos da coluna 'race'
#print(df[['age', 'numAge']]) #mostra duas colunas
#print(df.loc[0]) #retorna dados de uma linha específica
#print(df.loc[10:15]) #retorna dados da linha 10 a 15
#print(df.loc[10:15,'smoking']) #retorna dados da linha 10 a 15 da coluna smoking'
#print(df[df['gender'] == 'F']) #filtra somente os dados em que o input da coluna 'gender' é Feminino
#print(df.loc[df['gender'] == 'F','smoking']) #filtra somente os dados em que o input da coluna 'gender' é Feminino da coluna smoking

#Análise do colesterol médio entre fumantes e não fumantes
print(f"Taxa média de colesterol entre fumantes: {df.loc[df['smoking'] == 'Y', 'tchol'].mean()}") #dados da coluna smokig em que o valor para fumante seja sim e pega somente o valor total (tchol)
print(f"Taxa média de colesterol entre não fumantes: {df.loc[df['smoking'] == 'N', 'tchol'].mean()}")