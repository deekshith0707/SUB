from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Deek!</h1>"


@app.route('/about')
def about():
    return "<h1>About Me</h1><p>My name is Deeksith P Kumar From Hassan.</p>"

@app.route('/contact')
def contact():
    return "<h1>Contact me</h1><p>Email: deekshipkss@gmail.com</p>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to the Deek! platform.</p>"

@app.route('/status')
def status():
    return "<h1>Status: Running</h1>"

@app.route('/products')
def products():
    return "<h1>Products</h1><ul><li>CI/CD Tools</li><li>Monitoring Tools</li><li>Automation Tools</li></ul>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
