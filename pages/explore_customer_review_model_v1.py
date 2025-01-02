import streamlit as st


def call_customer_review_model():
    from dfpipe_eazyai import EazyaiCustomerReviewModel
    if st.toggle("Call Customer Review Model", value=True):
        text_list = [
            "This is a good product",
            "This is a bad product",
            "Enjoyed eating here ...its got lots of seating areas inside and outside  .....ideal for large families, gatherings  .....the food is old style Italian and very sharable....its got lots of  options even vegetarian options.... its got good value  for feeding alot of people at the table potions are bigger then a average restaurant.  They got a upstairs  area too",
        ]
        texts = st.text_area("Customer reviews to test, separated by new line", value='\n'.join(text_list))
        texts = texts.split('\n')
        if st.button("Call Customer Review Model"):
            model = EazyaiCustomerReviewModel()
            result = model.customer_review_model_v1(texts)
            st.write(result)

def main():
    st.title("Explore Customer Review Model v1")
    call_customer_review_model()


if __name__ == "__main__":
    main()