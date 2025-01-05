import requests
import os

class HttpsCall:

    @staticmethod
    def call_with_json_body(url, body):
        headers = {
            "Content-Type": "application/json"  # Important for JSON payloads
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error calling {url}: {response.status_code} {response.text}", response)
        return response.json()

class EazyaiCustomerReviewModel:
    url = f"https://api.dfpipe.com/eazyai"

    def __init__(self, apikey=None):
        self.apikey = apikey
        if self.apikey is None:
            self.apikey = os.getenv('DFPIPE_API_KEY')
        if self.apikey is None:
            self.apikey = "dfpipe-eazymodel-jikhoh-jybmac-pYxsi9"

    def customer_review_model_v1(self, text_items: list[str]):
        if len(text_items) >= 20:
            raise ValueError("Too many items, maximum 20")

        body = {
            "apikey": self.apikey,
            "data": [{"text": text} for text in text_items],
            "action": "infer",
            "model_id": "customer_review_sentiment_v1"
        }
        body = HttpsCall.call_with_json_body(self.url,body)
        return body
    
    def customer_review_model_v2(self, text_items: list[str]):
        if len(text_items) >= 20:
            raise ValueError("Too many items, maximum 20")

        body = {
            "apikey": self.apikey,
            "data": [{"text": text} for text in text_items],
            "action": "infer",
            "model_id": "sentiment-analysis-v2.1"
        }
        body = HttpsCall.call_with_json_body(self.url,body)
        return body

