from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def loan_info_home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=2809, host='0.0.0.0')
