import sqlite3

DATABASE = "appointments.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            doctor TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            reason TEXT,
            status TEXT DEFAULT 'Booked'
        )
    """)

    connection.commit()
    connection.close()


def add_appointment(name, email, doctor, date, time, reason):
    connection = get_connection()

    connection.execute("""
        INSERT INTO appointments
        (name, email, doctor, appointment_date, appointment_time, reason)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, doctor, date, time, reason))

    connection.commit()
    connection.close()


def get_appointments():
    connection = get_connection()

    appointments = connection.execute("""
        SELECT * FROM appointments
        ORDER BY appointment_date, appointment_time
    """).fetchall()

    connection.close()

    return appointments


def cancel_appointment(appointment_id):
    connection = get_connection()

    connection.execute("""
        UPDATE appointments
        SET status = 'Cancelled'
        WHERE id = ?
    """, (appointment_id,))

    connection.commit()
    connection.close()
