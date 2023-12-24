from src import create_app
from flask import Flask, render_template

app = create_app()


@app.route('/')
def hello_world():
    # return 'Hello! welcome to home page for stock viz app'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
