---
title: Eazyai
emoji: 🚀
colorFrom: red
colorTo: red
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# Dfpipe.EazyAI

## What is Dfpipe.EazyAI?
Dfpipe EazyAI is a free service to help you use pre-built AI models in your applications, business, analysis, etc.

## How to use Dfpipe EazyAI APIs
### Option 1: Call the HTTPS API directly
You can simply use the API by making HTTP requests to the API. 
```
curl -X POST https://api.dfpipe.com/eazyai -H "Content-Type: application/json" -d '{"apikey": "dfpipe-eazymodel-jikhoh-jybmac-pYxsi9", "data": [{"text": "This is a good product"}, {"text": "This is a bad product"}], "action": "infer", "model_id": "customer_review_sentiment_v1"}'
```

Then you will get the result in JSON format, such as, 
```
{
    "status_code": 200, 
    "body": {
        "results": [{"y": 1, "confidence": 0.932}, {"y": 0, "confidence": 0.998}], 
        "model_id": "customer_review_sentiment_v1", 
        "model_version": "1.0"
    }
}
```

### Option 2: Use the python script to call the API

See examples.py -> customer_review_sentiment_v1_example()


