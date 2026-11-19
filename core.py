CATEGORIES = {"food", "rent", "travel", "fun", "bills", "donations", "other"}
transactions = []

def add_transaction(amount, category, date, kind):
    transactions.append({
        "amount": amount,
        "category": category,
        "date": date,
        "type": kind,
    })
