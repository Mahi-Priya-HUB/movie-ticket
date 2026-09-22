

import json
from datetime import datetime

movies = [
    {
        "id": 1,
        "name": "Avengers",
        "language": "English",
        "price": 200,
        "shows": ["10:00 AM", "2:00 PM", "6:00 PM"]
    },
    {
        "id": 2,
        "name": "3 Idiots",
        "language": "Hindi",
        "price": 150,
        "shows": ["11:00 AM", "3:00 PM", "7:00 PM"]
    },
    {
        "id": 3,
        "name": "Inception",
        "language": "English",
        "price": 250,
        "shows": ["9:00 AM", "1:00 PM", "8:00 PM"]
    }
]

try:
    with open("bookings.json", "r") as file:
        bookings = json.load(file)
except:
    bookings = []


def show_movies():
    print("\nAvailable Movies")

    for movie in movies:
        print("\nID:", movie["id"])
        print("Movie:", movie["name"])
        print("Language:", movie["language"])
        print("Price: Rs.", movie["price"])
        print("Shows:", ", ".join(movie["shows"]))


def book_ticket():
    show_movies()

    try:
        movie_id = int(input("\nEnter movie id: "))
    except:
        print("Please enter a number.")
        return

    movie = None

    for m in movies:
        if m["id"] == movie_id:
            movie = m
            break

    if movie is None:
        print("Movie not found.")
        return

    print("\nShows available:")

    for i in range(len(movie["shows"])):
        print(i + 1, movie["shows"][i])

    try:
        show_number = int(input("Select show: "))
        show = movie["shows"][show_number - 1]
    except:
        print("Invalid show.")
        return

    print("\nSeats:")
    print("A1 A2 A3 A4 A5")
    print("B1 B2 B3 B4 B5")
    print("C1 C2 C3 C4 C5")

    seat_input = input("Enter seats separated by comma: ")
    seats = seat_input.upper().replace(" ", "").split(",")

    all_seats = [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5"
    ]

    for seat in seats:
        if seat not in all_seats:
            print("Invalid seat:", seat)
            return

    for booking in bookings:
        if booking["movie"] == movie["name"] and booking["show"] == show:
            for seat in seats:
                if seat in booking["seats"]:
                    print(seat, "is already booked.")
                    return

    name = input("Enter your name: ")

    total = len(seats) * movie["price"]

    if len(bookings) == 0:
        booking_id = 1
    else:
        booking_id = bookings[-1]["id"] + 1

    booking = {
        "id": booking_id,
        "name": name,
        "movie": movie["name"],
        "show": show,
        "seats": seats,
        "total": total,
        "date": str(datetime.now())
    }

    bookings.append(booking)

    with open("bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)

    print("\nTicket booked successfully!")
    print("Booking ID:", booking["id"])
    print("Name:", name)
    print("Movie:", movie["name"])
    print("Show:", show)
    print("Seats:", ", ".join(seats))
    print("Total amount: Rs.", total)


def view_bookings():
    if len(bookings) == 0:
        print("\nNo bookings found.")
        return

    print("\nYour Bookings")

    for booking in bookings:
        print("\nBooking ID:", booking["id"])
        print("Name:", booking["name"])
        print("Movie:", booking["movie"])
        print("Show:", booking["show"])
        print("Seats:", ", ".join(booking["seats"]))
        print("Amount: Rs.", booking["total"])


def cancel_ticket():
    if len(bookings) == 0:
        print("\nNo bookings found.")
        return

    try:
        booking_id = int(input("Enter booking ID: "))
    except:
        print("Invalid ID.")
        return

    for booking in bookings:
        if booking["id"] == booking_id:
            bookings.remove(booking)

            with open("bookings.json", "w") as file:
                json.dump(bookings, file, indent=4)

            print("Booking cancelled.")
            return

    print("Booking not found.")


while True:
    print("\n==============================")
    print("     MOVIE TICKET BOOKING")
    print("==============================")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        cancel_ticket()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Wrong choice.")

