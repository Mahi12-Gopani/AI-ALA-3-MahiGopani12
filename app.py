from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "exit" in user_input:
        return "Thank you for chatting! Goodbye."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm fully operational! How about you?"
    elif "your name" in user_input:
        return "I am called the Python Professional Chatbot."
    elif "help" in user_input:
        return "You can ask me about Python programming, tech concepts, general knowledge, or even quiz questions."
    elif "python" in user_input and ("work" in user_input or "how" in user_input):
        return "Python works by interpreting code line-by-line using the Python interpreter."
    elif "python" in user_input and ("advantages" in user_input or "benefits" in user_input):
        return "Python advantages include simplicity, readability, vast libraries, cross-platform compatibility, and strong community support."
    elif "python" in user_input and ("uses" in user_input or "applications" in user_input):
        return "Python is used in web development, data science, automation, artificial intelligence, scientific computing, and more."
    elif "python" in user_input and ("version" in user_input or "latest" in user_input):
        return "As of now, Python 3.11 is the latest stable version."
    elif "what is a variable" in user_input:
        return "A variable is a storage location identified by a name that holds data."
    elif "what is a function" in user_input:
        return "A function is a block of reusable code that performs a specific task."
    elif "what is object oriented programming" in user_input:
        return "OOP bundles data and functions into objects, promoting modularity and reuse."
    elif "what is artificial intelligence" in user_input:
        return "AI is about creating systems that can perform tasks usually requiring human intelligence."
    elif "what is machine learning" in user_input:
        return "ML is a subset of AI where systems learn patterns from data to make predictions."
    elif "what is data science" in user_input:
        return "Data Science extracts insights from structured and unstructured data."
    elif "capital of france" in user_input:
        return "The capital of France is Paris."
    elif "who is the president of the united states" in user_input:
        return "The current president of the United States is Joe Biden."
    elif "who discovered gravity" in user_input:
        return "Sir Isaac Newton is credited with discovering gravity."
    elif "what is the speed of light" in user_input:
        return "The speed of light is ~299,792 km/s."
    else:
        return "Sorry, I didn't quite catch that. Can you please rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
