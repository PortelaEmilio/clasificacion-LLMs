# Guía Rápida: Clasificación de Imágenes y Textos

## 🚀 Inicio Rápido en 3 Pasos

### Para Clasificación de Imágenes

1. **Instalar Ollama**
   ```bash
   # Visita https://ollama.ai e instala según tu sistema operativo
   ```

2. **Iniciar Ollama e instalar modelo**
   ```bash
   # Terminal 1: Iniciar servidor
   ollama serve
   
   # Terminal 2: Instalar modelo
   ollama pull gemma3:27b-it-qat
   ```

3. **Ejecutar el ejemplo**
   ```bash
   python classify_images_with_ollama.py
   ```

### Para Clasificación de Texto

1. **Obtener API key de OpenAI**
   - Visita https://platform.openai.com/api-keys
   - Crea una nueva API key

2. **Configurar variable de entorno**
   ```bash
   export OPENAI_API_KEY='sk-...'
   ```

3. **Ejecutar el script**
   ```bash
   python classify_with_gpt.py
   ```

## 📝 Casos de Uso Comunes

### Caso 1: Clasificar todas las imágenes de una carpeta

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()

prompt = "Describe esta imagen brevemente"

results = classifier.process_directory(
    directory_path="mis_imagenes",
    prompt=prompt,
    output_file="resultados.json"
)
```

### Caso 2: Clasificar una imagen específica

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()

result = classifier.classify_single_image(
    image_source="foto.jpg",
    prompt="¿Qué objetos aparecen en esta imagen?",
    is_url=False
)

print(result)
```

### Caso 3: Clasificar imagen desde URL

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()

result = classifier.classify_single_image(
    image_source="https://example.com/imagen.jpg",
    prompt="Analiza el contenido de esta imagen",
    is_url=True
)

print(result)
```

### Caso 4: Personalizar el modelo y URL de Ollama

```python
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier(
    model_name="llava:latest",  # Usar otro modelo
    ollama_url="http://192.168.1.100:11434"  # Ollama en otra máquina
)

# Usar el clasificador normalmente
```

## 🎨 Ejemplos de Prompts para Imágenes

### Descripción General
```python
prompt = """Describe esta imagen en detalle, incluyendo:
- Sujeto principal
- Entorno y contexto
- Colores predominantes
- Emociones o atmósfera que transmite"""
```

### Clasificación de Objetos
```python
prompt = """Lista todos los objetos visibles en esta imagen.
Para cada objeto indica:
- Nombre del objeto
- Ubicación aproximada (izquierda, derecha, centro, arriba, abajo)
- Tamaño relativo (pequeño, mediano, grande)

Responde en formato JSON."""
```

### Análisis de Escenas
```python
prompt = """Analiza esta escena e identifica:
1. ¿Es interior o exterior?
2. ¿Qué hora del día parece ser?
3. ¿Hay personas presentes?
4. ¿Cuál es el estado emocional general de la escena?
5. ¿Qué actividad se está realizando (si alguna)?

Responde cada pregunta brevemente."""
```

### Detección de Texto
```python
prompt = """¿Hay texto visible en esta imagen?
Si es así:
- Transcribe todo el texto que veas
- Indica el idioma
- Describe dónde está ubicado el texto
- Indica si el texto es parte de un cartel, letrero, documento, etc."""
```

### Análisis de Estilo
```python
prompt = """Analiza el estilo visual de esta imagen:
- Estilo fotográfico (retrato, paisaje, macro, etc.)
- Técnica utilizada (fotografía, ilustración, 3D, etc.)
- Iluminación (natural, artificial, dramatic, soft)
- Composición (regla de tercios, centrado, diagonal, etc.)
- Tratamiento de color (vibrante, monocromático, pastel, etc.)"""
```

## ⚡ Consejos de Rendimiento

1. **Procesamiento por lotes**: Usa `process_directory()` en lugar de múltiples llamadas a `classify_single_image()`

2. **Tamaño de imágenes**: Las imágenes se convierten automáticamente a JPEG, lo que reduce el uso de memoria

3. **Timeout**: El timeout por defecto es 120 segundos. Ajústalo si necesitas más tiempo:
   ```python
   # Modifica el timeout en la función classify_image
   ```

4. **Reintentos**: Por defecto hay 3 reintentos automáticos en caso de error

5. **Memoria**: El script limpia automáticamente la memoria después de cada imagen

## 🐛 Solución de Problemas Comunes

### "No se puede conectar con Ollama"
- Verifica que el servidor esté corriendo: `ps aux | grep ollama`
- Reinicia el servidor: `killall ollama && ollama serve`

### "Modelo no encontrado"
- Lista modelos instalados: `ollama list`
- Instala el modelo: `ollama pull gemma3:27b-it-qat`

### "Timeout al procesar imagen"
- La imagen puede ser muy grande
- El modelo puede estar ocupado con otra tarea
- Reinicia Ollama

### "Error de memoria"
- Cierra otras aplicaciones que usen mucha RAM
- Procesa menos imágenes a la vez
- Reduce el tamaño de las imágenes antes de procesarlas

## 📚 Recursos Adicionales

- [Documentación completa](README.md)
- [Ejemplos interactivos](example_usage.py)
- [Documentación de Ollama](https://ollama.ai/docs)
- [Modelos disponibles](https://ollama.ai/library)

## 💡 Próximos Pasos

1. Lee el [README.md](README.md) completo para más detalles
2. Ejecuta `python example_usage.py` para ver ejemplos interactivos
3. Experimenta con diferentes prompts y modelos
4. Adapta los scripts a tus necesidades específicas
