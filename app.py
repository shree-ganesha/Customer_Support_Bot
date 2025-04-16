from flask import Flask, render_template, request, jsonify
from rag_pipeline import get_answer,get_retriever

app = Flask(__name__)

# Initialize the retriever once (singleton-style for performance)
retriever = get_retriever()

@app.route('/')
def index():
    """
    Serve the main chatbot UI page.
    """
    return render_template('index.html')


@app.route('/Chatbot', methods=['POST'])
def chatbot():
    """
    Handle chatbot POST requests and return answers from the RAG pipeline.
    """
    try:
        question = request.form['question']
        answer = get_answer(question, retriever)
        return jsonify({'answer': answer})
    except Exception as ex:
        return jsonify({'answer': str(ex)})

if __name__ == '__main__':
    app.run(debug=True)