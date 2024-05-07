import unittest
from hospital_management_system import Patient, Doctor, Hospital, MedicalRecord, Appointment
from datetime import datetime

class TestHospitalManagementSystem(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital("ABC Hospital", "123 Main St", "123-456-7890")

        self.patient1 = Patient("John Doe", 30, "Male", "456 Elm St", "555-1234")
        self.patient2 = Patient("Jane Smith", 25, "Female", "789 Oak St", "555-5678")
        self.hospital.add_patient(self.patient1)
        self.hospital.add_patient(self.patient2)

        self.doctor1 = Doctor("Dr. Smith", "Cardiology", "987-654-3210", ["Heart Surgery", "Angioplasty"])
        self.doctor2 = Doctor("Dr. Johnson", "Pediatrics", "876-543-2109", ["Immunization", "Pediatric Surgery"])
        self.hospital.add_doctor(self.doctor1)
        self.hospital.add_doctor(self.doctor2)

        self.appointment1 = self.hospital.schedule_appointment("John Doe", "Dr. Smith", "2024-05-10", "10:00 AM")
        self.appointment2 = self.hospital.schedule_appointment("Jane Smith", "Dr. Johnson", "2024-05-12", "11:00 AM")

    def test_patient_creation(self):
        self.assertEqual(self.patient1.name, "John Doe")
        self.assertEqual(self.patient1.age, 30)
        self.assertEqual(self.patient1.gender, "Male")
        self.assertEqual(self.patient1.address, "456 Elm St")
        self.assertEqual(self.patient1.contact, "555-1234")

    def test_doctor_creation(self):
        self.assertEqual(self.doctor1.name, "Dr. Smith")
        self.assertEqual(self.doctor1.department, "Cardiology")
        self.assertEqual(self.doctor1.contact, "987-654-3210")
        self.assertListEqual(self.doctor2.specializations, ["Immunization", "Pediatric Surgery"])

    def test_hospital_creation(self):
        self.assertEqual(self.hospital.name, "ABC Hospital")
        self.assertEqual(self.hospital.address, "123 Main St")
        self.assertEqual(self.hospital.contact, "123-456-7890")

    def test_schedule_appointment(self):
        self.assertEqual(self.appointment1.patient.name, "John Doe")
        self.assertEqual(self.appointment1.doctor.name, "Dr. Smith")
        self.assertEqual(self.appointment1.date, "2024-05-10")
        self.assertEqual(self.appointment1.time, "10:00 AM")

        self.assertEqual(self.appointment2.patient.name, "Jane Smith")
        self.assertEqual(self.appointment2.doctor.name, "Dr. Johnson")
        self.assertEqual(self.appointment2.date, "2024-05-12")
        self.assertEqual(self.appointment2.time, "11:00 AM")

    def test_add_medical_record(self):
        medical_record = MedicalRecord("Routine Checkup", datetime.now())
        self.patient1.add_medical_record(medical_record)
        self.assertEqual(len(self.patient1.medical_history), 1)
        self.assertEqual(self.patient1.medical_history[0].description, "Routine Checkup")

if __name__ == "__main__":
    unittest.main()
