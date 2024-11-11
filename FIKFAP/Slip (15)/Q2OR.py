class RestaurantReservationAssistant:
    def __init__(self):
        self.menu = {
            "Pasta": 12.99,
            "Burger": 10.99,
            "Salad": 8.99,
            "Steak": 19.99,
            "Dessert": 5.99
        }
        self.reservations = []

    def show_menu(self):
        print("Here is our menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def make_reservation(self, name, date, time, guests):
        reservation = {
            'name': name,
            'date': date,
            'time': time,
            'guests': guests
        }
        self.reservations.append(reservation)
        print(f"Reservation confirmed for {name} on {date} at {time} for {guests} guests.")

    def chat(self):
        print("Welcome to the Restaurant Reservation Assistant!")
        
        while True:
            user_input = input("\nHow can I assist you today? (Type 'menu' to see the menu, 'reserve' to make a reservation, or 'exit' to quit): ").strip().lower()

            if user_input == 'menu':
                self.show_menu()
            elif user_input == 'reserve':
                name = input("Please enter your name: ")
                date = input("Enter the reservation date (YYYY-MM-DD): ")
                time = input("Enter the reservation time (HH:MM): ")
                guests = input("Enter the number of guests: ")

                try:
                    guests = int(guests)
                    if guests <= 0:
                        raise ValueError("Number of guests must be positive.")
                    self.make_reservation(name, date, time, guests)
                except ValueError as e:
                    print(f"Invalid input: {e}")
            elif user_input == 'exit':
                print("Thank you for using the Restaurant Reservation Assistant! Goodbye!")
                break
            else:
                print("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    assistant = RestaurantReservationAssistant()
    assistant.chat()

    