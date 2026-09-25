from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_appointment, get_appointments, cancel_appointment

app = Flask(__name__)

# Create database and table
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    email = request.form["email"]
    doctor = request.form["doctor"]
    date = request.form["date"]
    time = request.form["time"]
    reason = request.form["reason"]

    add_appointment(name, email, doctor, date, time, reason)

    return redirect(url_for("appointments"))


@app.route("/appointments")
def appointments():
    data = get_appointments()
    return render_template("appointments.html", appointments=data)


@app.route("/cancel/<int:appointment_id>")
def cancel(appointment_id):
    cancel_appointment(appointment_id)
    return redirect(url_for("appointments"))


if __name__ == "__main__":
    app.run(debug=True)
