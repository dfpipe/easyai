
def customer_review_sentiment_v1_example():
    from dfpipe_eazyai import EazyaiCustomerReviewModel
    model = EazyaiCustomerReviewModel()
    result = model.customer_review_model_v1([
        "I love this brand. This camera doorbell is fantastic. Great picture quality, wide view, super easy to install. Can’t recommend highly enough. Very smart little device, able to detect easily between object and person.",
        "I am not happy with this.", 
        "Works as expected.",
        "Terrible experience.", 
        "Highly recommend it!",
    ])
    print('-----------Example 1-----------')
    print(result)
    print(result['body']['results'])

def customer_review_sentiment_v2_example():
    from dfpipe_eazyai import EazyaiCustomerReviewModel
    model = EazyaiCustomerReviewModel()
    result = model.customer_review_model_v2([
        "I love this brand. This camera doorbell is fantastic. Great picture quality, wide view, super easy to install. Can’t recommend highly enough. Very smart little device, able to detect easily between object and person.",
        "I am not happy with this.", 
        "Works as expected.",
        "Terrible experience.", 
        "Highly recommend it!",
    ])
    print('-----------Example 2-----------')
    print(result)
    print(result['body']['results'])


if __name__ == "__main__":
    customer_review_sentiment_v1_example()
    customer_review_sentiment_v2_example()