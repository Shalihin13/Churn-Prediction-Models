import streamlit as st

st.set_page_config(page_title="Churn Prediction", page_icon= "🏃‍♂️", layout='centered', initial_sidebar_state="collapsed")

st.sidebar.title('Navigasi')
page = st.sidebar.radio('Select',["Introduction", "Project", "Machine Learning","About Me"])

if page == 'Introduction':
        import introduction
        introduction.view_intro()
        
elif page == 'Project':
        import project
        project.view_project()

elif page == 'Machine Learning':
        import machine_learning
        machine_learning.predict()
        
else : 
        import about_me
        about_me.view_about_me()
