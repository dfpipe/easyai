import streamlit as st
import pandas as pd
from pathlib import Path




def logo_demo():
    from eazyai.logo import EazyaiLogoV4, draw_bounding_boxes
    from eazyai.utils import smart_read_image_v1
    st.title("Logo Detection V4 Demo")

    image = None

    btn_pre1 = st.button("use default image to show an example")
    if btn_pre1:
        # using the default image to show an example
        image = smart_read_image_v1('images/pexels-photo-29252132.webp')

    # data_type = st.radio("select a data type", ["url", "local image"])

    url = st.text_input("Enter a url to try the model")
    if url: 
        image = smart_read_image_v1(url)
    
    filep = st.file_uploader("Or you can upload a local image", type=["jpg", "jpeg", "png"])
    if filep:
        image = filep.read()
    

    def run_model(image):
        model = EazyaiLogoV4()
        result = model.detect_image(image)
        # get 1st image's result
        result = result[0]
        st.image(draw_bounding_boxes(image, result['prediction_list']))

        st.json(result)
    
    if image:
        run_model(image)

def main():
    st.title("Hello world! Welcome to use EazyAI Free model apis")
    st.write("You may find more information at https://dfpipe.com")

    logo_demo()

if __name__ == "__main__":
    main()




