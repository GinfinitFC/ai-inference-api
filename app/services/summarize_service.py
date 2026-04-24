from transformers import pipeline

# load once (important for performance)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str):
    if len(text.split()) < 30:
        return {
            "summary": text,
            "note": "Text too short to summarize effectively"
        }

    result = summarizer(text, max_length=130, min_length=30, do_sample=False)

    return {
        "summary": result[0]["summary_text"]
    }