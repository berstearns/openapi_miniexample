from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/foo/<language>', methods=['POST']) 
def foo(language):
    corpus = request.json
    return jsonify(corpus)
