from transformers import pipeline

 
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)

 
texts = [
    "I love this movie! It's fantastic.",
    "This product is terrible, I'm so disappointed."
]


 
results = sentiment_analyzer(texts)

for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Label: {result['label']}, Score: {result['score']:.4f}")
    print("-" * 40)
