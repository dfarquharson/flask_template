from flask import Flask

app = Flask(__name__)


@app.route('/up', methods=['GET'])
def up():
    return "Hello, World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
