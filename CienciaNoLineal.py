#Gestion de modelo
#===========================================================================
import pickle

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np

# Preprocesado y modelado
# ==============================================================================
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from scipy import stats
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')



# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
def Graficar_Distribucion(datos):
    filas=int(len(datos.select_dtypes(include=['float64', 'int','int64']).columns)/2)
    fig, axes = plt.subplots(nrows=filas, ncols=2, figsize=(9, 10))
    axes = axes.flat
    columnas_numeric = datos.select_dtypes(include=['float64', 'int','int64']).columns

    for i, colum in enumerate(columnas_numeric):
        sns.histplot(
            data    = datos,
            x       = colum,
            stat    = "count",
            kde     = True,
            color   = (list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],
            line_kws= {'linewidth': 2},
            alpha   = 0.3,
            ax      = axes[i]
        )
        axes[i].set_title(colum, fontsize = 10, fontweight = "bold")
        axes[i].tick_params(labelsize = 8)
        axes[i].set_xlabel("")



    fig.tight_layout()
    plt.subplots_adjust(top = 0.9)
    fig.suptitle('Distribución variables numéricas', fontsize = 10, fontweight = "bold");


def graficar_correlacion(df):
    import matplotlib.pyplot as plt
    corr_matrix = df.select_dtypes(include=['float64', 'int','int64']).corr(method='pearson')
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))
    sns.heatmap(
        corr_matrix,
        annot     = True,
        cbar      = False,
        annot_kws = {"size": 8},
        vmin      = -1,
        vmax      = 1,
        center    = 0,
        cmap      = sns.diverging_palette(20, 220, n=200),
        square    = True,
        ax        = ax
    )

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation = 45,
        horizontalalignment = 'right',
    )

    ax.tick_params(labelsize = 10)
    
    
def ver_correlacion(df):
    '''
    Función para convertir una matriz de correlación de pandas en formato tidy
    '''
    corr_mat = df.select_dtypes(include=['float64', 'int','int64']).corr(method='pearson')
    corr_mat = corr_mat.stack().reset_index()
    corr_mat.columns = ['variable_1','variable_2','r']
    corr_mat = corr_mat.loc[corr_mat['variable_1'] != corr_mat['variable_2'], :]
    corr_mat['abs_r'] = np.abs(corr_mat['r'])
    corr_mat = corr_mat.sort_values('abs_r', ascending=False)
    
    return(corr_mat)
    
    
from scipy.optimize import curve_fit



