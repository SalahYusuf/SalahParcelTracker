def courier_menu(parcels):
    while True:
        print("\nCOURIER")
        print("1. Dashboard")
        print("2. Parcel list")
        print("3. Update status")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            dashboard(parcels)

        elif choice == "2":
            parcel_list(parcels)

        elif choice == "3":
            update_status(parcels)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def dashboard(parcels):
    pending = 0
    transit = 0
    delivered = 0

    for parcel in parcels:
        if parcel["status"] == "Pending":
            pending += 1

        elif parcel["status"] == "In Transit":
            transit += 1

        elif parcel["status"] == "Delivered":
            delivered += 1

    print("\nDASHBOARD")
    print("Total:", len(parcels))
    print("Pending:", pending)
    print("In Transit:", transit)
    print("Delivered:", delivered)


def parcel_list(parcels):
    print("\nPARCEL LIST")

    for parcel in parcels:
        print(
            parcel["id"],
            "-",
            parcel["receiver"],
            "-",
            parcel["status"]
        )


def update_status(parcels):
    parcel_id = input("Tracking ID: ").upper()
    found = False

    for parcel in parcels:
        if parcel["id"] == parcel_id:
            found = True

            print("1. Pending")
            print("2. In Transit")
            print("3. Delivered")

            choice = input("New status: ")

            if choice == "1":
                parcel["status"] = "Pending"

            elif choice == "2":
                parcel["status"] = "In Transit"

            elif choice == "3":
                parcel["status"] = "Delivered"

            else:
                print("Invalid choice.")
                return

            print("Status updated.")

    if found == False:
        print("Parcel not found.")
