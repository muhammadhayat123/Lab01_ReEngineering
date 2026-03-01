# legacy_system.py
import datetime

def process():
    print("Welcome to Shop System")
    name = input("Enter customer name: ")
    total = 0

    while True:
        item = input("Enter item price (or 'q' to quit): ")
        if item == 'q':
            break
        total += float(item)

    discount = 0
    if total > 1000:
        discount = total * 0.1

    final = total - discount

    print("Customer:", name)
    print("Total:", total)
    print("Discount:", discount)
    print("Final:", final)
    print("Date:", datetime.datetime.now())

process()