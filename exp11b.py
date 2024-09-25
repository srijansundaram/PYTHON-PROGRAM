# Base class
class Passenger:
    def __init__(self, name, passenger_id):
        self.name = name                # Name of the passenger
        self.passenger_id = passenger_id  # Unique ID for the passenger

    def display_info(self):
        """Display information about the passenger."""
        return f"Name: {self.name}\nPassenger ID: {self.passenger_id}"

# Subclass for Regular Passengers
class RegularPassenger(Passenger):
    def __init__(self, name, passenger_id, seat_number):
        super().__init__(name, passenger_id)  # Call to the base class constructor
        self.seat_number = seat_number          # Seat number assigned to the passenger

    def display_info(self):
        """Display information about the regular passenger."""
        base_info = super().display_info()  # Get base class info
        return f"{base_info}\nSeat Number: {self.seat_number}"

# Subclass for Senior Citizens
class SeniorCitizen(RegularPassenger):
    def __init__(self, name, passenger_id, seat_number, discount):
        super().__init__(name, passenger_id, seat_number)  # Call to the base class constructor
        self.discount = discount                     # Discount percentage for senior citizens

    def display_info(self):
        """Display information about the senior citizen passenger."""
        base_info = super().display_info()  # Get base class info
        return f"{base_info}\nSeat Number: {self.seat_number}\nDiscount: {self.discount}%"

# Main function to demonstrate the classes
def main():
    # Create instances of RegularPassenger and SeniorCitizen
    regular_passenger = RegularPassenger("Alice Smith", "REG123", "12A")
    senior_citizen = SeniorCitizen("John Doe", "SEN456", "5B", 20)

    # Display information about each passenger
    print("Regular Passenger Information:")
    print(regular_passenger.display_info())
    print("\nSenior Citizen Information:")
    print(senior_citizen.display_info())

if __name__ == "__main__":
    main()
