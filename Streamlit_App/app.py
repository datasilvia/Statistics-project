import streamlit as st
from PIL import Image
import os

# Función para cargar imágenes de manera segura
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Error: No image found at {image_path}")
        return None

# Cargar imágenes desde la carpeta Streamlit_App/images
title_image = load_image('gato.png')
menu_image = load_image('menu.png')

# Mostrar la imagen de título si se cargó correctamente
if title_image:
    st.image(title_image, use_column_width=True)

# Crear el menú de navegación
if menu_image:
    st.sidebar.image(menu_image, use_column_width=True)
st.sidebar.title("Navigation")

# Botón para seleccionar el idioma
language = st.sidebar.radio("Select Language", ["English", "Español"])

# Botón para alternar entre modo claro y modo oscuro
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])

# Aplicar el tema seleccionado
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e1117;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #0e1117;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Botón para ir al repositorio de GitHub
if st.sidebar.button('Go to GitHub Repository'):
    js = "window.open('https://github.com/datasilvia/Statistics-project')"
    st.sidebar.markdown(f'<a href="https://github.com/datasilvia/Statistics-project" target="_blank">Go to GitHub Repository</a>', unsafe_allow_html=True)

# Definir las secciones de la aplicación
if language == "English":
    menu = st.sidebar.radio("Go to", ["Objectives", "Development Process", "Charts and Visualizations", "Results and Conclusions"])

    if menu == "Objectives":
        st.title("🎯 Objectives")
        st.write("""
        The objective of this project is to analyze the results of a digital experiment conducted by the Customer Experience (CX) team at Vanguard. The experiment aims to determine if a new user interface (UI) and in-context prompts improve the completion rate of the online process for clients.
        """)
        st.subheader("⚙️ Functionality")
        st.write("""
        This project includes the following functionalities:
        - 🔍 Data exploration and cleaning: EDA and Data Cleaning
        - 📊 Client behavior analysis
        - 📈 Performance metrics evaluation
        - 🧪 Hypothesis testing: Assess the effectiveness of the redesign
        - 🔬 Experiment evaluation
        - 📉 Interactive data visualization: Using Tableau
        """)
        st.subheader("🛠️ Tools Used")
        st.write("""
        The following tools and technologies were used to carry out this project:
        - 🐍 Python: For data exploration and analysis
        - 📊 Pandas: For data manipulation and cleaning
        - 📉 Matplotlib and Seaborn: For data visualization
        - 📊 Tableau: For creating interactive visualizations
        - 📓 Jupyter Notebook: For documenting and presenting the analysis
        - 🐙 GitHub: For version control and collaboration
        - 📋 Trello: For project management
        """)
    elif menu == "Development Process":
        st.title("🚀 Development Process")
        st.subheader("🧹 Data Exploration and Cleaning")
        st.write("""
        - Initial exploration of the datasets (df_final_demo, df_final_web_data, df_final_experiment_clients).
        - Data cleaning and resolving quality issues.
        """)
        st.subheader("📊 Client Behavior Analysis")
        st.write("""
        - Demographic analysis of clients.
        - Analysis of client behavior during the online process.
        """)
        st.subheader("📈 Performance Metrics Evaluation")
        st.write("""
        - Defining success indicators.
        - Evaluating the outcome of the redesign.
        """)
        st.subheader("🧪 Hypothesis Testing")
        st.write("""
        - Conducting hypothesis tests on the completion rate.
        - Evaluating the completion rate with a cost-effectiveness threshold.
        - Conducting other relevant hypothesis tests.
        """)
        st.subheader("🔬 Experiment Evaluation")
        st.write("""
        - Evaluating the design effectiveness.
        - Assessing the duration of the experiment.
        - Identifying additional data needs.
        """)
        st.subheader("📉 Data Visualization with Tableau")
        st.write("""
        - Creating interactive visualizations in Tableau.
        - Preparing dashboards for the presentation.
        """)
        st.subheader("📋 Trello Board")
        st.write("""
        Our Trello board is an essential tool for managing the project's workflow and ensuring that all tasks are organized and tracked efficiently. It helps us to:
        - Plan: Outline the project's objectives, milestones, and deliverables.
        - Organize: Break down the project into manageable tasks and assign them to team members.
        - Track Progress: Monitor the status of each task, from to-do to in-progress to completed.
        - Collaborate: Facilitate communication and collaboration among team members by providing a centralized platform for updates and feedback.
        - Adapt: Adjust plans and priorities as needed based on the project's progress and any new insights or challenges that arise.
        """)
        st.image('trello.png', use_column_width=True)
    elif menu == "Charts and Visualizations":
        st.title("Charts and Visualizations")
        st.write("Create and explore interactive visualizations using Tableau.")
    elif menu == "Results and Conclusions":
        st.title("Results and Conclusions")
        st.subheader("📈 Results")
        st.write("""
        The project results include:
        - A detailed analysis of client behavior and the effectiveness of the redesign.
        - Hypothesis tests supporting conclusions about the completion rate.
        - Interactive visualizations in Tableau presenting the findings clearly and comprehensively.
        - A final report and presentation summarizing the results and recommendations.
        """)
