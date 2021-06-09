from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/foo/<language>', methods=['POST']) 
def foo(language):
    corpus = request.json
    corpus.update({"language":language})
    return jsonify(corpus)


if __name__ == "__main__":
    app.run()
