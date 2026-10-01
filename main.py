from customer import customer_menu
from courier import courier_menu


# --------------------------------------------
# SHARED PARCEL DATA
# --------------------------------------------

parcels = [
    {
        "id": "P001",
        "receiver": "Salah",
        "phone": "012-3456789",
        "address": "Cyberjaya, Selangor",
        "courier": "Courier",
        "origin": "Shah Alam",
        "destination": "Cyberjaya",
        "status": "Pending",
        "weight": "1.2 kg",
        "contents": "Clothing",
        "service": "Standard Delivery",
    },
    {
        "id": "P002",
        "receiver": "Mikail",
        "phone": "013-4567890",
        "address": "Putrajaya",
        "courier": "Courier",
        "origin": "Kuala Lumpur",
        "destination": "Putrajaya",
        "status": "In Transit",
        "weight": "2.0 kg",
        "contents": "Books",
        "service": "Express Delivery",
    },
    {
        "id": "P003",
        "receiver": "Aleesya",
        "phone": "014-5678901",
        "address": "Shah Alam, Selangor",
        "courier": "Courier",
        "origin": "Seremban",
        "destination": "Shah Alam",
        "status": "Delivered",
        "weight": "0.8 kg",
        "contents": "Accessories",
        "service": "Standard Delivery",
    },
    {
        "id": "P004",
        "receiver": "Adam",
        "phone": "015-6789012",
        "address": "Bangi, Selangor",
        "courier": "Courier",
        "origin": "Kajang",
        "destination": "Bangi",
        "status": "In Transit",
        "weight": "3.5 kg",
        "contents": "Electronics",
        "service": "Express Delivery",
    },
]


def line():
    print("=" * 55)


def homepage():
    while True:
        print("\n")
        line()
        print("               SALAH PARCEL TRACKER")
        line()
        print("1. Customer")
        print("2. Courier")
        print("3. Exit")
        line()

        choice = input("Choose your role: ").strip()

        if choice == "1":
            customer_menu(parcels)

        elif choice == "2":
            courier_menu(parcels)

        elif choice == "3":
            print("\nThank you for using Salah Parcel Tracker.")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    homepage()
