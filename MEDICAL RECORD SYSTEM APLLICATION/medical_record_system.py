class MedicalRecordSystem:
    def __init__(self):
        self.patient = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patient.append(patient)
        return self.patient

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        return self.doctors
