# online-appointment-booking-system

## Project Description

The Online Appointment Booking System is a web-based application developed using Python Flask and SQLite.

The system allows patients to book appointments with doctors online. Users can enter their personal details, select a doctor, choose an appointment date and time, and provide the reason for the appointment.

The system also provides an appointment management page where booked appointments can be viewed and cancelled.

## Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3


## Features

* Online appointment booking
* Patient information management
* Doctor selection
* Date and time selection
* Appointment reason
* View appointment details
* Cancel appointments
* SQLite database
* Simple and responsive user interface

## Project Structure

```text
online-appointment-booking-system/
│
├── app.py
├── database.py
├── appointments.db
├── templates/
│   ├── index.html
│   └── appointments.html
│
└── README.md
```

## How It Works

### 1. Book Appointment

The user opens the application and enters:

* Patient name
* Email
* Doctor
* Appointment date
* Appointment time
* Reason for appointment

After submitting the form, the information is stored in the SQLite database.

### 2. View Appointments

The user can select **View My Appointments** to see all stored appointments.

### 3. Cancel Appointment

The user can cancel a booked appointment.

Instead of deleting the record permanently, the system changes the appointment status to `Cancelled`.

## Database

The project uses SQLite.

The `appointments` table contains:

| Field            | Description            |
| ---------------- | ---------------------- |
| id               | Unique appointment ID  |
| name             | Patient name           |
| email            | Patient email          |
| doctor           | Selected doctor        |
| appointment_date | Appointment date       |
| appointment_time | Appointment time       |
| reason           | Reason for appointment |
| status           | Booked or Cancelled    |

## Installation

### Step 1: Install Python

Make sure Python is installed.

Check using:

```bash
python --version
```

### Step 2: Install Flask

```bash
pip install flask
```

### Step 3: Run the application

```bash
python app.py
```

### Step 4: Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Sample Workflow

```text
User
  ↓
Open Website
  ↓
Enter Patient Details
  ↓
Select Doctor
  ↓
Select Date & Time
  ↓
Submit Appointment
  ↓
SQLite Database
  ↓
View Appointment
  ↓
Cancel if Required
```

## My Role

I developed the application using Python Flask and SQLite.

My responsibilities included:

* Designing the appointment booking form
* Developing Flask routes
* Creating the SQLite database
* Implementing appointment insertion and retrieval
* Implementing appointment cancellation
* Designing the HTML/CSS user interface
* Connecting the frontend with the backend
* Testing the application

## Project Outcome

The project provides a simple online platform for managing doctor appointments and demonstrates my understanding of:

* Python programming
* Flask framework
* CRUD operations
* SQLite database
* HTML/CSS
* Backend routing
* Form handling
* Database connectivity

## Future Enhancements

* User registration and login
* Admin dashboard
* Doctor login
* Doctor availability management
* Email notifications
* SMS reminders
* Online payment
* Appointment conflict detection
* Search and filter doctors
* Deployment to a cloud platform

## Author

**Your Name**

Online Appointment Booking System — Python Flask Project
