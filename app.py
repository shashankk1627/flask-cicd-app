from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Returns a simple greeting. """
    return 'Hello, World! CI/CD is cool!'

if __name__ == '__main__':
    # Note: Use 0.0.0.0 to make it accessible on your network if running in Docker
    app.run(host='0.0.0.0', port=5000, debug=True)