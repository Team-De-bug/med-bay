from .models import Bill, BillUnit


# Getting cart total
def get_total(orders):
    total = 0
    for order in orders:
        total += order.quantity * order.item.price
    return total


# Getting total for bill objects
def get_bill_total(bill_units):
    total = 0
    for unit in bill_units:
        total += unit.quantity * unit.price
    return total


# Generating bills
def generate_bill(name, contact_num, date, orders):
    bill = Bill(name=name, contact_num=contact_num, date=date)
    bill.save()
    total = 0

    # Creating the bill_units and removing orders
    for order in orders:
        unit = BillUnit(name=order.item.name, quantity=order.quantity,
                        desc=order.item.desc, price=order.item.price,
                        bill=bill)
        total += order.item.price * order.quantity
        unit.save()

    return bill
