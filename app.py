from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/code_registration")
def code_registration():
    return render_template('code_registration.html')


@app.route("/welcome")
def welcome():
    return render_template('welcome.html')


@app.route("/api/protected_api", methods=["POST"])
def protected_api():
    return 'some protected data from api'


if __name__ == '__main__':
    app.run(debug=True)
