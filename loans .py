loans = []

def add_loan(loan_id, name, sid, device, device_id, date_out, due):
    loan = {
        "loan_id": loan_id,
        "name": name,
        "sid": sid,
        "device": device,
        "device_id": device_id,
        "date_out": date_out,
        "due": due,
        "returned": False
    }
    loans.append(loan)
    print("Added\n")


def show_loans():
    if not loans:
        print("No loans\n")
    for loan in loans:
        print(loan)
    print()


def get_loan(loan_id):
    for loan in loans:
        if loan["loan_id"] == loan_id:
            return loan
    return None


def set_returned(loan_id, value):
    loan = get_loan(loan_id)
    if loan:
        loan["returned"] = value
        print("Updated\n")


def set_due(loan_id, new_due):
    loan = get_loan(loan_id)
    if loan:
        loan["due"] = new_due
        print("Updated\n")


def remove_loan(loan_id):
    for i, loan in enumerate(loans):
        if loan["loan_id"] == loan_id:
            loans.pop(i)
            print("Deleted\n")
            return


if __name__ == "__main__":
    add_loan(1, "Alex Green", "S12345", "Laptop", "L‑001", "2025‑11‑24", "2025‑12‑01")
    show_loans()
    set_due(1, "2025‑12‑05")
    set_returned(1, True)
    remove_loan(1)
    show_loans()
