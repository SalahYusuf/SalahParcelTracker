from customer import customer_menu
from courier import courier_menu


parcels = [
    {
        "id": "P001",
        "receiver": "Salah",
        "destination": "Cyberjaya",
        "status": "Pending"
    },
    {
        "id": "P002",
        "receiver": "Mikail",
        "destination": "Putrajaya",
        "status": "In Transit"
    },
    {
        "id": "P003",
        "receiver": "Aleesya",
        "destination": "Shah Alam",
        "status": "Delivered"
    }
]


while True:
    print("\nPARCEL TRACKER")
    print("1. Customer")
    print("2. Courier")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        customer_menu(parcels)

    elif choice == "2":
        courier_menu(parcels)

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
