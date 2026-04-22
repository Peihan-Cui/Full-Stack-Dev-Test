from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = "HVAC-secret"

def load_equipment():
  with open("data/equipment.json", "r") as f:
    return json.load(f)

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

@app.route("/job", methods=["POST"])
def job_submit():
  session["job"] = {
    "job_type": request.form.get("job_type"),
    "job_level": request.form.get("job_level")
  }
  return redirect("/equipment")

@app.route("/equipment")
def equipment_page():
  customer = session.get("customer")
  job = session.get("job")

  equipment_data = load_equipment()

  return render_template(
    "equipment.html",
    equipment=equipment_data,
    customer=customer,
    job=job
  )

@app.route("/equipment", methods=["POST"])
def equipment_submit():
  selected_ids = request.form.getlist("equipment")

  equipment_data = load_equipment()

  selected = [
    item for item in equipment_data
    if item["id"] in selected_ids
  ]

  session["equipment"] = selected

  return redirect("/quote")

if __name__ == '__main__':
    app.run(debug=True)