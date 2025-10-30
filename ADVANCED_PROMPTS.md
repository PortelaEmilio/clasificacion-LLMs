# Ejemplos Avanzados de Prompts

Esta guía contiene ejemplos de prompts especializados para diferentes casos de uso en clasificación de imágenes.

## 📊 Análisis de Datos Visuales

### Gráficos y Visualizaciones
```python
prompt = """Analiza este gráfico o visualización de datos.

1. Tipo de gráfico: (barra, línea, pastel, dispersión, etc.)
2. Título y etiquetas: ¿Qué información se está mostrando?
3. Datos principales: Resume los valores o tendencias clave
4. Conclusiones: ¿Qué historia cuenta este gráfico?

Responde en formato JSON:
{
    "tipo_grafico": "",
    "titulo": "",
    "eje_x": "",
    "eje_y": "",
    "tendencia_principal": "",
    "valores_destacados": [],
    "conclusion": ""
}"""
```

### Diagramas y Esquemas
```python
prompt = """Analiza este diagrama o esquema.

Identifica:
- Tipo de diagrama (flujo, UML, arquitectura, etc.)
- Componentes principales
- Relaciones entre componentes
- Flujo de información (si aplica)
- Propósito del diagrama

Proporciona una descripción estructurada."""
```

## 🏞️ Análisis de Escenas y Ambientes

### Fotografía de Paisajes
```python
prompt = """Analiza esta fotografía de paisaje.

Evalúa:
1. Ubicación geográfica probable (montaña, playa, bosque, etc.)
2. Condiciones climáticas
3. Hora del día aproximada
4. Estación del año
5. Elementos naturales prominentes
6. Presencia humana o infraestructura
7. Calidad fotográfica (composición, iluminación)

Formato JSON con cada aspecto."""
```

### Espacios Interiores
```python
prompt = """Describe este espacio interior.

Analiza:
- Tipo de espacio (sala, oficina, cocina, etc.)
- Estilo de decoración
- Iluminación (natural/artificial)
- Mobiliario y objetos principales
- Color scheme dominante
- Funcionalidad del espacio
- Estado de orden/limpieza

Proporciona una descripción detallada."""
```

## 👤 Análisis de Personas e Interacciones

### Expresiones Faciales
```python
prompt = """Analiza las expresiones faciales en esta imagen.

Para cada persona visible:
1. Emoción principal (felicidad, tristeza, sorpresa, etc.)
2. Intensidad emocional (1-10)
3. Gestos faciales específicos
4. Dirección de la mirada
5. Contexto de la expresión

⚠️ Si no hay personas, indica "No hay personas en la imagen"

Responde en JSON."""
```

### Lenguaje Corporal
```python
prompt = """Analiza el lenguaje corporal en esta imagen.

Para cada persona:
- Postura (erguida, relajada, tensa, etc.)
- Gestos con las manos
- Posición de brazos y piernas
- Interacción con otros (si hay más personas)
- Nivel de confianza aparente
- Estado emocional inferido

Formato JSON con detalles."""
```

## 🔍 Análisis Técnico

### Calidad de Imagen
```python
prompt = """Evalúa la calidad técnica de esta imagen.

Aspectos a analizar:
1. Resolución aparente (alta, media, baja)
2. Nitidez y enfoque
3. Ruido o grano
4. Exposición (sobre/sub expuesta)
5. Balance de blancos
6. Rango dinámico
7. Compresión visible
8. Artefactos o defectos

Puntúa cada aspecto de 1-10 y proporciona una evaluación general."""
```

### Metadatos Visuales
```python
prompt = """Infiere información sobre cómo se tomó esta foto.

Analiza e infiere:
- Tipo de cámara probable (smartphone, DSLR, profesional)
- Distancia focal aproximada
- Profundidad de campo
- Tipo de lente (gran angular, teleobjetivo, etc.)
- Uso de flash
- Condiciones de iluminación
- Post-procesamiento aplicado

Base tus inferencias en evidencia visual."""
```

## 🎨 Análisis Artístico y Creativo

### Estilo Artístico
```python
prompt = """Analiza el estilo artístico de esta imagen.

Identifica:
1. Movimiento artístico (realismo, surrealismo, abstracto, etc.)
2. Técnica utilizada (óleo, acuarela, digital, fotografía, etc.)
3. Paleta de colores
4. Composición y balance
5. Uso de luz y sombra
6. Influencias aparentes
7. Período histórico aproximado

Proporciona un análisis detallado en formato narrativo."""
```

### Diseño Gráfico
```python
prompt = """Evalúa este diseño gráfico desde una perspectiva profesional.

Analiza:
- Propósito del diseño (publicidad, editorial, web, etc.)
- Jerarquía visual
- Uso de tipografía
- Esquema de color y su efectividad
- Balance y espacio negativo
- Llamada a la acción (si aplica)
- Público objetivo aparente
- Efectividad general (1-10)

Formato JSON con justificaciones."""
```

## 🏢 Análisis de Documentos

