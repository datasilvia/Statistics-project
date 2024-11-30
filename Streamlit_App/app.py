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
menu = st.sidebar.radio("Go to", ["Objectives", "Development Process", "Charts and Visualizations", "Results and Conclusions"])

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
        </style>
        """,
        unsafe_allow_html=True
    )

# Botón para ir al repositorio de GitHub
if st.sidebar.button('Go to GitHub Repository'):
    js = "window.open('https://github.com/datasilvia/Statistics-project')"
    st.sidebar.markdown(f'<a href="https://github.com/datasilvia/Statistics-project" target="_blank">Go to GitHub Repository</a>', unsafe_allow_html=True)


# Definir las secciones de la aplicación
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

# Ejecutar la aplicación con: streamlit run app.py