else:
    menu = st.sidebar.radio("Ir a", ["Objetivos", "Proceso de Desarrollo", "Gráficos y Visualizaciones", "Resultados y Conclusiones"])

    if menu == "Objetivos":
        st.title("🎯 Objetivos")
        st.write("""
        El objetivo de este proyecto es analizar los resultados de un experimento digital realizado por el equipo de Customer Experience (CX) en Vanguard. El experimento tiene como objetivo determinar si una nueva interfaz de usuario (UI) y mensajes contextuales mejoran la tasa de finalización del proceso en línea para los clientes.
        """)
        st.subheader("⚙️ Funcionalidad")
        st.write("""
        Este proyecto incluye las siguientes funcionalidades:
        - 🔍 Exploración y limpieza de datos: EDA y limpieza de datos
        - 📊 Análisis del comportamiento del cliente
        - 📈 Evaluación de métricas de rendimiento
        - 🧪 Pruebas de hipótesis: Evaluar la efectividad del rediseño
        - 🔬 Evaluación del experimento
        - 📉 Visualización de datos interactiva: Usando Tableau
        """)
        st.subheader("🛠️ Herramientas Utilizadas")
        st.write("""
        Las siguientes herramientas y tecnologías se utilizaron para llevar a cabo este proyecto:
        - 🐍 Python: Para la exploración y análisis de datos
        - 📊 Pandas: Para la manipulación y limpieza de datos
        - 📉 Matplotlib y Seaborn: Para la visualización de datos
        - 📊 Tableau: Para crear visualizaciones interactivas
        - 📓 Jupyter Notebook: Para documentar y presentar el análisis
        - 🐙 GitHub: Para el control de versiones y la colaboración
        - 📋 Trello: Para la gestión de proyectos
        """)
    elif menu == "Proceso de Desarrollo":
        st.title("🚀 Proceso de Desarrollo")
        st.subheader("🧹 Exploración y Limpieza de Datos")
        st.write("""
        - Exploración inicial de los conjuntos de datos (df_final_demo, df_final_web_data, df_final_experiment_clients).
        - Limpieza de datos y resolución de problemas de calidad.
        """)
        st.subheader("📊 Análisis del Comportamiento del Cliente")
        st.write("""
        - Análisis demográfico de los clientes.
        - Análisis del comportamiento del cliente durante el proceso en línea.
        """)
        st.subheader("📈 Evaluación de Métricas de Rendimiento")
        st.write("""
        - Definición de indicadores de éxito.
        - Evaluación del resultado del rediseño.
        """)
        st.subheader("🧪 Pruebas de Hipótesis")
        st.write("""
        - Realización de pruebas de hipótesis sobre la tasa de finalización.
        - Evaluación de la tasa de finalización con un umbral de rentabilidad.
        - Realización de otras pruebas de hipótesis relevantes.
        """)
        st.subheader("🔬 Evaluación del Experimento")
        st.write("""
        - Evaluación de la efectividad del diseño.
        - Evaluación de la duración del experimento.
        - Identificación de necesidades adicionales de datos.
        """)
        st.subheader("📉 Visualización de Datos con Tableau")
        st.write("""
        - Creación de visualizaciones interactivas en Tableau.
        - Preparación de paneles para la presentación.
        """)
        st.subheader("📋 Tablero de Trello")
        st.write("""
        Nuestro tablero de Trello es una herramienta esencial para gestionar el flujo de trabajo del proyecto y garantizar que todas las tareas estén organizadas y se realicen de manera eficiente. Nos ayuda a:
        - Planificar: Definir los objetivos, hitos y entregables del proyecto.
        - Organizar: Desglosar el proyecto en tareas manejables y asignarlas a los miembros del equipo.
        - Seguimiento del Progreso: Monitorear el estado de cada tarea, desde pendiente hasta en progreso y completada.
        - Colaborar: Facilitar la comunicación y colaboración entre los miembros del equipo proporcionando una plataforma centralizada para actualizaciones y comentarios.
        - Adaptar: Ajustar los planes y prioridades según sea necesario en función del progreso del proyecto y cualquier nueva información o desafío que surja.
        """)
        st.image('trello.png', use_column_width=True)
    elif menu == "Gráficos y Visualizaciones":
        st.title("Gráficos y Visualizaciones")
        st.write("Crea y explora visualizaciones interactivas utilizando Tableau.")
    elif menu == "Resultados y Conclusiones":
        st.title("Resultados y Conclusiones")
        st.subheader("📈 Resultados")
        st.write("""
        Los resultados del proyecto incluyen:
        - Un análisis detallado del comportamiento del cliente y la efectividad del rediseño.
        - Pruebas de hipótesis que respaldan las conclusiones sobre la tasa de finalización.
        - Visualizaciones interactivas en Tableau que presentan los hallazgos de manera clara y completa.
        - Un informe final y una presentación que resumen los resultados y recomendaciones.
        """)

# Ejecutar la aplicación con: streamlit run app.py
