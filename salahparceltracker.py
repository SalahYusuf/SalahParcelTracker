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


print("PARCEL TRACKER")
print("1. Customer")
print("2. Courier")

choice = input("Choose: ")


if choice == "1":
    parcel_id = input("Tracking ID: ")

    for parcel in parcels:
        if parcel["id"] == parcel_id:
            print("ID:", parcel["id"])
            print("Receiver:", parcel["receiver"])
            print("Destination:", parcel["destination"])
            print("Status:", parcel["status"])


elif choice == "2":
    print("1. Parcel List")
    print("2. Update Status")

    courier_choice = input("Choose: ")

    if courier_choice == "1":
        for parcel in parcels:
            print(parcel["id"], parcel["receiver"], parcel["status"])

    elif courier_choice == "2":
        parcel_id = input("Tracking ID: ")

        for parcel in parcels:
            if parcel["id"] == parcel_id:
                new_status = input("New status: ")
                parcel["status"] = new_status
                print("Status updated.")

