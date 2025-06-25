from transformers import pipeline

def analyze_sentiment(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    label = result["label"]
    confidence = result["score"] * 100
    return label, confidence
