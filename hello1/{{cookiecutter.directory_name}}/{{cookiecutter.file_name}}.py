from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1> Hello my beloved {{ cookiecutter.greeting_recipient }} </h1>"


if __name__ == '__main__':
    app.run(host="{{cookiecutter.host}}", port="{{cookiecutter.port}}", debug={{cookiecutter.debug_mode}})
