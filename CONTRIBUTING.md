# 🤝 Guía de Contribución a CienciaDeDatosFacil

¡Gracias por tu interés en contribuir a CienciaDeDatosFacil! Este documento proporciona pautas y buenas prácticas para contribuir al proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Puedo Contribuir](#cómo-puedo-contribuir)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Proceso de Contribución](#proceso-de-contribución)
- [Guía de Estilo](#guía-de-estilo)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Mejoras](#sugerir-mejoras)

## 📜 Código de Conducta

Este proyecto y todos sus participantes se rigen por un código de conducta. Al participar, se espera que respetes este código. Comportamiento inaceptable puede ser reportado a elisaul77@gmail.com.

### Nuestros Estándares

- ✅ Usar lenguaje acogedor e inclusivo
- ✅ Respetar diferentes puntos de vista y experiencias
- ✅ Aceptar críticas constructivas con gracia
- ✅ Enfocarse en lo que es mejor para la comunidad
- ✅ Mostrar empatía hacia otros miembros de la comunidad

## 🎯 Cómo Puedo Contribuir

Hay muchas formas de contribuir a CienciaDeDatosFacil:

### 1. 🐛 Reportar Bugs

Los bugs se rastrean como [GitHub Issues](https://github.com/elisaul77/CienciaDeDatosFacil/issues). Antes de crear un issue:

- **Verifica** que el bug no haya sido reportado anteriormente
- **Proporciona** información detallada sobre cómo reproducir el problema
- **Incluye** información del sistema (Python version, OS, etc.)

### 2. 💡 Sugerir Mejoras

Las sugerencias de mejoras también se manejan como GitHub Issues. Para sugerir una mejora:

- **Describe** claramente la funcionalidad propuesta
- **Explica** por qué sería útil para la comunidad
- **Proporciona** ejemplos de uso si es posible

### 3. 📝 Mejorar Documentación

- Corrige errores tipográficos
- Mejora explicaciones confusas
- Añade ejemplos de uso
- Traduce documentación

### 4. 💻 Contribuir con Código

- Implementa nuevos algoritmos
- Optimiza código existente
- Añade tests
- Corrige bugs

## 🛠️ Configuración del Entorno de Desarrollo

### Requisitos

- Python 3.9 o superior
- Git
- Editor de código (recomendado: VS Code, PyCharm)

### Instalación

1. **Fork el repositorio**
   ```bash
   # Haz clic en "Fork" en GitHub
   ```

2. **Clona tu fork**
   ```bash
   git clone https://github.com/TU-USUARIO/CienciaDeDatosFacil.git
   cd CienciaDeDatosFacil
   ```

3. **Configura el upstream**
   ```bash
   git remote add upstream https://github.com/elisaul77/CienciaDeDatosFacil.git
   ```

4. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

5. **Instala dependencias**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels
   pip install pytest black flake8  # Herramientas de desarrollo
   ```

## 🔄 Proceso de Contribución

### 1. Crear una Rama

```bash
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

Nomenclatura de ramas:
- `feature/` - Nueva funcionalidad
- `fix/` - Corrección de bug
- `docs/` - Cambios en documentación
- `refactor/` - Refactorización de código
- `test/` - Añadir o modificar tests

### 2. Hacer Cambios

- Escribe código claro y bien comentado
- Sigue la guía de estilo de Python (PEP 8)
- Añade docstrings a funciones nuevas
- Asegúrate de que el código funcione

### 3. Probar tus Cambios

```python
# Prueba tu función manualmente
import pandas as pd
from CienciaNoLineal import tu_nueva_funcion

# Crea datos de prueba
df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 4, 6]})

# Prueba la función
resultado = tu_nueva_funcion(df)
print(resultado)
```

### 4. Formatear Código

```bash
# Formatear con black
black CienciaNoLineal.py

# Verificar con flake8
flake8 CienciaNoLineal.py --max-line-length=100
```

### 5. Commit tus Cambios

```bash
git add .
git commit -m "feat: añade función para análisis de componentes principales"
```

**Formato de mensajes de commit:**
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `docs:` - Cambios en documentación
- `style:` - Cambios de formato (no afectan código)
- `refactor:` - Refactorización
- `test:` - Añadir tests
- `chore:` - Mantenimiento

### 6. Push a tu Fork

```bash
git push origin feature/nueva-funcionalidad
```

### 7. Crear Pull Request

1. Ve a tu fork en GitHub
2. Haz clic en "Pull Request"
3. Describe tus cambios detalladamente
4. Espera revisión y feedback

## 📝 Guía de Estilo

### Código Python

- **Sigue PEP 8**: El estándar de estilo de Python
- **Líneas de máximo 100 caracteres**
- **Usa snake_case** para nombres de funciones y variables
- **Usa docstrings** para documentar funciones

### Ejemplo de Función Bien Documentada

```python
def calcular_media_ponderada(valores, pesos):
    """
    Calcula la media ponderada de un conjunto de valores.
    
    Parameters
    ----------
    valores : array-like
        Array con los valores numéricos
    pesos : array-like
        Array con los pesos asociados a cada valor
    
    Returns
    -------
    float
        Media ponderada de los valores
    
    Examples
    --------
    >>> valores = [1, 2, 3, 4]
    >>> pesos = [0.1, 0.2, 0.3, 0.4]
    >>> calcular_media_ponderada(valores, pesos)
    3.0
    
    Raises
    ------
    ValueError
        Si las longitudes de valores y pesos no coinciden
    """
    if len(valores) != len(pesos):
        raise ValueError("valores y pesos deben tener la misma longitud")
    
    return np.average(valores, weights=pesos)
```

### Comentarios

- **Usa comentarios** para explicar "por qué", no "qué"
- **Evita comentarios obvios**
- **Documenta decisiones no triviales**

```python
# ❌ Mal: Comentario obvio
# Incrementa i en 1
i += 1

# ✅ Bien: Explica razonamiento
# Usamos logaritmo para estabilizar la varianza
y_transformed = np.log(y + 1)
```

### Nombres Descriptivos

```python
# ❌ Mal
def f(x, y):
    return x + y

# ✅ Bien
def calcular_suma_variables(primera_variable, segunda_variable):
    return primera_variable + segunda_variable
```

## 🐛 Reportar Bugs

### Antes de Reportar

1. **Verifica** la [lista de issues existentes](https://github.com/elisaul77/CienciaDeDatosFacil/issues)
2. **Asegúrate** de usar la versión más reciente
3. **Recopila** información sobre tu entorno

### Información a Incluir

Crea un issue con el siguiente template:

```markdown
## Descripción del Bug
[Descripción clara del problema]

## Para Reproducir
Pasos para reproducir el comportamiento:
1. Importar '...'
2. Llamar función con '...'
3. Ver error

## Comportamiento Esperado
[Qué esperabas que sucediera]

## Comportamiento Actual
[Qué sucedió realmente]

## Código para Reproducir
```python
# Tu código aquí
```

## Entorno
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python: [e.g., 3.9.7]
- Pandas: [e.g., 1.3.4]
- NumPy: [e.g., 1.21.4]

## Información Adicional
[Screenshots, logs, etc.]
```

## 💡 Sugerir Mejoras

### Template para Sugerencias

```markdown
## Funcionalidad Propuesta
[Descripción clara de la funcionalidad]

## Motivación
[Por qué sería útil esta funcionalidad]

## Ejemplo de Uso
```python
# Cómo se usaría la nueva función
resultado = nueva_funcion(datos)
```

## Alternativas Consideradas
[Otras formas de resolver el mismo problema]

## Contexto Adicional
[Información relevante, referencias, etc.]
```

## 🎓 Áreas de Contribución

### Alta Prioridad

- 🔴 **Nuevos Algoritmos**: SVM, Random Forest, Clustering
- 🔴 **Mejoras de Performance**: Optimización de código existente
- 🔴 **Tests Automatizados**: Suite completa de tests
- 🔴 **Documentación**: Tutoriales y ejemplos

### Media Prioridad

- 🟡 **Visualizaciones Avanzadas**: Gráficos interactivos
- 🟡 **Integración con Pandas**: Métodos de DataFrame
- 🟡 **Validación de Entrada**: Chequeos más robustos
- 🟡 **Ejemplos Avanzados**: Casos de uso complejos

### Baja Prioridad

- 🟢 **Traducción**: Documentación en otros idiomas
- 🟢 **Notebooks Jupyter**: Tutoriales interactivos
- 🟢 **Videos Tutoriales**: Contenido multimedia
- 🟢 **Blog Posts**: Artículos explicativos

## 🏆 Reconocimiento

Todos los contribuidores serán:
- ✅ Listados en el archivo [SPONSORS.md](SPONSORS.md)
- ✅ Mencionados en las release notes
- ✅ Reconocidos en la documentación

### Top Contributors

Los contribuidores más activos recibirán:
- 🌟 Badge especial en GitHub
- 📢 Mención en redes sociales
- 🎁 Swag del proyecto (cuando esté disponible)

## 📚 Recursos Útiles

### Python y Ciencia de Datos

- [PEP 8 - Guía de Estilo](https://pep8.org/)
- [NumPy Docs](https://numpy.org/doc/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Scikit-learn Docs](https://scikit-learn.org/)

### Git y GitHub

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Forking Projects](https://guides.github.com/activities/forking/)

## 💬 Comunidad

### Dónde Obtener Ayuda

- 📫 **Email**: elisaul77@gmail.com
- 💬 **GitHub Discussions**: [Discussions](https://github.com/elisaul77/CienciaDeDatosFacil/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/elisaul77/CienciaDeDatosFacil/issues)

### Reuniones de Comunidad

- 📅 Actualmente no hay reuniones programadas
- 📢 Anunciaremos cuando la comunidad crezca

## ❓ Preguntas Frecuentes

### ¿Necesito ser experto en Python?

No, ¡contribuidores de todos los niveles son bienvenidos! Empieza con tareas simples como mejorar documentación.

### ¿Cuánto tiempo toma revisar un PR?

Típicamente entre 2-7 días. Puedes acelerar el proceso:
- Siguiendo la guía de estilo
- Incluyendo tests
- Proporcionando descripción detallada

### ¿Puedo trabajar en múltiples issues?

Sí, pero recomendamos completar uno antes de empezar otro.

### ¿Qué pasa si mi PR es rechazado?

Recibirás feedback constructivo. Puedes hacer ajustes y volver a enviar.

## 🙏 Agradecimientos

Gracias a todos los que contribuyen a hacer CienciaDeDatosFacil mejor:
- 💻 Contribuidores de código
- 📝 Escritores de documentación
- 🐛 Reportadores de bugs
- 💡 Sugerentes de ideas
- ⭐ Usuarios que dan estrellas al proyecto

---

**¿Listo para contribuir?** 🚀

1. Fork el proyecto
2. Crea una rama
3. Haz tus cambios
4. Crea un Pull Request

**¡Esperamos tu contribución!** ❤️
