import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st
from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Visualisasi Prediksi Batu Ginjal')
    
    if st.checkbox('Plot Confusion Matrix'):
        model, score = train_model(x, y)
        plt.figure(figsize=(10, 6))
        disp = ConfusionMatrixDisplay.from_estimator(model, x, y, values_format='d')
        disp.plot()
        st.pyplot()
        
    if st.checkbox('Plot Decision Tree'):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nonckd', 'ckd']
        )
        st.graphviz_chart(dot_data)
