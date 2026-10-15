
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

print("Loading sentiment analysis model...")
sentiment_analyzer = pipeline("sentiment-analysis")
print("Model loaded successfully!")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            result = sentiment_analyzer(text)[0]

    return render_template(
        "index.html",
        result=result,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=False)
