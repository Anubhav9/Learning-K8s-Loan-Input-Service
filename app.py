from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def loan_info_home_page():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def get_judgement():
    annual_income=request.form.get("input-annual-income")
    formatted_body={
        "annual_income":annual_income
    }
    response=requests.post(url="http://judgement-service:3012/decide",json=formatted_body)

if __name__ == "__main__":
    app.run(port=2809, host='0.0.0.0')

