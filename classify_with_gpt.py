#!/usr/bin/env python3
"""
Script para clasificar frases usando GPT-4o-mini via API de OpenAI
y evaluar el desempeño comparando con las etiquetas correctas (_ME)
"""

import pandas as pd
import json
import time
import os
from typing import Dict, List, Tuple
from openai import OpenAI
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# Configuración de la API
API_KEY = os.getenv('API_KEY_OPENAI')  # Usar variable de entorno para seguridad
if not API_KEY:
    raise ValueError("Por favor, configura la variable de entorno API_KEY_OPENAI con tu clave de API de OpenAI")
MODEL = 'gpt-4o-mini-2024-07-18'  # Usamos el modelo disponible más cercano

# Configurar cliente OpenAI
client = OpenAI(api_key=API_KEY)

def load_prompt() -> str:
    """Carga el prompt desde el archivo"""
    with open('prompt_18.txt', 'r', encoding='utf-8') as f:
        return f.read()

def classify_sentence_with_gpt(sentence: str, prompt: str, max_retries: int = 3) -> Dict:
    """
    Clasifica una frase usando GPT-4o-mini
    """
    full_prompt = f"{prompt}\n\nClassify the following sentence:\n\"{sentence}\""
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a multilingual identity statement classifier. Always respond with valid JSON following the specified format."},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.1,  # Baja temperatura para resultados más consistentes
                max_tokens=1500
            )
            
            response_text = response.choices[0].message.content.strip()
            
            # Intentar parsear JSON
            try:
                # Limpiar el texto si contiene markdown
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                
                result = json.loads(response_text)
                return result
                
            except json.JSONDecodeError:
                print(f"Error parsing JSON on attempt {attempt + 1} for sentence: {sentence[:50]}...")
                if attempt == max_retries - 1:
                    return create_error_response(sentence, "JSON parsing error")
                
        except Exception as e:
            print(f"API error on attempt {attempt + 1} for sentence: {sentence[:50]}... Error: {e}")
            if attempt == max_retries - 1:
                return create_error_response(sentence, f"API error: {e}")
            time.sleep(2)  # Esperar antes de reintentar
    
    return create_error_response(sentence, "Max retries exceeded")

def create_error_response(sentence: str, error: str) -> Dict:
    """Crea una respuesta de error en el formato esperado"""
    return {
        "sentences": [{
            "text": sentence,
            "sense": "ERROR",
            "reference": "ERROR", 
            "attribution": "ERROR",
            "sense_justification": f"Error: {error}",
            "reference_justification": f"Error: {error}",
            "attribution_justification": f"Error: {error}"
        }],
        "summary": {
            "sense": "ERROR",
            "reference": "ERROR",
            "attribution": "ERROR",
            "sense_justification": f"Error: {error}",
            "reference_justification": f"Error: {error}",
            "attribution_justification": f"Error: {error}"
        }
    }

def extract_classification(gpt_response: Dict, sentence: str) -> Tuple[str, str, str]:
    """
    Extrae las clasificaciones de la respuesta de GPT
    """
    try:
        if "sentences" in gpt_response and len(gpt_response["sentences"]) > 0:
            sentence_data = gpt_response["sentences"][0]
            sense = sentence_data.get("sense", "ERROR")
            reference = sentence_data.get("reference", "ERROR")
            attribution = sentence_data.get("attribution", "ERROR")
            
            # Convertir valores NA a "NA" (categoría válida)
            if reference == "NA":
                reference = "NA"
            if attribution == "NA":
                attribution = "NA"
                
            return sense, reference, attribution
        else:
            return "ERROR", "ERROR", "ERROR"
    except Exception as e:
        print(f"Error extracting classification for sentence: {sentence[:50]}... Error: {e}")
        return "ERROR", "ERROR", "ERROR"

