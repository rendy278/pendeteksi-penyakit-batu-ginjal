import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title('Halaman Prediksi')
    col1, col2, col3 = st.columns(3)
    with col1:
        bp = st.text_input('Input Nilai bp')
        sg = st.text_input('Input Nilai sg')
        al = st.text_input('Input Nilai al')
        su = st.text_input('Input Nilai su')
        rbc = st.text_input('Input Nilai rbc')
        pc = st.text_input('Input Nilai pc')
        pcc = st.text_input('Input Nilai pcc')
        ba = st.text_input('Input Nilai ba')

    with col2:
        bgr = st.text_input('Input Nilai bgr')
        bu = st.text_input('Input Nilai bu')
        sc = st.text_input('Input Nilai sc')
        sod = st.text_input('Input Nilai sod')
        pot = st.text_input('Input Nilai pot')
        hemo = st.text_input('Input Nilai hemo')
        pcv = st.text_input('Input Nilai pcv')
        wc = st.text_input('Input Nilai wc')

    with col3:
        rc = st.text_input('Input Nilai rc')
        htn = st.text_input('Input Nilai htn')
        dm = st.text_input('Input Nilai dm')
        cad = st.text_input('Input Nilai cad')
        appet = st.text_input('Input Nilai appet')
        pe = st.text_input('Input Nilai pe')
        ane = st.text_input('Input Nilai ane')
        
    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, 
                hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]
    
    # Tombol prediksi
    if st.button('Prediksi'):
        prediction, score = predict(x, y, features)
        st.info('Prediksi Sukses...')
        
        if prediction == 1:
            st.warning('Orang Tersebut Rentan Terkena Penyakit Ginjal')
        else:
            st.success('Orang Tersebut Relatif Aman Dari Terkena Penyakit Ginjal')
            
        st.write('Model yang digunakan memiliki tingkat akurasi', (score * 100), '%')
