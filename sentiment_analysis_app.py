import requests


api_url = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"


headers = {
    "Authorization": "Bearer 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"
}
     

text = "I love programming!"

response = requests.post(api_url, headers=headers, json={"inputs": text})

if response.status_code == 200:
    result = response.json()

    label = result[0][0]['label']
    score = result[0][0]['score']
    print(f"Sentiment: {label} with confidence {score:.4f}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