### Documentos Escaneados
```python
prompt = """Analiza este documento escaneado.

Extrae:
1. Tipo de documento (carta, contrato, factura, etc.)
2. Idioma(s) presente(s)
3. Fecha (si es visible)
4. Remitente/Destinatario (si aplica)
5. Contenido principal (resumen)
6. Elementos estructurales (logo, firma, sello, etc.)
7. Calidad del escaneo

⚠️ No incluyas información personal específica, solo el tipo de información."""
```

### Capturas de Pantalla
```python
prompt = """Analiza esta captura de pantalla.

Identifica:
- Tipo de aplicación o sitio web
- Sistema operativo
- Elementos de interfaz visibles
- Funcionalidad principal mostrada
- Estado de la aplicación
- Idioma de la interfaz
- Diseño de UI/UX

Proporciona descripción estructurada."""
```

## 🛍️ Análisis Comercial

### Productos
```python
prompt = """Analiza este producto desde una perspectiva comercial.

Evalúa:
1. Categoría del producto
2. Marca (si es visible)
3. Estado (nuevo, usado)
4. Características visibles
5. Presentación y empaquetado
6. Público objetivo aparente
7. Rango de precio estimado
8. Puntos de venta destacados

Formato JSON."""
```

### Escaparates y Displays
```python
prompt = """Analiza esta exhibición comercial o escaparate.

Evalúa:
- Tipo de tienda o marca
- Productos en exhibición
- Estrategia de merchandising
- Uso de color y iluminación
- Mensaje de marketing
- Temporada o campaña
- Efectividad visual (1-10)
- Público objetivo

Proporciona análisis detallado."""
```

## 🔬 Análisis Especializado

### Imágenes Médicas (Uso Educativo)
```python
prompt = """⚠️ Solo para fines educativos y demostración.

Describe esta imagen de naturaleza médica o científica:

1. Tipo de imagen (rayos X, microscopio, etc.)
2. Estructura anatómica visible
3. Características destacadas
4. Contexto educativo

⚠️ NO proporciones diagnósticos médicos.
⚠️ Solo descripciones anatómicas generales."""
```

### Naturaleza y Vida Silvestre
```python
prompt = """Identifica y describe la vida silvestre en esta imagen.

Para cada organismo visible:
1. Tipo de organismo (mamífero, ave, insecto, planta, etc.)
2. Especie probable (si es identificable)
3. Comportamiento observado
4. Hábitat
5. Características distintivas
6. Contexto ecológico

Formato estructurado con nivel de confianza para identificaciones."""
```

## 🎯 Prompts Multi-Propósito

### Análisis Completo
```python
prompt = """Realiza un análisis exhaustivo de esta imagen.

Secciones:
1. DESCRIPCIÓN BÁSICA:
   - Qué es la imagen
   - Sujeto principal
   - Contexto

2. ANÁLISIS TÉCNICO:
   - Calidad
   - Composición
   - Iluminación

3. ANÁLISIS DE CONTENIDO:
   - Objetos/personas
   - Acciones/eventos
   - Emociones/atmósfera

4. INTERPRETACIÓN:
   - Mensaje o propósito
   - Audiencia target
   - Efectividad

5. METADATOS INFERIDOS:
   - Dónde fue tomada (tipo de lugar)
   - Cuándo (hora del día, época)
   - Cómo (dispositivo probable)

Proporciona respuesta JSON estructurada."""
```

## 💡 Consejos para Crear Prompts Efectivos

1. **Sé específico**: Define exactamente qué información necesitas
2. **Usa estructura**: Organiza el prompt con secciones numeradas o bullets
3. **Define el formato**: Especifica JSON, texto narrativo, bullets, etc.
4. **Da contexto**: Explica el propósito del análisis
5. **Incluye restricciones**: Menciona qué NO hacer si es relevante
6. **Solicita confianza**: Pide nivel de certeza en identificaciones
7. **Maneja errores**: Incluye instrucciones para casos edge (ej: "si no hay personas...")

## 🔄 Prompts Adaptables

### Template Genérico
```python
def crear_prompt_personalizado(
    objetivo: str,
    aspectos_analizar: list,
    formato_respuesta: str = "JSON"
) -> str:
    prompt = f"""Analiza esta imagen con el objetivo de: {objetivo}

Aspectos a analizar:
"""
    for i, aspecto in enumerate(aspectos_analizar, 1):
        prompt += f"{i}. {aspecto}\n"
    
    prompt += f"\nResponde en formato {formato_respuesta}."
    return prompt

# Uso:
prompt = crear_prompt_personalizado(
    objetivo="identificar elementos de seguridad",
    aspectos_analizar=[
        "Equipos de protección personal visibles",
        "Señalización de seguridad",
        "Condiciones de riesgo aparentes",
        "Cumplimiento de normativas (general)"
    ]
)
```

## 📚 Referencias

- Para más información sobre ingeniería de prompts: [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- Ejemplos de la comunidad: [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
- Documentación de Ollama: [Ollama Docs](https://ollama.ai/docs)
