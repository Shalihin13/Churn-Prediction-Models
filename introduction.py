import streamlit as st

def view_intro():
    # title
        st.markdown( """<div>
        <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Churn Prediction 🏃‍♂️ </h1>
        </div>""", unsafe_allow_html= True )
        with st.expander(" ℹ️ Information", expanded=True):
             st.write("""
                    **Churn Prediction** merupakan salah satu analisis penting yang berdampak langsung pada profitabilitas perusahaan. 
                    Customer churn mengacu pada situasi di mana pelanggan berhenti menggunakan suatu produk atau layanan.

                    **Churn prediction** bertujuan untuk memprediksi pelanggan yang berpotensi berhenti menggunakan layanan,
                    sehingga perusahaan dapat mengambil langkah preventif untuk mempertahankan mereka.
                    Dengan menggunakan teknik **machine learning**, prediksi churn dilakukan berdasarkan data historis pelanggan, 
                    seperti perilaku penggunaan, lama berlangganan, dan jenis layanan yang digunakan. 

                    Model ini membantu mengidentifikasi pelanggan dengan risiko churn yang tinggi 
                    dan memungkinkan perusahaan melakukan intervensi dini untuk meningkatkan retensi pelanggan.
                    """)
            
        st.markdown("""
            ### How does it work ❓ 
            Pilih parameter-parameter yang paling berpengaruh, lalu model machine learning akan mempelajari hubungan antara parameter tersebut 
            dengan status pelanggan, berdasarkan pola dari data historis.
            Model akan memprediksi kemungkinan seorang pelanggan akan berhenti (churn) atau tetap menggunakan layanan.
            """)
        
    