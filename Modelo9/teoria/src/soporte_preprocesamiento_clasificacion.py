# Tratamiento de datos
# -----------------------------------------------------------------------
import numpy as np
import pandas as pd

# Otros objetivos
# -----------------------------------------------------------------------
import math

# Gráficos
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

import os
import sys 

import warnings
warnings.filterwarnings("ignore")
sys.path.append(os.path.abspath("src"))   
import soporte_preprocesamiento_clasificacion as f

from scipy.stats import chi2_contingency

# -----------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


## EDA

def exploracion_dataframe(dataframe, columna_control):
    """
    Realiza un análisis exploratorio básico de un DataFrame, mostrando información sobre duplicados,
    valores nulos, tipos de datos, valores únicos para columnas categóricas y estadísticas descriptivas
    para columnas categóricas y numéricas, agrupadas por la columna de control.

    Params:
    - dataframe (DataFrame): El DataFrame que se va a explorar.
    - columna_control (str): El nombre de la columna que se utilizará como control para dividir el DataFrame.

    Returns: 
    No devuelve nada directamente, pero imprime en la consola la información exploratoria.
    """
    print(f"El número de datos es {dataframe.shape[0]} y el de columnas es {dataframe.shape[1]}")
    print("\n ..................... \n")

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())    
    
    # como estamos en un problema de A/B testing y lo que realmente nos importa es comparar entre el grupo de control y el de test, los principales estadísticos los vamos a sacar de cada una de las categorías
    
    # for categoria in dataframe[columna_control].unique():
    #     dataframe_filtrado = dataframe[dataframe[columna_control] == categoria]
    
    #     print("\n ..................... \n")
    #     print(f"Los principales estadísticos de las columnas categóricas para el {categoria} son: ")
    #     display(dataframe_filtrado.describe(include = "O").T)
        
    #     print("\n ..................... \n")
    #     print(f"Los principales estadísticos de las columnas numéricas para el {categoria} son: ")
    #     display(dataframe_filtrado.describe().T)


def separar_dataframe(df):
    return df.select_dtypes(include=np.number), df.select_dtypes(include="O")



def plot_numericas(df, tamanio):
    cols_numericas=df.columns

    nfilas=math.ceil(len(cols_numericas) /2)  #es para que si da 4,5, se quede con 5 y no con 4 porque de normal redondea hacia abajo
    fig, axes = plt.subplots(nrows= nfilas, ncols= 2, figsize= tamanio)
    axes=axes.flat
    for indice,col in enumerate(cols_numericas):
        sns.histplot(x=col, data= df, ax= axes[indice], bins=50)
        axes[indice].set_title(col)
        axes[indice].set_xlabel("")


    if len(cols_numericas) %2 != 0:
        fig.delaxes(axes[-1])
    else:
        pass

    plt.tight_layout()
    
def plot_categoricas(df, tamanio, paleta="mako"):
    cols_categoricas=df.columns

    nfilas=math.ceil(len(cols_categoricas) /2)  #es para que si da 4,5, se quede con 5 y no con 4 porque de normal redondea hacia abajo
    fig, axes = plt.subplots(nrows= nfilas, ncols= 2, figsize= tamanio)
    axes=axes.flat
    for indice,col in enumerate(cols_categoricas):
        sns.countplot(x=col, data= df, ax= axes[indice], palette=paleta, order= df[col].value_counts().index)
        axes[indice].set_title(col)
        axes[indice].set_xlabel("")
        axes[indice].tick_params(rotation=90)
        plt.tight_layout() 


    if len(cols_categoricas) %2 != 0:
        fig.delaxes(axes[-1])
    else:
        pass

    plt.tight_layout()    


def relacion_dependiente_categoricas(df, variable_dependiente, tamanio=(15,8), paleta="mako"):
    df_cat= f.separar_dataframe(df)[1]
    cols_categoricas=df_cat.columns
    nfilas=math.ceil(len(cols_categoricas) /2)  #es para que si da 4,5, se quede con 5 y no con 4 porque de normal redondea hacia abajo
    fig, axes = plt.subplots(nrows= nfilas, ncols= 2, figsize= tamanio)
    axes=axes.flat

    for indice, col in enumerate(cols_categoricas):
        datos_agrupados= df.groupby(col)[variable_dependiente].mean().reset_index().sort_values(variable_dependiente, ascending=False)
        sns.barplot(x=col ,y=variable_dependiente, data=datos_agrupados, palette=paleta, ax=axes[indice])
        axes[indice].tick_params(rotation=90)
        axes[indice].set_title(f"Relación entre {col} y {variable_dependiente}")
        axes[indice].set_xlabel("")
    plt.tight_layout()



def relacion_dependiente_numericas(df, variable_dependiente, tamanio=(15,8), paleta="mako"):
    df_numericas= f.separar_dataframe(df)[0]
    cols_numericas=df_numericas.columns
    nfilas=math.ceil(len(cols_numericas) /2)  #es para que si da 4,5, se quede con 5 y no con 4 porque de normal redondea hacia abajo
    fig, axes = plt.subplots(nrows= nfilas, ncols= 2, figsize= tamanio)
    axes=axes.flat

    for indice, col in enumerate(cols_numericas):
        if col == variable_dependiente:
            fig.delaxes(axes[indice])
        else:
            sns.scatterplot(x=col ,y=variable_dependiente, data=df_numericas, palette=paleta, ax=axes[indice])

            axes[indice].set_title(f"Relación entre {col} y {variable_dependiente}")
            axes[indice].set_xlabel("")
    plt.tight_layout()


def matriz_correlacion(df,tamanio=(10,7)):
    matriz_corr=df.corr(numeric_only=True)
    plt.figure(figsize=tamanio)
    mascara=np.triu(np.ones_like(matriz_corr, dtype=np.bool_))
    sns.heatmap(matriz_corr, annot=True, vmin=-1, vmax=1, mask=mascara)
    plt.tight_layout()



## ANALIZAR ORDEN con CHI 2 (Encoding)

def detectar_orden_cat(df,lista_cat,var_respuesta):
    for categoria in lista_cat:
        print(f"Estamos evaluando el orden de la variable {categoria.upper()}")
        df_cross_tab=pd.crosstab(df[categoria], df[var_respuesta])
        display(df_cross_tab)
        
        chi2, p, dof, expected= chi2_contingency(df_cross_tab)

        if p <0.05:
            print(f"La variable {categoria} SI tiene orden")
        else:
            print(f"La variable {categoria} NO tiene orden")




## CALCULAR MÉTRICAS DE LOGISTICA

def calcular_metricas(y_train, y_test, pred_train, pred_test, ymodelo_nombre):
    """
    Calcula métricas de rendimiento para el modelo seleccionado.
    """

    # Métricas
    metricas_train = {
        "accuracy": accuracy_score(y_train, pred_train),
        "precision": precision_score(y_train, pred_train, average='weighted', zero_division=0),
        "recall": recall_score(y_train, pred_train, average='weighted', zero_division=0),
        "f1": f1_score(y_train, pred_train, average='weighted', zero_division=0)
    }
    metricas_test = {
        "accuracy": accuracy_score(y_test, pred_test),
        "precision": precision_score(y_test, pred_test, average='weighted', zero_division=0),
        "recall": recall_score(y_test, pred_test, average='weighted', zero_division=0),
        "f1": f1_score(y_test, pred_test, average='weighted', zero_division=0)
    }

    return pd.DataFrame({"train": metricas_train, "test": metricas_test})
        