import requests
import joblib 
import os
import streamlit as st
import pandas as pd
import pickle
import warnings
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize


def predict():
    model = joblib.load('churn_model_3fitur.joblib')
        
    st.markdown("""
        <h1 style="color:mediumseagreen; text-align:left;">🧠 Prediksi Churn Pelanggan</h1>
        <p style="text-align:justify;">
            Gunakan form di bawah untuk memprediksi apakah pelanggan akan melakukan <b>churn</b> berdasarkan tiga fitur utama:
            <i>Tenure, Monthly Charges</i>, dan <i>Jenis Kontrak</i>.</p> """, unsafe_allow_html=True)
    
    with st.form('Prediction Form'):
        st.markdown("#### 📋 Input Data Pelanggan")
        set1, set2, set3 = st.columns (3)
        with set1 :
            tenure = st.select_slider('Choose Tenure:', list(range(0,73)))
            
        with set2 :
            MonthlyCharges = st.select_slider('Choose MonthlyCharges:', ("Low", "Mid", "High", "Very High"))
            charge_mapping = {
            "Low": 22.23,
            "Mid": 55.72,
            "High": 80.22,
            "Very High": 100.89}
            MonthlyCharges_val = charge_mapping[MonthlyCharges]
            
        with set3 :
            Contract  = st.select_slider('Choose Contract:' , ('Month-to-month', 'One year', 'Two year'))
            contract_mapping = {
            'Month-to-month': 1,
            'One year': 2,
            'Two year': 3}
            Contract_val = contract_mapping[Contract]

        data_predict = {'tenure':[tenure],'MonthlyCharges':[MonthlyCharges_val], 'Contract':[Contract_val]}
        data_predict= pd.DataFrame(data_predict, index=[0])
        
        # Submit Button
        submitted = st.form_submit_button('🔍Predict')
        
        if submitted :
            prediction = model.predict(data_predict)
            label = 'Churn' if prediction[0] == 1 else 'No Churn'
            # st.success(f"🎯Prediction: {label}")
            st.markdown("---")
            st.markdown(f"""
                <div style='text-align:center; font-size:20px;'>
                    <strong>🎯 Hasil Prediksi:</strong><br>
                    <span style='color:mediumseagreen; font-size:26px;'>{label}</span>
                </div>
            """, unsafe_allow_html=True)
