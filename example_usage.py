#!/usr/bin/env python3
"""
Script de ejemplo que demuestra clasificación de textos e imágenes
Muestra ambos flujos de trabajo en un solo lugar
"""

import os
import json
from pathlib import Path

# Verificar si las dependencias están instaladas
try:
    from classify_images_with_ollama import OllamaImageClassifier
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    print("⚠️ Módulo de clasificación de imágenes no disponible")

print("="*70)
print("EJEMPLO: CLASIFICACIÓN DE TEXTOS E IMÁGENES CON LLMs")
print("="*70)


def ejemplo_clasificacion_texto():
    """
    Ejemplo de clasificación de texto con OpenAI
    """
    print("\n" + "="*70)
    print("📝 EJEMPLO 1: CLASIFICACIÓN DE TEXTO")
    print("="*70)
    
    # Verificar si tenemos la API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("\n⚠️ Para usar clasificación de texto con OpenAI:")
        print("   export OPENAI_API_KEY='tu-api-key-aqui'")
        print("\n💡 Ejemplo de uso con la API de OpenAI:")
        print("""
from openai import OpenAI

client = OpenAI(api_key='tu-api-key')

# Clasificar una frase
prompt = "Clasifica esta frase: 'Me encanta programar en Python'"
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": "Eres un clasificador de texto"},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
        """)
        return
    
    print("✅ API key de OpenAI configurada")
    print("💡 Ejecuta 'python classify_with_gpt.py' para clasificación completa")


