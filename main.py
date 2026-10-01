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
    },
    {
        "id": "P004",
        "receiver": "Zarlyn",
        "destination": "Gombak",
        "status": "Pending"
    },
    {
        "id": "P005",
        "receiver": "Adam",
        "destination": "Sungai Besi",
        "status": "In Transit"
    },
    {
        "id": "P006",
        "receiver": "Zuhaira",
        "destination": "Kajang",
        "status": "Delivered"
    },
    {
        "id": "P097",
        "receiver": "Afif Zakwan",
        "destination": "Ke Hati Kamu 💖",
        "status": "Pending"
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
