# pdf_page_counter.py
import streamlit as st
from utils import render_pdf

def main():
    st.sidebar.title("PDF Viewer")
    st.sidebar.write("Upload a PDF file to render and display it.")

    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        
        zoom_level = st.sidebar.slider("Zoom Level", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

        render_pdf(st, uploaded_file, zoom_level)
    else:
        st.write("Upload a PDF file using the sidebar to render and display it.")

if __name__ == "__main__":
    main()
