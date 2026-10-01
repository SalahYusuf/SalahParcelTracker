def customer_menu(parcels):
    while True:
        print("\nCUSTOMER")
        print("1. Track parcel")
        print("2. Back")

        choice = input("Choose: ")

        if choice == "1":
            track_parcel(parcels)

        elif choice == "2":
            break

        else:
            print("Invalid choice.")


def track_parcel(parcels):
    parcel_id = input("Tracking ID: ").upper()
    found = False

    for parcel in parcels:
        if parcel["id"] == parcel_id:
            print("\nPARCEL FOUND")
            print("ID:", parcel["id"])
            print("Receiver:", parcel["receiver"])
            print("Destination:", parcel["destination"])
            print("Status:", parcel["status"])
            found = True

    if found == False:
        print("Parcel not found.")
