# Clasificación Automática con GPT-4o-mini via OpenAI API

Este repositorio contiene un script en Python para clasificar frases automáticamente utilizando el modelo GPT-4o-mini de OpenAI a través de su API.

## Descripción

El script `classify_with_gpt.py` realiza la clasificación de frases y evalúa el desempeño comparando con etiquetas correctas (_ME). Utiliza la biblioteca `openai` para interactuar con la API de OpenAI.

## Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `openai`, `scikit-learn`, `numpy`
- Archivo de prompt: `prompt_18.txt` (debe estar en el mismo directorio)
- Dataset de frases a clasificar (CSV con columna 'frase' y etiquetas _ME)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/clasificacion-openai.git
   cd clasificacion-openai
   ```

2. Instala las dependencias:
   ```bash
   pip install pandas openai scikit-learn numpy
   ```

3. Configura tu API key de OpenAI en el script (línea 16).

## Uso

1. Asegúrate de tener el archivo `prompt_18.txt` en el directorio.
2. Ejecuta el script:
   ```bash
   python classify_with_gpt.py
   ```

El script cargará el dataset, clasificará las frases y generará métricas de evaluación.

## Resultados

El script genera:
- Precisión, recall, F1-score
- Matriz de confusión
- Reporte de clasificación detallado
- Archivo CSV con resultados

## Notas de Seguridad

- La API key está hardcodeada en el script. En producción, usa variables de entorno.
- El script procesa frases que pueden contener información sensible.

## Licencia

[Especifica la licencia aquí]</content>
<parameter name="filePath">/home/emilio/Documentos/Master/TFM/Clasificacion_bio_simple/clasificacion-openai-repo/README.md