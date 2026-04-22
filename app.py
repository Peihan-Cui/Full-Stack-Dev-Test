from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = "HVAC-secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/customer", methods=["POST"])
def customer_submit():
    customer = {
        "name": request.form.get("name"),
        "propertyType": request.form.get("propertyType"),
        "squareFootage": request.form.get("squareFootage"),
        "systemType": request.form.get("systemType"),
        "phone": request.form.get("phone")
    }

    session["customer"] = customer
    return redirect("/job")

@app.route("/job")
def job_page():
    customer = session.get("customer")
    return render_template("job.html", customer=customer)

if __name__ == '__main__':
    app.run(debug=True)