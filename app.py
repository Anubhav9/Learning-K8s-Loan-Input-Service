from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def loan_info_home_page():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def get_judgement():
    # Get input from the form
    annual_income = request.form.get("input-annual-income")

    # Validate input
    if not annual_income or not annual_income.isdigit():
        return {"error": "Invalid or missing input-annual-income parameter"}, 400

    # Prepare the payload for judgement-service
    formatted_body = {
        "input-annual-income": annual_income  # Match the key expected by judgement-service
    }

    try:
        # Send POST request to the judgement-service
        response = requests.post(
            url="http://judgement-service:3012/decide",
            json=formatted_body,  # Send payload as JSON
            timeout=5  # Optional timeout to prevent hanging
        )

        # Handle the response from judgement-service
        if response.status_code == 200:
            return response.text  # Rendered HTML returned by judgement-service
        else:
            return {
                "error": f"Judgement-service returned an error: {response.status_code}"
            }, response.status_code

    except requests.exceptions.RequestException as e:
        # Handle network errors gracefully
        return {"error": f"Failed to reach judgement-service: {str(e)}"}, 500


if __name__ == "__main__":
    app.run(port=2809, host='0.0.0.0')
    


