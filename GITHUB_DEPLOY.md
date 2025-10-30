# 🚀 Guía para Subir a GitHub

## ✅ Lista de Verificación Pre-Commit

Antes de subir a GitHub, verifica que:

- [x] `.gitignore` está actualizado y protege archivos sensibles
- [x] No hay API keys en el código
- [x] `.env.example` está presente (plantilla de configuración)
- [x] `LICENSE` está incluido (MIT License)
- [x] `README.md` está actualizado y es público
- [x] Archivos innecesarios eliminados (COMPARISON.md, CHANGELOG.md, INDEX.md)
- [x] No hay archivos con datos personales

## 📝 Archivos que SE SUBIRÁN a GitHub

```
clasificacion-LLMs/
├── .env.example              ✅ Plantilla segura (sin claves reales)
├── .gitignore               ✅ Protección de archivos sensibles
├── ADVANCED_PROMPTS.md      ✅ Ejemplos de prompts
├── LICENSE                  ✅ Licencia MIT
├── QUICKSTART.md            ✅ Guía rápida
├── README.md                ✅ Documentación principal
├── check_installation.py    ✅ Script de verificación
├── classify_images_with_ollama.py  ✅ Script de imágenes
├── classify_with_gpt.py     ✅ Script de texto
├── example_usage.py         ✅ Ejemplos interactivos
├── prompt_18.txt            ✅ Prompt de clasificación
├── quick_test.py            ✅ Prueba rápida
└── requirements.txt         ✅ Dependencias
```

## 🚫 Archivos que NO se subirán (protegidos por .gitignore)

```
❌ .env                      # Tu API key real
❌ .env.local               # Configuración local
❌ *.csv                    # Datasets con datos personales
❌ *_results.json           # Resultados de clasificaciones
❌ images_test/             # Imágenes de prueba
❌ __pycache__/             # Cache de Python
❌ COMPARISON.md            # Documentación interna
❌ CHANGELOG.md             # Documentación interna
❌ INDEX.md                 # Documentación interna
```

## 🔒 Verificación de Seguridad

```bash
# 1. Verificar que no haya API keys en el código
grep -r "sk-proj" . --exclude-dir=.git
grep -r "OPENAI_API_KEY.*=" . --exclude-dir=.git | grep -v ".env.example"

# 2. Verificar archivos que se van a commitear
git status

# 3. Ver diferencias antes de commit
git diff
```

Si encuentras API keys, **DETENTE** y elimínalas antes de continuar.

## 📤 Comandos para Subir a GitHub

### Opción 1: Nuevo Repositorio

```bash
# 1. Inicializar git (si no está inicializado)
git init

# 2. Añadir archivos
git add .

# 3. Hacer commit
git commit -m "Initial commit: Text and Image Classification with LLMs"

# 4. Crear repositorio en GitHub (https://github.com/new)
# Nombre sugerido: clasificacion-llms

# 5. Conectar con repositorio remoto
git remote add origin https://github.com/TU-USUARIO/clasificacion-llms.git

# 6. Subir a GitHub
git branch -M main
git push -u origin main
```

### Opción 2: Repositorio Existente

```bash
# 1. Añadir cambios
git add .

# 2. Commit
git commit -m "Add image classification with Ollama and improved documentation"

# 3. Push
git push origin main
```

## ⚠️ IMPORTANTE: Antes de Push

```bash
# Verificar una última vez que no subes información sensible
git diff --cached

# Buscar archivos grandes o innecesarios
git ls-files | xargs ls -lh | sort -k5 -h -r | head -20

# Verificar .gitignore está funcionando
git status --ignored
```

## 🎯 Después de Subir

1. **Verifica en GitHub** que no aparezcan:
   - Archivos `.env` con claves reales
   - Archivos CSV con datos personales
   - Carpetas de resultados o imágenes de prueba

2. **Configura el repositorio**:
   - Añade descripción
   - Añade topics: `llm`, `classification`, `ollama`, `openai`, `computer-vision`
   - Configura GitHub Pages si quieres documentación web

3. **Protege la rama main**:
   - Settings → Branches → Add rule
   - Requiere pull request reviews (opcional)

## 🔄 Mantener el Repositorio Limpio

```bash
# Limpiar archivos no rastreados
git clean -n  # Ver qué se eliminaría
git clean -f  # Eliminar archivos

# Limpiar caché de Python
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Verificar que .gitignore funciona
git check-ignore -v <archivo>
```

## 📝 Crear Release (Opcional)

```bash
# 1. Tag de versión
git tag -a v1.0.0 -m "Initial release: Text and Image Classification"

# 2. Push del tag
git push origin v1.0.0

# 3. En GitHub: Releases → Create new release
# - Tag: v1.0.0
# - Title: "v1.0.0 - Initial Release"
# - Description: Features del release
```

## 🛡️ Si Accidentalmente Subiste una API Key

```bash
# 1. REVOCA la API key inmediatamente en:
# https://platform.openai.com/api-keys

# 2. Genera una nueva API key

# 3. Si ya hiciste push:
# NO uses git history rewrite en repos públicos
# En su lugar:
# - Revoca la clave comprometida
# - Crea nueva clave
# - Actualiza tu .env local
# - Añade un commit explicando que rotaste la clave

# 4. Considera usar GitHub Secrets Scanner
# https://docs.github.com/en/code-security/secret-scanning
```

## ✅ Checklist Final

Antes de compartir el repositorio públicamente:

- [ ] He verificado que no hay API keys en el código
- [ ] He probado que .gitignore funciona correctamente
- [ ] He leído el README y es apropiado para público
- [ ] La licencia está incluida
- [ ] Los ejemplos funcionan sin datos sensibles
- [ ] He actualizado la URL del repositorio en README
- [ ] He configurado la descripción y topics en GitHub

## 📞 Ayuda

Si tienes dudas sobre seguridad:
- Revisa: https://docs.github.com/en/code-security
- Usa: `git secrets` para escanear automáticamente
- Lee: https://gitguardian.com/

---

**¡Listo para GitHub! 🎉**

Una vez completada esta guía, tu repositorio estará limpio, seguro y listo para compartir.