######## Funcion para aplicar Un modelo No lineal df= Dataframe a analizar;columnX=Nombre dela columna eje X;columnY=nombre de la columna eje Y
########funcion("sigmoide","logaritmica","cuadratrica")
########Entrega Grafica de el modelo y  entrega evaluzacion del Modelo 
def AplicarModeloNolineal(df,columnX,columnY,funcion):
    x_data, y_data = (df["%s"%columnX].values, df["%s"%columnY].values)

    

    def sigmoid(x, Beta_1, Beta_2):
        y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
        return y
    def  expone(x, a, c, d):
        y=a*np.exp(-c*x)+d
        return y
    
    def  logaritmic(x, a, d):
        y=a*np.log(x)+d
        return y
    
    # Normalicemos nuestros datos
    xdata =x_data/max(x_data)
    ydata =y_data/max(y_data)

    # divide los datos en entrenamiento y prueba
    msk = np.random.rand(len(df)) < 0.8
    train_x = xdata[msk]
    test_x = xdata[~msk]
    train_y = ydata[msk]
    test_y = ydata[~msk]
    if(funcion=="sigmoide"):
        print("Funcion Sigmoide Seleccionada")
        X = np.arange(-5.0, 5.0, 0.1)
        Y = 1.0 / (1.0 + np.exp(-X))

        plt.plot(X,Y) 
        plt.ylabel('Variable Dependiente')
        plt.xlabel('Variable Independiente')
        plt.show()
        # construye el modelo utilizando el set de entrenamiento
        popt, pcov = curve_fit(sigmoid, train_x, train_y)

        # predecir utilizando el set de prueba
        y_hat = sigmoid(test_x, *popt)
        y_grafico=sigmoid(xdata, *popt)
    if(funcion=="logaritmica"):
        print("Funcion Logaritmica Seleccionada")
        X = np.arange(-5.0, 5.0, 0.1)
        Y = np.log(X)
        plt.plot(X,Y) 
        plt.ylabel('Variable Dependiente')
        plt.xlabel('Variable Independiente')
        plt.show()
        popt, pcov = curve_fit(logaritmic, train_x, train_y )

        # predecir utilizando el set de prueba
        y_hat = logaritmic(test_x, *popt)
        y_grafico=logaritmic(xdata, *popt)
    if(funcion=="exponencial"):
        print("Funcion Exponencial Seleccionada")
        X = np.arange(-5.0, 5.0, 0.1)
        Y= np.exp(X)
        plt.plot(X,Y) 
        plt.ylabel('Variable Dependiente')
        plt.xlabel('Variable Independiente')
        plt.show()
        popt, pcov = curve_fit(expone, train_x, train_y )

        # predecir utilizando el set de prueba
        y_hat = expone(test_x, *popt)
        y_grafico=expone(xdata, *popt)
        
    
    # evaluation
    print("""  ___  ____    __    ____  ____   ___    __     ___  ____  _____  _  _ 
 / __)(  _ \  /__\  ( ___)(_  _) / __)  /__\   / __)(_  _)(  _  )( \( )
( (_-. )   / /(  )\  )__)  _)(_ ( (__  /(  )\ ( (__  _)(_  )(_)(  )  ( 
 \___/(_)\_)(__)(__)(_)   (____) \___)(__)(__) \___)(____)(_____)(_)\_)
""")

    print("Promedio de error absoluto: %.2f" % np.mean(np.absolute(y_hat - test_y)))
    print("Suma residual de cuadrados (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
    from sklearn.metrics import r2_score
    print("R2-score: %.2f" % r2_score(y_hat , test_y) )
    
    
    
    plt.plot(xdata, ydata, 'ro', label='data')
    plt.plot(xdata,y_grafico, linewidth=3.0, label='fit')
    plt.legend(loc='best')
    plt.ylabel("%s"%columnY)
    plt.xlabel("%s"%columnX)
    plt.show()
    # Diagnóstico de los resíduos
    # ==============================================================================
    
    print(""" ____   ____    __     ___  _  _  _____  ___  ____  ____   ___  _____ 
(  _ \ (_  _)  /__\   / __)( \( )(  _  )/ __)(_  _)(_  _) / __)(  _  )
 )(_) ) _)(_  /(  )\ ( (_-. )  (  )(_)( \__ \  )(   _)(_ ( (__  )(_)( 
(____/ (____)(__)(__) \___/(_)\_)(_____)(___/ (__) (____) \___)(_____)
""")
    y_train = y_data
    prediccion_train = y_grafico*max(y_data)
    residuos_train   = prediccion_train - y_train
    
    # Gráficos De Diagnosticos
    # ==============================================================================
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 8))

    axes[0, 0].scatter(y_train, prediccion_train, edgecolors=(0, 0, 0), alpha = 0.4)
    axes[0, 0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()],
                    'k--', color = 'black', lw=2)
    axes[0, 0].set_title('Valor predicho vs valor real', fontsize = 10, fontweight = "bold")
    axes[0, 0].set_xlabel('Real')
    axes[0, 0].set_ylabel('Predicción')
    axes[0, 0].tick_params(labelsize = 7)

    axes[0, 1].scatter(list(range(len(y_train))), residuos_train,
                       edgecolors=(0, 0, 0), alpha = 0.4)
    axes[0, 1].axhline(y = 0, linestyle = '--', color = 'black', lw=2)
    axes[0, 1].set_title('Residuos del modelo', fontsize = 10, fontweight = "bold")
    axes[0, 1].set_xlabel('id')
    axes[0, 1].set_ylabel('Residuo')
    axes[0, 1].tick_params(labelsize = 7)

    sns.histplot(
        data    = residuos_train,
        stat    = "density",
        kde     = True,
        line_kws= {'linewidth': 1},
        color   = "firebrick",
        alpha   = 0.3,
        ax      = axes[1, 0]
    )

    axes[1, 0].set_title('Distribución residuos del modelo', fontsize = 10,
                         fontweight = "bold")
    axes[1, 0].set_xlabel("Residuo")
    axes[1, 0].tick_params(labelsize = 7)


    sm.qqplot(
        residuos_train,
        fit   = True,
        line  = 'q',
        ax    = axes[1, 1], 
        color = 'firebrick',
        alpha = 0.4,
        lw    = 2
    )
    axes[1, 1].set_title('Q-Q residuos del modelo', fontsize = 10, fontweight = "bold")
    axes[1, 1].tick_params(labelsize = 7)

    axes[2, 0].scatter(prediccion_train, residuos_train,
                       edgecolors=(0, 0, 0), alpha = 0.4)
    axes[2, 0].axhline(y = 0, linestyle = '--', color = 'black', lw=2)
    axes[2, 0].set_title('Residuos del modelo vs predicción', fontsize = 10, fontweight = "bold")
    axes[2, 0].set_xlabel('Predicción')
    axes[2, 0].set_ylabel('Residuo')
    axes[2, 0].tick_params(labelsize = 7)

    # Se eliminan los axes vacíos
    fig.delaxes(axes[2,1])

    fig.tight_layout()
    plt.subplots_adjust(top=0.9)
    fig.suptitle('Diagnóstico residuos', fontsize = 12, fontweight = "bold");
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return [popt,max(x_data),max(y_data),funcion]

