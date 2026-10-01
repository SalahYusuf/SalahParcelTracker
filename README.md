# Salah Parcel Tracker — Split Terminal Version

This version is intentionally split into three Python files so each team member can work on a separate Git branch.

## Files

- `main.py`
  - Homepage / main menu
  - Shared parcel data
  - Connects Customer and Courier modules

- `customer.py`
  - Customer menu
  - Track parcel
  - Tracking status
  - Receiver information
  - Parcel details

- `courier.py`
  - Courier menu
  - Dashboard
  - Parcel list
  - Update parcel status

## Run

From the project folder:

```bash
python3 main.py
```

No framework or external library is required.

## Suggested branches

- `homepage` → Salah works on `main.py`
- `customer` → Mikail works on `customer.py`
- `courier` → Aleesya works on `courier.py`

After each branch is tested, merge into `main`.

## Important

All modules share the same `parcels` list because `main.py` passes it to the Customer and Courier functions. This means a status updated by the Courier can immediately be seen by the Customer during the same program session.
