# 🛍️ NovaMarket AI Assistant

🤖 **Asistente Inteligente basado en IA para atención al cliente**

Desarrollado con **Python, Streamlit, LangChain y Google Gemini**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.60-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Oracle Cloud](https://img.shields.io/badge/Oracle-Cloud-red)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-green)

---

## 🌐 Demo en línea

La aplicación se encuentra desplegada en **Oracle Cloud Infrastructure (OCI)** y puede ser utilizada desde el siguiente enlace:

🔗 **Aplicación:** http://144.22.47.242/

**Repositorio del proyecto:**  
https://github.com/jeampierogonzalez81/AsistenteAI-NovaMarket

---

## 📖 Descripción

NovaMarket AI Assistant es un asistente conversacional desarrollado para responder preguntas de clientes utilizando exclusivamente documentación oficial en formato PDF.

El proyecto demuestra cómo implementar un sistema de consulta documental utilizando modelos de lenguaje de última generación, limitando las respuestas únicamente a la información disponible para reducir las alucinaciones del modelo.

## ✨ Características

✅ Interfaz moderna con Streamlit

✅ Integración con Google Gemini

✅ Procesamiento automático de múltiples PDF

✅ Historial de conversación

✅ Diseño inspirado en un sitio de comercio electrónico

✅ Respuestas únicamente basadas en la documentación

✅ Arquitectura modular

## 🏗️ Arquitectura

```
                     Usuario
                        │
                        ▼
               Streamlit Interface
                        │
                        ▼
               LangChain Prompt
                        │
                        ▼
             Google Gemini 2.5 Flash
                        ▲
                        │
           Documentación PDF NovaMarket
```

## 📂 Estructura

```
challenge-alura-python
│
├── documents/
│
├── src/
│   ├── agent.py
│   ├── app.py
│   ├── create_pdfs.py
│   ├── document_loader.py
│   └── ui_components.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python | Backend |
| Streamlit | Interfaz |
| LangChain | Orquestación |
| Google Gemini | Modelo LLM |
| PyPDF | Lectura PDF |
| dotenv | Variables de entorno |

## 🚀 Instalación

### Clonar

```bash
git clone https://github.com/jeampierogonzalez81/AsistenteAI-NovaMarket.git
```

### Entrar

```bash
cd AsistenteAI-NovaMarket
```

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar

#### Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🔑 Variables de entorno

Crear un archivo `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

## ▶️ Ejecutar

```bash
streamlit run src/app.py
```

## 💬 Ejemplos de preguntas

- ¿Cómo funciona la garantía?
- ¿Cuáles son los métodos de pago?
- ¿Qué cubre la política de devoluciones?
- ¿Cuánto tarda un envío?
- ¿Cómo protegen mis datos personales?

## 📈 Posibles mejoras

- Embeddings
- FAISS
- ChromaDB
- Carga dinámica de documentos
- Panel administrativo
- Autenticación de usuarios

## 👨‍💻 Autor

**Johan González**

**GitHub**

https://github.com/jeampierogonzalez81

**LinkedIn**

(Agregar perfil)

## 📄 Licencia

Proyecto desarrollado como parte del **Challenge de Alura Latam**, con fines educativos y demostrativos.
