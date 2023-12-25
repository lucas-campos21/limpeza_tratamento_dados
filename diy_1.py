import pandas as pd
import seaborn as srn
import statistics as sts
dataset = pd.read_csv('tempo.csv', sep = ';')
dataset.head()
dataset.shape
agrupado = dataset.groupby(['Aparencia']).size()
agrupado
agrupado.plot.bar(color = 'gray')
agrupado = dataset.groupby(['Vento']).size()
agrupado
agrupado.plot.bar(color = 'gray')
agrupado = dataset.groupby(['Jogar']).size()
agrupado
agrupado.plot.bar(color = 'gray')
dataset['Temperatura'].describe()
srn.boxplot(dataset['Temperatura']).set_title('Temperatura')
srn.distplot(dataset['Temperatura']).set_title('Temperatura')
dataset['Umidade'].describe()
srn.boxplot(dataset['Umidade']).set_title('Umidade')
srn.distplot(dataset['Umidade']).set_title('Umidade')
dataset.isnull().sum()
dataset['Umidade'].describe()
mediana = sts.median(dataset['Umidade'])
mediana
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100), 'Umidade'] = mediana
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]
dataset['Umidade'].fillna(mediana, inplace = True)
dataset['Umidade'].isnull().sum()
dataset.groupby(['Vento']).describe()
dataset.tail()
dataset['Vento'].fillna('FALSO', inplace= True)
dataset['Vento'].isnull().sum()
dataset.loc[dataset['Aparencia'] == 'menos', 'Aparencia'] = 'sol'
agrupado = dataset.groupby(['Aparencia']).size()
agrupado
mediana = sts.median(dataset['Temperatura'])
mediana
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)] = mediana
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)]