class Hospital:
    def __init__(self):
        # Initialize the patients attribute as an empty dictionary
        self.patients = {}

    def add_patient(self, name, age, disease):
        # Add patient details to the patients dictionary
        self.patients[name] = {'age': age, 'disease': disease}

    def view_patient(self, name):
        # View patient details
        if name in self.patients:
            print(f"Patient Name: {name}")
            print(f"Age: {self.patients[name]['age']}")
            print(f"Disease: {self.patients[name]['disease']}")
        else:
            print("Patient not found.")

    def delete_patient(self, name):
        # Delete a patient from the records
        if name in self.patients:
            del self.patients[name]
            print(f"Patient {name} has been deleted.")
        else:
            print("Patient not found.")

# Driver code
hospital = Hospital()

while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. View Patient")
    print("3. Delete Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter patient disease: ")
        hospital.add_patient(name, age, disease)
    elif choice == '2':
        name = input("Enter patient name to view: ")
        hospital.view_patient(name)
    elif choice == '3':
        name = input("Enter patient name to delete: ")
        hospital.delete_patient(name)
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")