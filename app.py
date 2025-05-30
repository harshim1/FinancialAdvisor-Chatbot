from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Make sure to set your OpenAI API key in the environment variable before running the app
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable financial advisor. Provide clear, personalized advice on budgeting, saving, investing, and managing debt."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "There was an error processing your request. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)