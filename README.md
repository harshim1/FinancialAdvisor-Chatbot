# Smart Financial Advisor Chatbot

A personalized financial advisor chatbot built with Flask. It can help you with budgeting, saving, investing, and debt advice.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## Features

- Basic NLP-based keyword matcher
- Flask backend and HTML frontend
- Easy to expand with ML models or financial APIs

## Future Ideas

- Integrate OpenAI API for natural conversation
- Use user financial history for tailored advice
- Deploy to AWS or render.com

## OpenAI Integration

This bot uses OpenAI's GPT-3.5 to give personalized financial advice.

### Setup Instructions

1. [Get your OpenAI API key](https://platform.openai.com/account/api-keys)
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```
3. Run the app as usual:
   ```bash
   python app.py
   ```
