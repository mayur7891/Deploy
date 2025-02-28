import pickle
import pandas as pd
import os
import re






pickle_tokenizer_path = os.path.abspath(os.path.join("app/pickles/tokenizer.pkl"))
pickle_sbert_path = os.path.abspath(os.path.join("app/pickles/sbert_pipeline.pkl"))

with open(pickle_tokenizer_path, "rb") as f:
    tokenizer = pickle.load(f)

with open(pickle_sbert_path, "rb") as f:
    sbert_model = pickle.load(f)

from transformers import pipeline
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_analyzer = sentiment_analyzer = pipeline("sentiment-analysis", model=model_name, tokenizer=tokenizer)

# def truncate_comment(comment):
#     tokens = tokenizer.encode(comment, truncation=True, max_length=512)
#     return tokenizer.decode(tokens, skip_special_tokens=True)


# def analyze_sentiment(comment):
#     if pd.isna(comment) or not isinstance(comment, str) or comment.strip() == "":
#         return "neutral", 0.0

#     truncated_comment = truncate_comment(comment)

#     try:
#         result = sentiment_analyzer(truncated_comment)[0]
#         sentiment = result["label"].lower()
#         # confidence = result["score"]
#         # sentiment_counts[sentiment] += 1
#     except Exception as e:
#         print(f"Error processing comment: {comment[:50]}... | Error: {e}")
#         sentiment = "neutral"

#     return sentiment

def analyze_sentiment(comment):
    if pd.isna(comment) or not isinstance(comment, str) or comment.strip() == "":
        return "neutral"
    return sentiment_analyzer(comment)[0]['label'].lower()


def preprocess_text(text):
    text = re.sub(r"[^A-Za-z0-9.,!?(){}[\]\"'@#&%+=<>*/-]+", " ", text)
    text = text.lower().strip() 
    if len(text)==0:
        return []
    text_embedding = sbert_model.encode(text, normalize_embeddings=True).tolist()
    return text_embedding