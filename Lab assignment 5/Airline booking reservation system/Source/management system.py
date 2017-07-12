import random      #Imported random function

letters = 'Random letters from A-Z'      #Letters are included as from A to Z for including seat number


class BookingCategory:             #Booking category has been mentioned rither Economy or first class
    ECONOMY = 'Eco'
    FIRSTCLASS = 'Firstclass'


class Seat:                #Seat number:- Row and seat information in terms of integer and string
    def __init__(self, row: int, letter: str):
        self.rownumber = row
        self.letter = letter

    def __str__(self):       #Returns seat information
        return '{}{}'.format(self.rownumber, self.letter)


class Seatingspace:            #Seating information called by class, row and remaining seats
    def __init__(self, book_class: str, start_row: int, row_count: int, seats_per_row: int):
        self.booking_class = book_class
        self.seat_count = row_count * seats_per_row
        self.seats_remaining = []

        for rownumber in range(start_row, row_count + start_row):
            for seat_number in range(seats_per_row):
                new_seat = Seat(rownumber, letters[seat_number])
                self.seats_remaining.append(new_seat)


class Flight:           #Tells flight information about seating space and class category passenger chosen
    def __init__(self, economy_seats: Seatingspace, firstclass_seats: Seatingspace):
        self.seating_areas = {
            BookingCategory.ECONOMY: economy_seats,
            BookingCategory.FIRSTCLASS: firstclass_seats}

    def print_statistics(self):       #Function created to display available seats in both Economical and First class category
        for booking_class, seating_area in self.seating_areas.items():
            print('{}: {}% is available'.format(booking_class,
                len(seating_area.seats_remaining) / seating_area.seat_count * 100))

    def remaining_seat_count(self, booking_class: str):   #Displays remaining seats by booking class
        return len(self.seating_areas[booking_class].seats_remaining)

    def get_seat(self, booking_class: str):
        return self.seating_areas[booking_class].seats_remaining.pop()


class Passenger:  #Class is defined to get passenger information such as name, booking id, seat information
    def __init__(self, name: str):
        self.name = name
        self.booking_id = None
        self.seat = None

    def flighthas_booked(self):   #If flight is not booked then returns value by booking id and doesnt show any booking record under it
        return self.booking_id is not None

    def book(self, flight: Flight, booking_class: str):
        if flight.remaining_seat_count(booking_class) != 0:
            self.seat = flight.get_seat(booking_class)
            self.booking_id = random.Random().randrange(500, 5000)  #Random value of booking id in range mentioned
            return True

        return False


def main():    #super data member isi used to call all values and pass arguments. Instances has been created for each information mentioned above
    business = Seatingspace(BookingCategory.FIRSTCLASS, start_row=1, row_count=5, seats_per_row=4)
    economy = Seatingspace(BookingCategory.ECONOMY, start_row=6, row_count=20, seats_per_row=6)

    flight = Flight(economy, business)

    Mandar = Passenger('Mandar')
    Mandar.book(flight, BookingCategory.ECONOMY)
    print("Mandar's booking seat:")
    print(Mandar.seat)
    print("Mandar's booking ID:")
    print(Mandar.booking_id)
    print("Seat availability:")

    flight.print_statistics()


if __name__ == '__main__':           #Values of super data member is passed by calling its method
    main()