from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = "HVAC-secret"

def load_equipment():
    with open("data/equipment.json", "r") as f:
        return json.load(f)


def load_labor_rates():
    with open("data/labor_rates.json", "r") as f:
        return json.load(f)


def group_rates_by_job(labor_rates):
    grouped = {}

    for rate in labor_rates:
        job = rate["jobType"]
        level = rate["level"]

        if job not in grouped:
            grouped[job] = []

        grouped[job].append(level)

    return grouped


def get_rate(job_type, job_level, labor_rates):
    return next(
        r for r in labor_rates
        if r["jobType"] == job_type and r["level"] == job_level
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/customer", methods=["POST"])
def customer_submit():
    session["customer"] = {
        "name": request.form.get("name"),
        "propertyType": request.form.get("propertyType"),
        "squareFootage": request.form.get("squareFootage"),
        "systemType": request.form.get("systemType"),
        "phone": request.form.get("phone")
    }

    return redirect("/job")

@app.route("/job")
def job_page():
    customer = session.get("customer")

    labor_rates = load_labor_rates()
    job_map = group_rates_by_job(labor_rates)

    return render_template(
        "job.html",
        customer=customer,
        job_map=job_map
    )

@app.route("/job", methods=["POST"])
def job_submit():
    labor_rates = load_labor_rates()

    job_type = request.form.get("job_type")
    job_level = request.form.get("job_level")

    rate = get_rate(job_type, job_level, labor_rates)

    session["job"] = {
        "jobType": rate["jobType"],
        "level": rate["level"],
        "hourlyRate": rate["hourlyRate"],
        "estimatedHours": rate["estimatedHours"]
    }

    return redirect("/equipment")

@app.route("/equipment")
def equipment_page():
    customer = session.get("customer")
    job = session.get("job")

    if not customer or not job:
        return redirect("/customer")

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

@app.route("/quote")
def quote_page():
    customer = session.get("customer")
    job = session.get("job")
    equipment = session.get("equipment")

    if not customer or not job or not equipment:
        return redirect("/customer")

    equipment_total = sum(
        item.get("baseCost") or item.get("base_cost") or 0
        for item in equipment
    )

    hourly = job["hourlyRate"]
    min_hours = job["estimatedHours"]["min"]
    max_hours = job["estimatedHours"]["max"]

    labor_min = hourly * min_hours
    labor_max = hourly * max_hours

    total_min = equipment_total + labor_min
    total_max = equipment_total + labor_max

    return render_template(
        "quote.html",
        customer=customer,
        job=job,
        equipment=equipment,
        equipment_total=equipment_total,
        labor_min=labor_min,
        labor_max=labor_max,
        total_min=total_min,
        total_max=total_max,
        hourly=hourly,
        min_hours=min_hours,
        max_hours=max_hours
    )

if __name__ == "__main__":
    app.run(debug=True)