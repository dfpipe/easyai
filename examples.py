
def customer_review_sentiment_v1_example():
    from dfpipe_eazyai import EazyaiCustomerReviewModel
    model = EazyaiCustomerReviewModel()
    result = model.customer_review_model_v1(["This is a good product", "This is a bad product"])
    print(result)


if __name__ == "__main__":
    customer_review_sentiment_v1_example()