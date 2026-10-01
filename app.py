from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

parcels = []

# HOMEPAGE

@app.route("/")
def home():
    return render_template("index.html")

# CUSTOMER

@app.route("/customer")
def customer_page():
    query = request.args.get("q", "").strip().upper()

    if not query:
        return render_template(
            "customer.html",
            query="",
            error=None
        )

    parcel = None

    for item in parcels:
        if item.get("id") == query:
            parcel = item
            break

    if parcel is None:
        return render_template(
            "customer.html",
            query=query,
            error="Tracking number not found."
        )

    return redirect(
        url_for(
            "customer_tracking",
            parcel_id=parcel["id"]
        )
    )


@app.route("/customer/<parcel_id>/tracking")
def customer_tracking(parcel_id):
    parcel = None

    for item in parcels:
        if item.get("id") == parcel_id:
            parcel = item
            break

    if parcel is None:
        return redirect(url_for("customer_page"))

    statuses = [
        "Pending",
        "In Transit",
        "Delivered"
    ]

    history = parcel.get("history", [])

    return render_template(
        "customer_tracking.html",
        parcel=parcel,
        statuses=statuses,
        history=history,
        active="tracking"
    )


@app.route("/customer/<parcel_id>/receiver")
def customer_receiver(parcel_id):
    parcel = None

    for item in parcels:
        if item.get("id") == parcel_id:
            parcel = item
            break

    if parcel is None:
        return redirect(url_for("customer_page"))

    return render_template(
        "customer_receiver.html",
        parcel=parcel,
        phone=parcel.get("phone", "-"),
        address=parcel.get("address", "-"),
        active="receiver"
    )


@app.route("/customer/<parcel_id>/details")
def customer_details(parcel_id):
    parcel = None

    for item in parcels:
        if item.get("id") == parcel_id:
            parcel = item
            break

    if parcel is None:
        return redirect(url_for("customer_page"))

    return render_template(
        "customer_details.html",
        parcel=parcel,
        active="details"
    )

# COURIER

courier = {
    "name": "Courier"
}

# COURIER HOME

@app.route("/courier")
def courier_page():

    return render_template(
        "courier.html",
        courier=courier
    )

# GET PARCELS ASSIGNED TO THE COURIER

def get_courier_parcels():
    courier_parcels = []

    for parcel in parcels:
        if parcel.get("courier") == courier["name"]:
            courier_parcels.append(parcel)
    return courier_parcels

# COURIER DASHBOARD

@app.route("/courier-dashboard")
def courier_dashboard():

    courier_parcels = get_courier_parcels()
    total_parcels = len(courier_parcels)
    pending = 0
    in_transit = 0
    delivered = 0

    for parcel in courier_parcels:
        if parcel.get("status") == "Pending":
            pending += 1

        elif parcel.get("status") == "In Transit":
            in_transit += 1

        elif parcel.get("status") == "Delivered":
            delivered += 1

    return render_template(
        "courier_dashboard.html",
        courier=courier,
        total_parcels=total_parcels,
        pending=pending,
        in_transit=in_transit,
        delivered=delivered
    )

# COURIER PARCEL LIST

@app.route("/courier-parcel-list")
def courier_parcel_list():

    courier_parcels = get_courier_parcels()

    return render_template(
        "courier_parcel_list.html",
        courier=courier,
        parcels=courier_parcels
    )

# UPDATE PARCEL STATUS=

@app.route("/update-status/<parcel_id>", methods=["POST"])
def update_status(parcel_id):

    new_status = request.form.get("status")

    for parcel in parcels:
        if (
            parcel.get("id") == parcel_id
            and parcel.get("courier") == courier["name"]
        ):
            parcel["status"] = new_status
            break

    return redirect(
        url_for("courier_parcel_list")
    )

# RUN APPLICATION

if __name__ == "__main__":
    app.run(debug=True)