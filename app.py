from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/up', methods=['GET'])
def up():
    return rjson({'status': 'happy'})


def rjson(blob, statcode=200):
    return Response(json.dumps(blob), mimetype='application/json',
                    status=statcode)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
