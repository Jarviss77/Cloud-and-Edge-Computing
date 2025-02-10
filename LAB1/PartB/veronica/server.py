from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Echo API</title>
</head>
<body>
    <h2>Enter a Message</h2>
    <form action="/result" method="GET">
        <input type="text" name="msg">
        <input type="submit" value="Send">
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_FORM)

@app.route('/result')
def result():
    msg = request.args.get('msg', 'Hello World')
    rest_server_ip = "10.20.20.127"
    response = requests.get(f'http://{rest_server_ip}:5000/echo?msg={msg}')
    return f"<h2>Response from API: {response.text}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)