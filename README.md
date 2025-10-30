# 🤖 Clasificación Automática con LLMs

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema completo para clasificación automática de **textos** e **imágenes** utilizando modelos de lenguaje grandes (LLMs):

- **OpenAI GPT-4o-mini** - Para clasificación de texto
- **Ollama** con modelos de visión - Para clasificación de imágenes

## 📋 Características

- ✅ Clasificación de texto con OpenAI
- ✅ Clasificación de imágenes con Ollama (modelos locales)
- ✅ Procesamiento por lotes de directorios completos
- ✅ Soporte para múltiples formatos de imagen
- ✅ Sistema de verificación automática
- ✅ Ejemplos interactivos incluidos
- ✅ Documentación completa

## 🚀 Inicio Rápido

### 1. Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/clasificacion-llms.git
cd clasificacion-llms

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configuración

**Para clasificación de texto (OpenAI):**
```bash
# Copiar plantilla de configuración
cp .env.example .env

# Editar .env y añadir tu API key de OpenAI
# OPENAI_API_KEY=tu-api-key-aqui
```

Obtén tu API key en: https://platform.openai.com/api-keys

**Para clasificación de imágenes (Ollama):**
```bash
# Instalar Ollama (visita https://ollama.ai para instrucciones)

# Iniciar servidor
ollama serve

# Instalar modelo de visión (en otra terminal)
ollama pull gemma3:27b-it-qat
```

### 3. Verificar Instalación

```bash
python check_installation.py
```

Este script verifica:
- ✅ Versión de Python
- ✅ Dependencias instaladas
- ✅ Configuración de APIs
- ✅ Servidor Ollama (si aplica)

## � Uso

### Clasificación de Texto con GPT-4o-mini

1. Asegúrate de tener el archivo `prompt_18.txt` en el directorio
2. Configura tu API key de OpenAI
3. Ejecuta el script:
   ```bash
   python classify_with_gpt.py
   ```

El script cargará el dataset, clasificará las frases y generará métricas de evaluación.

### Clasificación de Imágenes con Ollama

#### Opción 1: Uso Interactivo
```bash
python classify_images_with_ollama.py
```

El script te guiará para:
- Verificar la conexión con Ollama
- Seleccionar un directorio con imágenes
- Procesar todas las imágenes del directorio

#### Opción 2: Uso Programático

```python
from classify_images_with_ollama import OllamaImageClassifier

# Crear clasificador
classifier = OllamaImageClassifier(
    model_name="gemma3:27b-it-qat",
    ollama_url="http://localhost:11434"
)

# Verificar conexión
if classifier.check_connection():
    
    # Clasificar una sola imagen desde archivo local
    prompt = """Describe this image in detail, identifying the main subject, 
    setting, and notable features."""
    
    result = classifier.classify_single_image(
        image_source="path/to/image.jpg",
        prompt=prompt,
        is_url=False
    )
    print(result)
    
    # Procesar un directorio completo
    results = classifier.process_directory(
        directory_path="images_folder",
        prompt=prompt,
        output_file="results.json"
    )
```

#### Opción 3: Clasificar desde URL

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()

# Clasificar imagen desde URL
result = classifier.classify_single_image(
    image_source="https://example.com/image.jpg",
    prompt="Describe this image",
    is_url=True
)
```

## 📊 Resultados

### Clasificación de Texto
El script genera:
- Precisión, recall, F1-score
- Matriz de confusión
- Reporte de clasificación detallado
- Archivo CSV con resultados

### Clasificación de Imágenes
El script genera:
- Archivo JSON con resultados de cada imagen
- Resumen en consola con estadísticas
- Timestamp de procesamiento
- Manejo de errores por imagen

Ejemplo de salida JSON:
```json
[
    {
        "file": "image1.jpg",
        "path": "/full/path/to/image1.jpg",
        "classification": "Detailed description...",
        "error": null,
        "timestamp": "2025-10-30 14:32:15"
    }
]
```

## 🎯 Personalización de Prompts

### Para Imágenes

Puedes crear prompts personalizados según tu necesidad:

```python
# Prompt para clasificación de objetos
object_prompt = """Identify all objects in this image.
List them in order of prominence.
For each object, provide:
- Name
- Location in image
- Estimated size relative to image
- Color

Respond in JSON format."""

# Prompt para análisis de sentimiento visual
sentiment_prompt = """Analyze the emotional tone of this image.
Consider:
- Facial expressions (if any)
- Color palette
- Composition
- Lighting

Rate the emotional valence from 1-10 (1=negative, 10=positive)
and arousal from 1-10 (1=calm, 10=exciting).

Respond in JSON format with: valence, arousal, description"""
```

Consulta [ADVANCED_PROMPTS.md](ADVANCED_PROMPTS.md) para más ejemplos especializados.

## 🔄 Procesamiento por Lotes

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()
directories = ["dir1", "dir2", "dir3"]
prompt = "Describe this image briefly"

for dir_path in directories:
    results = classifier.process_directory(
        directory_path=dir_path,
        prompt=prompt,
        output_file=f"{dir_path}_results.json"
    )
```

## 🛠️ Solución de Problemas

| Problema | Solución |
|----------|----------|
| **Ollama no conecta** | Ejecuta `ollama serve` y verifica con `ollama list` |
| **Modelo no encontrado** | Instala el modelo: `ollama pull gemma3:27b-it-qat` |
| **Error de memoria** | Las imágenes se optimizan automáticamente. Reduce el tamaño si persiste |
| **OpenAI timeout** | Verifica tu conexión e API key. Hay 3 reintentos automáticos |
| **Dependencias faltantes** | Ejecuta `python check_installation.py` para diagnóstico |

## � Documentación Adicional

- **[QUICKSTART.md](QUICKSTART.md)** - Guía de inicio rápido en 3 pasos
- **[ADVANCED_PROMPTS.md](ADVANCED_PROMPTS.md)** - 15+ ejemplos de prompts especializados
- **[check_installation.py](check_installation.py)** - Script de verificación del sistema
- **[example_usage.py](example_usage.py)** - Ejemplos interactivos

## 🔒 Seguridad

- ⚠️ **Nunca subas tu `.env` con API keys al repositorio**
- ✅ Usa `.env.example` como plantilla
- ✅ Las API keys deben estar en variables de entorno
- ✅ Revisa el `.gitignore` antes de hacer commit

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## � Agradecimientos

- [Ollama](https://ollama.ai) por proporcionar modelos de visión locales
- [OpenAI](https://openai.com) por su API de clasificación de texto
- Comunidad open source por las herramientas y librerías

## 📞 Soporte

- 🐛 **Issues**: [GitHub Issues](https://github.com/tu-usuario/clasificacion-llms/issues)
- 📖 **Documentación**: Ver archivos `.md` en el repositorio
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/tu-usuario/clasificacion-llms/discussions)
