def chatbot():
    print("Hello! I am your Healthcare Appointment Bot.")
    print("I can help you book appointments and provide clinic information.")

    while True:
        print("\nHow can I assist you today?")
        print("1. Book an appointment")
        print("2. Find clinic information")
        print("3. Exit")

        choice = input("Please enter your choice (1, 2, or 3): ")

        if choice == '1':
            book_appointment()
        elif choice == '2':
            clinic_information()
        elif choice == '3':
            print("Thank you for using Healthcare Appointment Bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def book_appointment():
    print("\nLet's book an appointment.")
    patient_name = input("Enter your name: ")
    date = input("Enter your preferred date (YYYY-MM-DD): ")
    time = input("Enter your preferred time (HH:MM): ")

    
    print(f"Thank you, {patient_name}. Your appointment is booked on {date} at {time}.")

def clinic_information():
    print("\nHere is the clinic information:")
    print("Clinic Hours: 9 AM to 5 PM, Monday to Friday.")
    print("Location: 123 Health St., Wellness City.")
    print("Contact: (123) 456-7890")

if __name__ == "__main__":
    chatbot()