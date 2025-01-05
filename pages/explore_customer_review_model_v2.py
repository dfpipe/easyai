import streamlit as st
import pandas as pd

def call_customer_review_model():
    from dfpipe_eazyai import EazyaiCustomerReviewModel

    st.title("Explore Review Sentiment Model v2")
    st.write("This is a free service to help you use pre-built AI models in your applications, business, analysis, etc.")
    st.write("You can upload a CSV file with a 'text' column, or use the default data.")
    st.write('If you upload a csv file, make sure the column name is "text"')
    st.write("You may find more information at https://dfpipe.com")

    # Allow user to upload a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)
    else:
        # Create an editable DataFrame with a 'text' column
        df = pd.DataFrame({'text': ["This is a good product", "This is a bad product", "I love this brand. This camera doorbell is fantastic. Great picture quality, wide view, super easy to install. Can’t recommend highly enough. Very smart little device, able to detect easily between object and person.",
        "I am not happy with this.", "Terrible experience.", "Highly recommend it!"]})
    
    # Display and allow editing of the DataFrame
    edited_df = st.data_editor(df, num_rows="dynamic")

    if st.button("Call dfpipe.eazyai api"):
        if 'text' in edited_df.columns:
            texts = edited_df['text'].tolist()
            st.warning("Calling the Dfpipe.eazyai api...Please wait for the model to finish processing...")
            model = EazyaiCustomerReviewModel()
            result = model.customer_review_model_v2(texts)
            if result['status_code'] == 200:
                results_json = result['body']['results']
                df1 = pd.DataFrame(results_json)
                df1 = df.merge(df1, left_index=True, right_index=True)
                st.write(df1)
            else:
                st.error(result['body'])
        else:
            st.error("The DataFrame must contain a 'text' column.")

def main():
    call_customer_review_model()

if __name__ == "__main__":
    main()