def normalize_categories(category: str, dimension: str) -> str:
    """
    Normaliza las categorías para la comparación
    """
    if pd.isna(category) or category == "" or category == "ERROR":
        return "NA"
    
    category = str(category).strip()
    
    # Mapeo de categorías para Reference (jerarquía superior)
    if dimension == "reference":
        reference_mapping = {
            # Sin anclaje
            "Biosocial": "Sin anclaje", "Generic": "Sin anclaje",
            "Name": "Sin anclaje", "Gender": "Sin anclaje", "Age": "Sin anclaje",
            "Physical Characteristics": "Sin anclaje", "Health identity": "Sin anclaje",
            "Universal definition": "Sin anclaje", "Material partitive": "Sin anclaje",
            "Social partitive": "Sin anclaje",
            
            # Anclaje  
            "Familiar": "Anclaje", "Groupal": "Anclaje", "Active": "Anclaje", "Social": "Anclaje",
            "Matrimonial": "Anclaje", "Partner": "Anclaje", "Nuclear family": "Anclaje",
            "Extended family": "Anclaje", "Home": "Anclaje", "Housing": "Anclaje",
            "Primary group": "Anclaje", "Secondary group": "Anclaje", "Generalized other": "Anclaje",
            "Job": "Anclaje", "Work role": "Anclaje", "Unemployment": "Anclaje",
            "Educational role": "Anclaje", "Complementary activity": "Anclaje",
            "Social class": "Anclaje", "Local": "Anclaje", "Local identity": "Anclaje",
            "Intermediate identity": "Anclaje", "State identity": "Anclaje",
            "Supranational identity": "Anclaje", "Marginal identity": "Anclaje",
            "Queer identity": "Anclaje", "Political identity": "Anclaje",
            "Sexual Orientation": "Anclaje", "Ethnic identity": "Anclaje",
            "Famous personalities": "Anclaje", "Religious identity": "Anclaje",
            "Linguistic reference": "Anclaje"
        }
        return reference_mapping.get(category, category)
    
    # Mapeo de categorías para Sense (jerarquía superior)
    elif dimension == "sense":
        sense_mapping = {
            # Consensual
            "Physical": "Consensual", "Collective": "Consensual", "Activity": "Consensual",
            "Property": "Consensual", "Narrative": "Consensual", "Global": "Consensual",
            
            # Subconsensual
            "Attitudinal": "Subconsensual", "Self-esteem": "Subconsensual",
            "Preference": "Subconsensual", "Beliefs": "Subconsensual",
            "Aspirations": "Subconsensual", "Self-doubt": "Subconsensual",
            "Nihilistic": "Subconsensual", "About others": "Subconsensual",
            "Test evasion": "Subconsensual", "Metaphor": "Subconsensual"
        }
        return sense_mapping.get(category, category)
    
    return category

def main():
    """
    Función principal
    """
    print("=== CLASIFICACIÓN DE FRASES CON GPT-4o-mini ===\n")
    
    # Cargar datos
    print("Cargando datos...")
    df = pd.read_csv("clasificacion_ME_204_simple.csv")
    print(f"Total de frases a clasificar: {len(df)}")
    
    # Cargar prompt
    print("Cargando prompt...")
    prompt = load_prompt()
    
    # Preparar resultados
    results = []
    
    print("\nIniciando clasificación...")
    start_time = time.time()
    
    for idx, row in df.iterrows():
        sentence = row['frase']
        print(f"Procesando frase {idx + 1}/{len(df)}: {sentence[:50]}...")
        
        # Clasificar con GPT
        gpt_response = classify_sentence_with_gpt(sentence, prompt)
        
        # Extraer clasificaciones
        sense_pred, reference_pred, attribution_pred = extract_classification(gpt_response, sentence)
        
        # Normalizar categorías verdaderas (de específicas a jerarquía superior)
        sense_true = normalize_categories(row['sense_ME'], 'sense')
        reference_true = normalize_categories(row['reference_ME'], 'reference') if pd.notna(row['reference_ME']) else "NA"
        attribution_true = str(row['attribution_ME']) if pd.notna(row['attribution_ME']) else "NA"
        
        # Almacenar resultados
        result = {
            'bio_num': row['bio_num'],
            'frase_num': row['frase_num'],
            'frase': sentence,
            'sense_true': sense_true,
            'sense_predicted': sense_pred,
            'reference_true': reference_true,
            'reference_predicted': reference_pred,
            'attribution_true': attribution_true,
            'attribution_predicted': attribution_pred,
            'gpt_response': json.dumps(gpt_response)
        }
        results.append(result)
        
        # Pausa para evitar límites de rate
        time.sleep(0.5)
        
        # Guardar progreso cada 10 frases
        if (idx + 1) % 10 == 0:
            temp_df = pd.DataFrame(results)
            temp_df.to_csv(f"temp_results_{idx + 1}.csv", index=False)
            print(f"Progreso guardado: {idx + 1} frases procesadas")
    
    # Crear DataFrame con resultados
    df_results = pd.DataFrame(results)
    
    # Guardar resultados completos
    df_results.to_csv("gpt_classification_results.csv", index=False)
    
    elapsed_time = time.time() - start_time
    print(f"\nClasificación completada en {elapsed_time:.2f} segundos")
    
    print("\nArchivos generados:")
    print("- gpt_classification_results.csv: Resultados completos de clasificación")

if __name__ == "__main__":
    main()
