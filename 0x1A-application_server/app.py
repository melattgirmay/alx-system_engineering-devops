from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define more routes and functionality here if needed

if __name__ == '__main__':
    app.run()

