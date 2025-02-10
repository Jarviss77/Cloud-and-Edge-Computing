from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def echo():
    msg = request.args.get('msg', 'Hello World')
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)