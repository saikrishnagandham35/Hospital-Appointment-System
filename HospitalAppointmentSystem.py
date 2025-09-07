import random 
from datetime import datetime, timedelta

# DECLARATION OF DOCTOR DETAILS
class Doctor:
    def __init__(self, name, specialization, mobile_number):
        self.name = name
        self.specialization = specialization
        self.mobile_number = mobile_number

# PATIENT APPOINTMENT DETAILS
class Appointment:
    def __init__(self, patient_name, mobile_number, age, gender, disease_type, appointment_time):
        self.appointment_number = self.generate_appointment_number()
        self.patient_name = patient_name
        self.mobile_number = mobile_number
        self.age = age
        self.gender = gender
        self.disease_type = disease_type
        self.appointment_time = appointment_time
        self.doctor = None

    # APPOINTMENT NUMBER GENERATOR
    def generate_appointment_number(self):
        return ''.join(random.choices('0123456789', k=6))

    # DISPLAYING OF OUTPUT
    def display_info(self):
        print("\n" + "-"*60)
        print("          APPOINTMENT CONFIRMED          ")
        print("-"*60)
        print("Appointment Details:")
        print(f"  Appointment Number: {self.appointment_number}")
        print(f"  Appointment Time:   {self.appointment_time}\n")
        
        print("Patient Details:")
        print(f"  Name:           {self.patient_name}")
        print(f"  Age:            {self.age}")
        print(f"  Gender:         {self.gender}")
        print(f"  Mobile Number:  {self.mobile_number}")
        print(f"  Ailment:        {self.disease_type}\n")
        
        print("Assigned Doctor:")
        print(f"  Name:           {self.doctor.name}")
        print(f"  Specialization: {self.doctor.specialization}")
        print(f"  Contact:        {self.doctor.mobile_number}")
        print("-"*60 + "\n")

def main():
    # CREATION DOCTORS LIST
    doctor1 = Doctor("Dr. Smith", "Cardiology", "1234567890")
    doctor2 = Doctor("Dr. Johnson", "Pediatrics", "9876543210")
    doctor3 = Doctor("Dr. Williams", "Dermatology", "5555555555")
    doctor4 = Doctor("Dr. Billgates", "Orthopedics", "1111111111")
    doctor5 = Doctor("Dr. Alex", "Gynecology", "2222222222")
    doctor6 = Doctor("Dr. Max", "Neurology", "3333333333")
    doctor7 = Doctor("Dr. Nick", "Ophthalmology", "4444444444")
    doctor8 = Doctor("Dr. Stark", "ENT", "5555555555")
    doctor9 = Doctor("Dr. Chris", "Urology", "6666666666")
    doctor10 = Doctor("Dr. Parker", "Internal Medicine", "7777777777")

    # Doctor Mapping based on disease keywords
    disease_doctor_mapping = {
        "heart": doctor1, "cardiology": doctor1,
        "child": doctor2, "children": doctor2, "pediatrics": doctor2,
        "skin": doctor3, "dermatology": doctor3,
        "bone": doctor4, "joint": doctor4, "orthopedics": doctor4,
        "women's health": doctor5, "gynecology": doctor5,
        "brain": doctor6, "nervous system": doctor6, "neurology": doctor6,
        "eye": doctor7, "ophthalmology": doctor7,
        "ent": doctor8, "ear": doctor8, "nose": doctor8, "throat": doctor8,
        "urinary": doctor9, "urology": doctor9,
        "general": doctor10, "checkup": doctor10, "internal medicine": doctor10
    }

    # User information with input validation
    patient_name = input("Enter patient name: ")
    
    while True:
        try:
            age = int(input("Enter patient age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")

    gender = input("Enter patient gender: ")

    while True:
        try:
            mobile_number = input("Enter patient mobile number: ")
            int(mobile_number)
            if len(mobile_number) == 10:
                break
            else:
                print("Please enter a valid 10-digit mobile number.")
        except ValueError:
            print("Invalid input. Please enter numbers only for the mobile number.")
            
    disease_type = input("Describe your health issue (e.g., 'heart pain', 'skin problem'): ").lower()

    # Find the correct doctor
    assigned_doctor = None
    for keyword, doctor in disease_doctor_mapping.items():
        if keyword in disease_type:
            assigned_doctor = doctor
            break
    
    # If no specialist is found, assign a general doctor
    if not assigned_doctor:
        assigned_doctor = doctor10 

    # Appointment Date and Time Generation
    tomorrow = datetime.now() + timedelta(days=1)
    hour = random.randint(10, 18)
    minute = random.choice([0, 15, 30, 45])
    appointment_datetime = tomorrow.replace(hour=hour, minute=minute, second=0, microsecond=0)
    appointment_time = appointment_datetime.strftime("%Y-%m-%d %I:%M %p")

    # CREATE AND DISPLAY APPOINTMENT
    appointment = Appointment(patient_name, mobile_number, age, gender, disease_type, appointment_time)
    appointment.doctor = assigned_doctor
    appointment.display_info()

    # CONFIRMATION OF THE APPOINTMENT
    confirm = input("Would you like to confirm this appointment? (yes/no): ").lower()
    
    if confirm == 'yes' or confirm == 'y':
        print("\nThank you! Your appointment is confirmed.")
    else:
        print("\nAppointment cancelled. Please run the program again to reschedule.")

# Run the main function
if __name__ == "__main__":
    main()