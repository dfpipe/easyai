import streamlit as st
import pandas as pd


def main():
    st.title("Hello world! Welcome to use EazyAI Free model apis")
    st.write("You may find more information at https://dfpipe.com")

    from pages.explore_customer_review_model_v2 import call_customer_review_model
    call_customer_review_model()

if __name__ == "__main__":
    main()