def ejemplo_clasificacion_imagen():
    """
    Ejemplo de clasificación de imágenes con Ollama
    """
    print("\n" + "="*70)
    print("🖼️ EJEMPLO 2: CLASIFICACIÓN DE IMÁGENES")
    print("="*70)
    
    if not OLLAMA_AVAILABLE:
        print("\n❌ Módulo de clasificación de imágenes no disponible")
        print("💡 Asegúrate de que classify_images_with_ollama.py esté en el directorio")
        return
    
    # Crear clasificador
    classifier = OllamaImageClassifier()
    
    # Verificar conexión
    print("\n🔍 Verificando conexión con Ollama...")
    if not classifier.check_connection():
        print("\n❌ No se puede conectar con Ollama")
        print("\n💡 Para usar clasificación de imágenes:")
        print("   1. Instala Ollama: https://ollama.ai")
        print("   2. Inicia el servidor: ollama serve")
        print("   3. Instala un modelo: ollama pull gemma3:27b-it-qat")
        return
    
    print("\n✅ Conexión con Ollama exitosa")
    
    # Crear directorio de ejemplo si no existe
    example_dir = Path("images_example")
    if not example_dir.exists():
        example_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n📁 Directorio '{example_dir}' creado")
        print("💡 Coloca algunas imágenes en este directorio para probar la clasificación")
        
        # Crear un archivo de instrucciones
        instructions_file = example_dir / "README.txt"
        with open(instructions_file, 'w', encoding='utf-8') as f:
            f.write("""
INSTRUCCIONES PARA CLASIFICACIÓN DE IMÁGENES
==============================================

1. Coloca tus imágenes (JPG, PNG, etc.) en este directorio
2. Ejecuta: python example_usage.py
3. El script procesará todas las imágenes automáticamente

Formatos soportados: .jpg, .jpeg, .png, .webp, .bmp, .gif

Ejemplo de uso programático:
----------------------------
from classify_images_with_ollama import OllamaImageClassifier

classifier = OllamaImageClassifier()

# Clasificar una imagen
result = classifier.classify_single_image(
    image_source="path/to/image.jpg",
    prompt="Describe esta imagen en detalle",
    is_url=False
)

print(result)
""")
        print(f"✅ Instrucciones guardadas en '{instructions_file}'")
        return
    
    # Buscar imágenes en el directorio
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif'}
    images = [f for f in example_dir.iterdir() 
             if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not images:
        print(f"\n⚠️ No hay imágenes en '{example_dir}'")
        print("💡 Coloca algunas imágenes en el directorio y ejecuta el script nuevamente")
        return
    
    print(f"\n📸 Se encontraron {len(images)} imágenes")
    
    # Crear prompt de ejemplo
    prompt = """Analiza esta imagen y proporciona una descripción detallada.

Por favor identifica:
1. Tema o sujeto principal
2. Entorno o contexto
3. Colores predominantes
4. Características notables

Responde en formato JSON con la siguiente estructura:
{
    "tema_principal": "descripción",
    "entorno": "descripción",
    "colores": ["color1", "color2"],
    "caracteristicas": ["característica1", "característica2"],
    "descripcion_general": "resumen breve"
}"""
    
    print("\n🔄 Procesando imágenes...")
    print("⏳ Este proceso puede tomar varios minutos dependiendo del número de imágenes")
    
    # Procesar el directorio
    results = classifier.process_directory(
        directory_path=example_dir,
        prompt=prompt,
        output_file="example_image_results.json"
    )
    
    # Mostrar resumen
    print("\n" + "="*70)
    print("📊 RESUMEN DE CLASIFICACIÓN")
    print("="*70)
    print(f"Total de imágenes: {len(results)}")
    successful = sum(1 for r in results if r.get('error') is None)
    print(f"Clasificaciones exitosas: {successful}")
    print(f"Errores: {len(results) - successful}")
    
    if successful > 0:
        print("\n💡 Resultados guardados en 'example_image_results.json'")
        print("   Puedes abrir este archivo para ver las clasificaciones detalladas")


def ejemplo_clasificacion_imagen_url():
    """
    Ejemplo de clasificación de imagen desde URL
    """
    print("\n" + "="*70)
    print("🌐 EJEMPLO 3: CLASIFICACIÓN DE IMAGEN DESDE URL")
    print("="*70)
    
    if not OLLAMA_AVAILABLE:
        print("\n❌ Módulo de clasificación de imágenes no disponible")
        return
    
    classifier = OllamaImageClassifier()
    
    if not classifier.check_connection():
        print("\n❌ No se puede conectar con Ollama")
        return
    
    # URL de ejemplo (imagen de prueba)
    example_url = "https://picsum.photos/800/600"
    
    print(f"\n📸 Clasificando imagen desde URL: {example_url}")
    print("💡 Esta es una imagen aleatoria de ejemplo de Lorem Picsum")
    
    prompt = "Describe esta imagen brevemente en español"
    
    result = classifier.classify_single_image(
        image_source=example_url,
        prompt=prompt,
        is_url=True
    )
    
    if result:
        print("\n✅ Clasificación exitosa")
    else:
        print("\n❌ Error en la clasificación")


def mostrar_menu():
    """
    Muestra el menú de opciones
    """
    print("\n" + "="*70)
    print("MENÚ DE EJEMPLOS")
    print("="*70)
    print("1. Clasificación de texto con OpenAI (requiere API key)")
    print("2. Clasificación de imágenes desde directorio (requiere Ollama)")
    print("3. Clasificación de imagen desde URL (requiere Ollama)")
    print("4. Ejecutar todos los ejemplos")
    print("0. Salir")
    print("="*70)


def main():
    """
    Función principal
    """
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción (0-4): ").strip()
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        
        if opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        elif opcion == "1":
            ejemplo_clasificacion_texto()
        elif opcion == "2":
            ejemplo_clasificacion_imagen()
        elif opcion == "3":
            ejemplo_clasificacion_imagen_url()
        elif opcion == "4":
            ejemplo_clasificacion_texto()
            ejemplo_clasificacion_imagen()
            ejemplo_clasificacion_imagen_url()
        else:
            print("\n❌ Opción no válida. Por favor selecciona 0-4.")
        
        if opcion != "0":
            input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
