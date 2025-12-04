from flask import Flask, render_template

meow = Flask(__name__)

@meow.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    meow.run(debug=True)