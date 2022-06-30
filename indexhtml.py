
from flask import Flask, request, abort, send_file


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def webhook2():
    return send_file('index.html')

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8001')

