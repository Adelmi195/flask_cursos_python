# Aplicación Web de Análisis de Correspondencia Multivariado (ACM)

## Overview

Aplicación web educativa completa desarrollada con Flask que enseña y permite realizar Análisis de Correspondencia Multivariado (ACM). La aplicación incluye contenido educativo, un minijuego interactivo y una herramienta completa de análisis con interfaz web para cargar datos y generar resultados visuales.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

La aplicación sigue una arquitectura web moderna con Flask:

- **Frontend**: Templates HTML con Bootstrap 5, CSS personalizado con paleta verde, JavaScript interactivo
- **Backend**: Flask con Python para procesamiento de datos y análisis ACM
- **Data Processing**: Pandas, NumPy, Scikit-learn para análisis estadístico
- **Visualization**: Matplotlib y Seaborn para generación de gráficos
- **File Upload**: Soporte para CSV y XLSX con validación
- **Deployment**: Configurado para Replit en puerto 5000

## Key Components

### Frontend Templates
- **base.html**: Template base con navegación, Bootstrap y estilos personalizados
- **index.html**: Página principal educativa con explicaciones del ACM y minijuego
- **acm_tool.html**: Interfaz de carga de archivos con especificaciones técnicas
- **configure_acm.html**: Configuración de parámetros del análisis
- **results.html**: Visualización completa de resultados con gráficos y métricas

### Backend Components
- **app.py**: Servidor Flask principal con rutas y lógica de análisis
- **File Processing**: Manejo de uploads CSV/XLSX con validación
- **ACM Analysis**: Implementación usando PCA como aproximación al ACM
- **Plot Generation**: Creación de gráficos (scree plot, biplot, distribuciones)
- **Results Processing**: Cálculo de métricas y evaluación de calidad

### Styling and UX
- **style.css**: Paleta de colores verde completa, diseño responsivo
- **Interactive Elements**: Minijuego educativo, drag & drop para archivos
- **Animations**: Transiciones CSS y efectos visuales
- **Responsive Design**: Compatible con dispositivos móviles

## Data Flow

1. **Educación**: Usuario aprende conceptos ACM en página principal
2. **Minijuego**: Interacción práctica para entender agrupaciones
3. **Carga de Datos**: Upload de archivos CSV/XLSX con validación
4. **Configuración**: Selección de variables y parámetros de análisis
5. **Procesamiento**: Análisis ACM con generación de visualizaciones
6. **Resultados**: Presentación de métricas, gráficos e interpretación

## External Dependencies

- **Flask**: Framework web principal
- **Pandas**: Procesamiento y análisis de datos
- **NumPy**: Operaciones matemáticas
- **Scikit-learn**: Algoritmos de machine learning (PCA)
- **Matplotlib**: Generación de gráficos estáticos
- **Seaborn**: Visualizaciones estadísticas avanzadas
- **Openpyxl**: Lectura de archivos Excel
- **Werkzeug**: Utilidades web y seguridad

## Features Implemented

### Educational Content
- Explicación completa del ACM con conceptos matemáticos
- Fundamentos teóricos y aplicaciones prácticas
- Guías de interpretación de resultados
- Minijuego interactivo para aprendizaje

### Data Analysis Tool
- Upload de archivos con validación de formato
- Detección automática de variables categóricas
- Configuración flexible de parámetros
- Análisis ACM completo con múltiples visualizaciones
- Evaluación de calidad y recomendaciones

### Visualizations
- Scree plot (varianza explicada)
- Biplot (mapa de correspondencias)
- Distribuciones de variables categóricas
- Métricas de evaluación interactivas

## Deployment Strategy

### Development
- Run `python app.py` to start Flask development server
- Access application at `http://localhost:5000`
- Debug mode enabled for development

### Replit Deployment
- Configured for Flask Server workflow on port 5000
- Static files served from /static directory
- Upload functionality with /uploads directory
- Ready for production deployment

## Recent Changes (July 17, 2025)
- ✓ Migrated from static HTML to complete Flask application
- ✓ Implemented full ACM educational content in Spanish
- ✓ Created interactive learning game for ACM concepts
- ✓ Built comprehensive data upload and validation system
- ✓ Developed complete ACM analysis pipeline
- ✓ Generated multiple visualization types (scree, biplot, distributions)
- ✓ Added quality assessment and interpretation guides
- ✓ Implemented responsive green-themed design
- ✓ Created example dataset for testing