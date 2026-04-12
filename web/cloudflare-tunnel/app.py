from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello from Termux!</h1><p>Your Flask server is running.</p>'

if __name__ == '__main__':
    # We use 0.0.0.0 so it's accessible on your local network
    app.run(host='0.0.0.0', port=5000)
