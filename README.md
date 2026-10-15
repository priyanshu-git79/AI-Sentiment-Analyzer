
# AI Sentiment Analyzer

A web application that analyzes text and predicts whether its sentiment is positive or negative using a pretrained AI model.

## Features

- AI-powered sentiment prediction
- Confidence score
- Modern, responsive web interface
- Example reviews and clear button (if implemented)
- Built using Python and Flask

## Technologies Used

- Python
- Flask
- Hugging Face Transformers
- PyTorch
- HTML, CSS, JavaScript

## Installation

1. Clone this repository:

   git clone YOUR_REPOSITORY_URL

2. Open the project folder:

   cd YOUR_REPOSITORY_NAME

3. Create a virtual environment:

   python -m venv venv

4. Activate it on Windows PowerShell:

   .\venv\Scripts\Activate.ps1

5. Install dependencies:

   python -m pip install -r requirements.txt

6. Run the application:

   python app.py

7. Open http://127.0.0.1:5000 in your browser.

## How It Works

The user enters text into the web interface. Flask sends the text to a pretrained sentiment-analysis model, which predicts a positive or negative sentiment and returns a confidence score.

## Author

Priyanshu Kumar
