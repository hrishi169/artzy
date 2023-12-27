import streamlit as st
import cv2
from PIL import Image
import numpy as np
import io

def create_sketch(img):
    kernel = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        ], np.uint8)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    img_diff = cv2.absdiff(img_dilated, img_gray)
    contour = 255 - img_diff
    return contour

def main():
    st.header("Artzy", divider="rainbow")
    # Add File upload widget
    uploaded_file = st.file_uploader("Add any picture to convert to sketch")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(bytes_data)
        with col2:
            if st.button('Generate Sketch'):
                # Generarte Sketch from an input image
                input_image = np.array(Image.open(io.BytesIO(bytes_data))) 
                output_sketch = create_sketch(input_image)
                with col3:
                    st.image(output_sketch)

main()
