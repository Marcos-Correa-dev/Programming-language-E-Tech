import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv("titanic.csv")
print(df)



print("-"*20)
print("TYPES DO DATAFRAME")
print(df.dtypes)
print("-"*20)

#--- ANALISE DAS VARIAVEIS QUALITATIVAS E QUANTITATIVAS
quant= []
quali= []

for i in df.dtypes.index:
    if df.dtypes[i]=="object":
        quali.append(i)
    else:
        quant.append(i)
print("\n"+"-"*20)
print("CATEGORIAS DE QUALIDADE OU QUANTIDADE")
print("\n Qualidade: ",quali)
print("\n Quantidade: ",quant)
print("\n"+"-"*20)

#------------------------------------------------------------

# CRIA UM DATAFRAME APARTIR DE UMA LISTA
df_quant= df[quant]
print("\n"+"-"*20)
print("\nDATAFRAME QUANTIDADE")
print("\n",df_quant)
print("\nMEDIA: ",df_quant.median())
print("\n"+"-"*20)


print("\n"+"-"*20)
print("\nDATAFRAME QUALIDADE")
df_quali=df[quali]
print("\n", df_quali)
print("\n"+"-"*20)
print("\nTABELA DE FREQUENCIA")
print("\n",df_quali.groupby("Sex").Name.count())#Um de cada vez
print("\n"+"-"*20)
for i in df_quali.columns:
    if i == "Name":
        pass
    else:
        print("-------------")
        print("variavel: ", i )
        print(df_quali.groupby(i).Name.count())#Todos de uma vez
        print("-------------")


#ANALISE DOS SOBREVIVENTES POR CATEGORIA
print("\n"+"-"*20)
print("ANALISE DOS SOBREVIVENTES POR CATEGORIA")
print("\n"+"-"*20)

#SOBREVIVENTES POR GENERO (GRAFICO)
sb.countplot(x='Sex', hue='Survived', data=df)
plt.title('Sobrevivência por Gênero')
plt.xlabel('Classe (1=Primeira, 3=Terceira)')
plt.ylabel('Contagem de Passageiros')
plt.show()
print()

#SOBREVIVENTES POR IDADE (GRAFICO)

print("\n"+"-"*20)
sb.histplot(data=df, x="Age", hue="Survived", kde=True )
plt.title("Sobrevivencia por Idade")
plt.xlabel("Idade")
plt.show()
print()


#TRATAMENTO DO PORTO DE EMBARQUE
print("\n"+"-"*20)
print("TRATAMENTO DO PORTO DE EMBARQUE ")
print("-"*20)
moda_embarque= df["Embarked"].mode()[0]
print(f"Moda da coluna 'Embarked' (usada para preenchimento): {moda_embarque}")
df['Embarked'].fillna(moda_embarque, inplace=True)

print("\nValores nulos na coluna 'Embarked' após o preenchimento:")
print(df['Embarked'].isnull().sum())
print("-"*20)