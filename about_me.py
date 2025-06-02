import streamlit as st


def view_about_me():
        st.markdown( """<div><h1 style="color:MEDIUMSEAGREEN;text-align:left;"> About Me 👤</h1>
        </div>""", unsafe_allow_html= True )        
        st.write ("""
                  👋 Hi, saya **Shalihin** — seorang data enthusiast memiliki ketertarikan dibidang **Machine Learning** dan **Visualisasi Data**.
                    Saya senang mengubah data menjadi wawasan yang bermakna melalui pemodelan analitik, serta membangun sistem prediktif untuk memecahkan masalah nyata. 
                    Dengan pendekatan yang fokus pada kejelasan dan interpretasi, saya berusaha menjadikan data lebih mudah dipahami dan bermanfaat bagi pengambilan keputusan. 
                    Mari kita jelajahi apa yang bisa diungkapkan oleh data !!""")
                  
        st.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/shalihin2205)')
        st.markdown('[![GitHub](https://img.shields.io/badge/GitHub-Profile-silver)](https://github.com/Shalihin13)')
        st.write('[![Email](https://img.shields.io/badge/Email-blue)(zayntaufik.28@gmail.com)')
        
