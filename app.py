from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
openai.api_key = "your_openai_api_key"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({"error": "Query is required"}), 400
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_query}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
