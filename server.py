from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if "__main__" == __name__:
    app.run(debug=False, port=8085, host='0.0.0.0')