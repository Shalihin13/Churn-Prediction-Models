import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def view_project():
    # Load Data
    data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data.dropna(subset=['TotalCharges'], inplace=True)

    # Judul Halaman
    st.markdown( """<div><h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Visualisasi Telco Customer </h1> </div>""", unsafe_allow_html= True )
    st.write("Berikut adalah visualisasi interaktif dari data Telco Customer Churn untuk membantu memahami distribusi dan pola variabel terhadap churn.")

    # Expandable Dataset Viewer
    with st.expander('📁 Lihat Data', expanded=False):
        st.dataframe(data, use_container_width=True)

    # Tabs untuk Visualisasi
    tab1, tab2 = st.tabs(["📌 Visualisasi Variabel", "📈 Churn Analysis"])

    # Tab 1: Visualisasi Variabel
    with tab1:
        st.markdown("### 🎯 Distribusi Variabel")
        sb = st.selectbox('Select Variabel:', ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
         'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
         'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
         'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn',
         'tenure', 'MonthlyCharges'])
        
        numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        
        # Visualisasi distribusi terhadap churn
        st.write(f"##### Distribusi {sb} terhadap Churn")

        if sb in numerical_cols:
            # Binning data numerik terhadap churn
            data['binned'] = pd.cut(data[sb], bins=10)

            fig_bin, ax_bin = plt.subplots(figsize=(5, 3))
            sns.countplot(data=data, x='binned', hue='Churn', palette='Blues', ax=ax_bin)
            ax_bin.set_title(f'Distribusi {sb} terhadap Churn',size=8)
            ax_bin.set_xlabel(f'Rentang ({sb})',size=8)
            ax_bin.set_ylabel('Jumlah Pelanggan',size=8)
            ax_bin.set_xticklabels(ax_bin.get_xticklabels(),size=8, rotation=30)
            st.pyplot(fig_bin)

        else:
            # Barplot kategorikal terhadap churn
            fig_churn, ax_churn = plt.subplots(figsize=(5, 3))
            sns.countplot(data=data, x=sb, hue='Churn', palette='Blues', ax=ax_churn)
            ax_churn.set_title(f'{sb} vs Churn',size=8)
            ax_churn.set_ylabel("Jumlah Pelanggan",size=8)
            ax_churn.set_xticklabels(ax_churn.get_xticklabels(),size=8, rotation=15)
            st.pyplot(fig_churn)
            
         # Tambahkan kode ini sebelum visualisasi
            df_churn_tenure = data.groupby(['tenure', 'Churn']).size().reset_index(name='count')

            fig_race = px.bar(
                df_churn_tenure,
                x='count',
                y='Churn',
                color='Churn',
                animation_frame='tenure',
                orientation='h',
                title=('🎬 Perkembangan Customer Churn Berdasarkan Tenure'),
                range_x=[0, df_churn_tenure['count'].max() + 10],
                color_discrete_map={'Yes': "#3182bd", 'No': "#deebf7"})

            fig_race.update_layout(
                height=500,
                xaxis_title="Jumlah Pelanggan",
                yaxis_title="Status Churn",
                showlegend=False)
            
            st.plotly_chart(fig_race, use_container_width=True)
                            
    # Tab 2: Analisis Churn
    with tab2:
        st.markdown("### 🔍 Analisis Churn Lebih Lanjut")
        st.write('Variabel paling berpengaruh berdasarkan model terbaik')

        col1, col2 = st.columns(2)

        with col1:
        # Contract Vs Churn
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            sns.countplot(data=data, x='Contract', hue='Churn', palette='Blues', ax=ax1)
            ax1.set_title("Churn berdasarkan kontrak ")
            st.pyplot(fig1)

        # Tenure vs Churn
           # Buat rentang tenure
            bins = [0, 12, 24, 36, 48, 60, 72]
            labels = ['0-12', '13-24', '25-36', '37-48', '49-60', '61-72']

            # Tambahkan kolom bin
            data['tenure_group'] = pd.cut(data['tenure'], bins=bins, labels=labels, include_lowest=True)

            # Visualisasi countplot tenure berdasarkan Churn
            fig3, ax3 = plt.subplots(figsize=(7.5, 4))
            sns.countplot(data=data, x='tenure_group', hue='Churn', palette='Blues', ax=ax3)
            ax3.set_title("Churn berdasarkan Tenure ")
            ax3.set_xlabel("Rentang Tenure (bulan)")
            ax3.set_ylabel("Jumlah Pelanggan")
            st.pyplot(fig3)

        with col2:
        # Monthly Charges by Churn
            fig2, ax2 = plt.subplots(figsize=(5, 2.95))
            sns.boxplot(data=data, x='Churn', y='MonthlyCharges', ax=ax2, legend=False)
            ax2.set_title("Churn berdasarkan Monthly Charges ")
            st.pyplot(fig2)
            
        # Distribusi Churn
            churn_counts = data['Churn'].value_counts()

            fig4, ax4 = plt.subplots(figsize=(5,2.6))
            wedges, texts, autotexts = ax4.pie(
                churn_counts,
                labels=churn_counts.index,
                autopct='%1.1f%%',
                startangle=30,
                colors=["#08519c", "#9ecae1"],  
                wedgeprops=dict(width=0.4),
                pctdistance=1.5 )

            ax4.axis('equal')
            ax4.set_title("Distribusi Churn")
            st.pyplot(fig4)

           