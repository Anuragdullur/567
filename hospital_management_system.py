from datetime import datetime

class Person:
    def __init__(self, name, age, gender, address, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.contact = contact

class Patient(Person):
    def __init__(self, name, age, gender, address, contact, medical_history=None):
        super().__init__(name, age, gender, address, contact)
        self.medical_history = medical_history if medical_history else []

    def add_medical_record(self, record):
        self.medical_history.append(record)

class Doctor(Person):
    def __init__(self, name, department, contact, specializations=None):
        super().__init__(name, None, None, None, contact)
        self.department = department
        self.specializations = specializations if specializations else []

    def add_specialization(self, specialization):
        self.specializations.append(specialization)

class MedicalRecord:
    def __init__(self, description, date):
        self.description = description
        self.date = date

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class Hospital:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self, patient):
        self.patients[patient.name] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.name] = doctor

    def schedule_appointment(self, patient_name, doctor_name, date, time):
        patient = self.patients.get(patient_name)
        doctor = self.doctors.get(doctor_name)
        if patient and doctor:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            return appointment
        else:
            return None

    def display_appointments(self):
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Time: {appointment.time}")

# Example Usage
if __name__ == "__main__":
    hospital = Hospital("ABC Hospital", "123 Main St", "123-456-7890")

    patient1 = Patient("John Doe", 30, "Male", "456 Elm St", "555-1234")
    patient1.add_medical_record(MedicalRecord("Diagnosed with flu", datetime.now()))
    patient2 = Patient("Jane Smith", 25, "Female", "789 Oak St", "555-5678")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    doctor1 = Doctor("Dr. Smith", "Cardiology", "987-654-3210", ["Heart Surgery", "Angioplasty"])
    doctor2 = Doctor("Dr. Johnson", "Pediatrics", "876-543-2109", ["Immunization", "Pediatric Surgery"])
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    appointment1 = hospital.schedule_appointment("John Doe", "Dr. Smith", "2024-05-10", "10:00 AM")
    appointment2 = hospital.schedule_appointment("Jane Smith", "Dr. Johnson", "2024-05-12", "11:00 AM")

    hospital.display_appointments()
