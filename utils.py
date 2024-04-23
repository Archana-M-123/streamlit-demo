# utils.py
import fitz
from PIL import Image
import io
import os

def render_pdf(st, uploaded_file, zoom_level):
   
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    try:
        pdf_doc = fitz.open("temp.pdf")

        for page_num in range(len(pdf_doc)):
            page = pdf_doc.load_page(page_num)
            zoom_matrix = fitz.Matrix(zoom_level, zoom_level)
            pixmap = page.get_pixmap(matrix=zoom_matrix)
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

            with io.BytesIO() as output:
                img.save(output, format="PNG")
                image_bytes = output.getvalue()

            st.image(image_bytes)

    except Exception as e:
        st.error(f"Error rendering PDF: {e}")

    finally:
        os.remove("temp.pdf")
