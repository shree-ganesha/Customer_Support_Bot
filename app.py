from flask import Flask, render_template, request, jsonify
from rag_pipeline import get_answer,get_retriever

app = Flask(__name__)

retriever = get_retriever()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Chatbot', methods=['POST'])
def ask():
    try:
        question = request.form['question']
        answer = get_answer(question, retriever)
        return jsonify({'answer': answer})
    except Exception as ex:
        return jsonify({'answer': str(ex)})

if __name__ == '__main__':
    app.run(debug=True)