def PredecirConModeloNolineal(df,columnX,popt,mx,my,funcion):
    x_data = df["%s"%columnX].values
    xdata =x_data/mx
    

    def sigmoid(x, Beta_1, Beta_2):
        y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
        return y
    def  expone(x, a, c, d):
        y=a*np.exp(-c*x)+d
        return y
    
    def  logaritmic(x, a, d):
        y=a*np.log(x)+d
        return y
    
    if(funcion=="exponencial"):
        y_grafico=my*expone(xdata, *popt)
    if(funcion=="logaritmica"):
        y_grafico=my*logaritmic(xdata, *popt)
    if(funcion=="sigmoide"):
        y_grafico=my*sigmoid(xdata, *popt)
        
    
    plt.plot(x_data,y_grafico, linewidth=3.0, label='fit')
    plt.legend(loc='best')
    plt.ylabel("Prediccion")
    plt.xlabel("%s"%columnX)
    plt.show()
    return pd.DataFrame({"%s"%columnX:x_data,"prediccion":y_grafico})
        
     
def MiMejorVecino(datos,etiqueta,Ks):
    columnas=datos.select_dtypes(include=['float64', 'int','int64']).columns.values
    print("columnas Usadasparael modelo :%s"%columnas)
    print("columnas etiqueta modelo :%s"%etiqueta)
    XDatos=datos[columnas]
    Y_etiqueta=datos[etiqueta].values
    ###################################################################################
    XDatos = preprocessing.StandardScaler().fit(XDatos).transform(XDatos.astype(float))
    #############################################################################################
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( XDatos, Y_etiqueta, test_size=0.2, random_state=4)
    print ('Set de Entrenamiento:', X_train.shape,  y_train.shape)
    print ('Set de Prueba:', X_test.shape,  y_test.shape)
    
    ############################################################################
    mean_acc = np.zeros((Ks-1))
    std_acc = np.zeros((Ks-1))
    ConfustionMx = [];
    for n in range(1,Ks):

        #Entrenar el Modelo y Predecir  
        neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
        yhat=neigh.predict(X_test)
        mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)


        std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])
    ##########################################################################333
    plt.plot(range(1,Ks),mean_acc,'g')
    plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
    plt.legend(('Certeza ', '+/- 3xstd'))
    plt.ylabel('Certeza ')
    plt.xlabel('Número de Vecinos (K)')
    plt.tight_layout()
    plt.show()
    ##########################################################################
    print( "La mejor aproximación de certeza fue con ", mean_acc.max(), "con k=", mean_acc.argmax()+1)

    ##############################################################################
    k=mean_acc.argmax()+1
    neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
    #############################################################################
    yhat = neigh.predict(X_test)
    #########################################################################
    
    print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
    print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, yhat))
    with open('mimejorvecino.pkl', 'wb') as model_file:
        pickle.dump(neigh, model_file)
    return neigh
        
        
def UsarModeloMiMejorVecino(RutadelModelo,df):
    columnas=df.select_dtypes(include=['float64', 'int','int64']).columns.values
    XDatos=df[columnas]
    XDatos = preprocessing.StandardScaler().fit(XDatos).transform(XDatos.astype(float))
    with open(RutadelModelo, 'rb') as model_file:
        ModeloLeido = pickle.load(model_file)
        PrediccionLeido=ModeloLeido.predict(XDatos)
        print('parametros del modelo:')
        print(ModeloLeido.get_params(deep=True))
    return pd.concat([df,pd.DataFrame({"Prediccion":PrediccionLeido})],axis=1)
