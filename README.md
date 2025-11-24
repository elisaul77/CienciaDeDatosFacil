# CienciaDeDatosFacil 📊

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsors-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/elisaul77)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=for-the-badge&logo=paypal)](https://paypal.me/eflorezp)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?style=for-the-badge&logo=buymeacoffee)](https://buymeacoffee.com/elisaul77)

**Librería Python para hacer mucho más fácil la ciencia de datos**

CienciaDeDatosFacil es una biblioteca de Python que simplifica el análisis de datos y modelado estadístico, proporcionando funciones de alto nivel para visualización, análisis de correlaciones, modelos no lineales y clasificación con K-Nearest Neighbors.

## ✨ Características Principales

- 📊 **Visualización de Datos**: Gráficos de distribución y matrices de correlación
- 🔍 **Análisis de Correlaciones**: Identificación automática de relaciones entre variables
- 📈 **Modelos No Lineales**: Ajuste de modelos sigmoides, logarítmicos y exponenciales
- 🎯 **Clasificación K-NN**: Implementación simplificada de K-Nearest Neighbors
- 🧪 **Diagnóstico de Modelos**: Análisis automático de residuos y validación
- 💾 **Persistencia de Modelos**: Guardado y carga de modelos entrenados

## 🚀 Instalación

### Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels
```

### Uso de la Biblioteca

Simplemente descarga `CienciaNoLineal.py` y colócalo en tu proyecto:

```python
from CienciaNoLineal import *
```

## 📖 Guía de Uso

### 1. Visualización de Distribuciones

Genera gráficos de distribución para todas las variables numéricas de tu dataset:

```python
import pandas as pd
from CienciaNoLineal import Graficar_Distribucion

# Cargar tus datos
df = pd.read_csv('tu_archivo.csv')

# Visualizar distribuciones
Graficar_Distribucion(df)
```

### 2. Análisis de Correlaciones

#### Visualización de Matriz de Correlación

```python
from CienciaNoLineal import graficar_correlacion

# Mostrar heatmap de correlaciones
graficar_correlacion(df)
```

#### Obtener Correlaciones Ordenadas

```python
from CienciaNoLineal import ver_correlacion

# Obtener tabla de correlaciones ordenadas por magnitud
correlaciones = ver_correlacion(df)
print(correlaciones.head())
```

### 3. Modelos No Lineales

Aplica modelos no lineales (sigmoide, logarítmico, exponencial) a tus datos:

```python
from CienciaNoLineal import AplicarModeloNolineal

# Ajustar un modelo sigmoide
AplicarModeloNolineal(
    df=df,
    columnX='variable_independiente',
    columnY='variable_dependiente',
    funcion='sigmoide'  # Opciones: 'sigmoide', 'logaritmica', 'exponencial'
)
```

Esta función:
- Divide automáticamente los datos en entrenamiento (80%) y prueba (20%)
- Ajusta el modelo seleccionado
- Muestra gráficos de ajuste
- Genera diagnósticos completos de residuos
- Calcula métricas de error (MSE, R²)

#### Realizar Predicciones

```python
from CienciaNoLineal import PredecirConModeloNolineal

# Usar modelo entrenado para predicciones
predicciones = PredecirConModeloNolineal(
    df=nuevos_datos,
    columnX='variable_independiente',
    popt=parametros_optimizados,  # De AplicarModeloNolineal
    mx=max_x,                      # Valor máximo de X del entrenamiento
    my=max_y,                      # Valor máximo de Y del entrenamiento
    funcion='sigmoide'
)
```

### 4. Clasificación K-Nearest Neighbors

#### Entrenar y Evaluar Modelo K-NN

```python
from CienciaNoLineal import MiMejorVecino

# Encontrar el mejor valor de K y entrenar modelo
modelo = MiMejorVecino(
    datos=df,
    etiqueta='columna_objetivo',  # Variable a predecir
    Ks=30  # Probar valores de K de 1 a 30
)
```

Esta función:
- Prueba diferentes valores de K (1 a Ks)
- Calcula la precisión para cada K
- Guarda automáticamente el mejor modelo en `MejorModelo.pkl`
- Muestra gráfico de precisión vs K

#### Usar Modelo K-NN Guardado

```python
from CienciaNoLineal import UsarModeloMiMejorVecino

# Cargar modelo y hacer predicciones
UsarModeloMiMejorVecino(
    RutadelModelo='MejorModelo.pkl',
    df=nuevos_datos
)
```

## 📊 Ejemplos Completos

### Ejemplo 1: Análisis Exploratorio Completo

```python
import pandas as pd
from CienciaNoLineal import *

# Cargar datos
df = pd.read_csv('datos.csv')

# 1. Visualizar distribuciones
Graficar_Distribucion(df)

# 2. Analizar correlaciones
graficar_correlacion(df)
correlaciones = ver_correlacion(df)
print("Top 5 correlaciones:")
print(correlaciones.head())

# 3. Modelar relación no lineal
AplicarModeloNolineal(
    df=df,
    columnX='edad',
    columnY='salario',
    funcion='logaritmica'
)
```

### Ejemplo 2: Pipeline de Clasificación

```python
import pandas as pd
from CienciaNoLineal import *

# Cargar datos de entrenamiento
df_train = pd.read_csv('datos_entrenamiento.csv')

# Entrenar y guardar mejor modelo
modelo = MiMejorVecino(
    datos=df_train,
    etiqueta='categoria',
    Ks=20
)

# Cargar datos nuevos
df_test = pd.read_csv('datos_prueba.csv')

# Hacer predicciones
UsarModeloMiMejorVecino(
    RutadelModelo='MejorModelo.pkl',
    df=df_test
)
```

## 🛠️ Funciones Disponibles

| Función | Descripción |
|---------|-------------|
| `Graficar_Distribucion(datos)` | Genera histogramas con KDE para variables numéricas |
| `graficar_correlacion(df)` | Muestra heatmap de correlaciones de Pearson |
| `ver_correlacion(df)` | Retorna DataFrame con correlaciones ordenadas |
| `AplicarModeloNolineal(df, columnX, columnY, funcion)` | Ajusta modelo no lineal y muestra diagnósticos |
| `PredecirConModeloNolineal(df, columnX, popt, mx, my, funcion)` | Realiza predicciones con modelo no lineal |
| `MiMejorVecino(datos, etiqueta, Ks)` | Entrena clasificador K-NN y encuentra mejor K |
| `UsarModeloMiMejorVecino(RutadelModelo, df)` | Carga modelo K-NN y hace predicciones |

## 📋 Modelos No Lineales Soportados

### Función Sigmoide
```python
y = 1 / (1 + exp(-β₁(x - β₂)))
```
**Uso**: Crecimiento con saturación, curvas S

### Función Logarítmica
```python
y = a * log(x) + d
```
**Uso**: Crecimiento que desacelera, rendimientos decrecientes

### Función Exponencial
```python
y = a * exp(-c * x) + d
```
**Uso**: Decaimiento exponencial, enfriamiento

## 🧪 Diagnósticos de Modelos

La función `AplicarModeloNolineal` genera automáticamente:

1. **Gráfico de Ajuste**: Comparación entre datos reales y predicciones
2. **Valor Predicho vs Valor Real**: Verificación de linealidad
3. **Residuos vs ID**: Detección de patrones
4. **Distribución de Residuos**: Verificación de normalidad (histograma + KDE)
5. **Gráfico Q-Q**: Prueba de normalidad de residuos
6. **Residuos vs Predicción**: Detección de heterocedasticidad
7. **Métricas**: MSE, RMSE, R² para train y test

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

### 💖 Apoya el Proyecto

Si CienciaDeDatosFacil te resulta útil, considera apoyar su desarrollo:

- ⭐ **Dale una estrella** al repositorio
- 💰 **[Haz una donación](FUNDING.md)** para apoyar el desarrollo continuo
- 🐛 **Reporta bugs** y sugiere mejoras
- 📝 **Contribuye con código** o documentación
- 📢 **Comparte** el proyecto con otros data scientists

[![GitHub Sponsors](https://img.shields.io/badge/❤️%20Sponsor-GitHub-pink)](https://github.com/sponsors/elisaul77)
[![PayPal](https://img.shields.io/badge/💰%20Donate-PayPal-blue)](https://paypal.me/eflorezp)

Ver todas las opciones de donación en **[FUNDING.md](FUNDING.md)**

## 📚 Recursos Adicionales

- **Pandas**: [Documentación oficial](https://pandas.pydata.org/)
- **Scikit-learn**: [Guía de usuario](https://scikit-learn.org/stable/user_guide.html)
- **Matplotlib**: [Tutoriales](https://matplotlib.org/stable/tutorials/index.html)
- **Seaborn**: [Galería de ejemplos](https://seaborn.pydata.org/examples/index.html)

## 📞 Soporte y Contacto

- **Issues**: [Reportar problemas en GitHub](https://github.com/elisaul77/CienciaDeDatosFacil/issues)
- **Email**: elisaul77@gmail.com
- **Discusiones**: [GitHub Discussions](https://github.com/elisaul77/CienciaDeDatosFacil/discussions)

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia GPL v3.0 - ver el archivo [LICENSE](LICENSE) para más detalles.

---

**¡Hecho con ❤️ para la comunidad de Data Science!** 🚀

Si este proyecto te ayuda, considera [apoyar el desarrollo](FUNDING.md) ☕
