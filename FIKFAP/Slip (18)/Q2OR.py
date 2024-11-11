class UniversityFAQBot:
    def __init__(self):
        self.faqs = {
            "admissions": {
                "What are the admission requirements?": "The admission requirements include a completed application form, transcripts, and standardized test scores.",
                "What is the deadline for applications?": "The application deadline for the fall semester is June 1st.",
                "Is there an application fee?": "Yes, there is a non-refundable application fee of $50."
            },
            "course_registration": {
                "How do I register for classes?": "You can register for classes through the student portal using your university credentials.",
                "What is the registration deadline?": "The registration deadline for the upcoming semester is August 15th.",
                "Can I change my course after registration?": "Yes, you can change your courses during the add/drop period."
            },
            "contact_details": {
                "What is the university's contact number?": "You can reach us at (123) 456-7890.",
                "Where is the admissions office located?": "The admissions office is located in Building A, Room 101.",
                "How can I contact the financial aid office?": "You can email the financial aid office at financialaid@university.edu."
            }
        }

    def get_response(self, category, question):
        if category in self.faqs and question in self.faqs[category]:
            return self.faqs[category][question]
        else:
            return "I'm sorry, I don't have an answer to that question."

    def chat(self):
        print("Welcome to the University FAQ Bot!")
        print("You can ask about 'admissions', 'course registration', or 'contact details'. Type 'exit' to quit.")

        while True:
            category = input("\nPlease enter a category (admissions/course_registration/contact_details): ").strip().lower()
            if category == 'exit':
                print("Thank you for using the University FAQ Bot! Goodbye!")
                break

            if category not in self.faqs:
                print("Invalid category. Please choose from 'admissions', 'course registration', or 'contact details'.")
                continue

            question = input("Please enter your question: ").strip()
            response = self.get_response(category, question)
            print(response)

if __name__ == "__main__":
    bot = UniversityFAQBot()
    bot.chat()