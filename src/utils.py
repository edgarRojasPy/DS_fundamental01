import numpy as np
import pandas as pd

def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando Numpy
    datos =  np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1,names=True)
    return datos
def cargar_datos_pd(ruta_archivo):
    # Carga los datos del archivo CSV utilizando Pandas.
    datos = pd.read_csv(ruta_archivo, sep=',',header=0)
    return datos
def ver_resumen_nulos(df):
    qna=df.isnull().sum(axis=0)
    qsna=df.shape[0]-qna
    
    ppna=round(100*(qna/df.shape[0]),2)
    aux= {'datos sin NAs en q': qsna, 'Na en q': qna ,'Na en %': ppna}
    na=pd.DataFrame(data=aux)
    resumen_nulos =na.sort_values(by='Na en %',ascending=False)
    return resumen_nulos
