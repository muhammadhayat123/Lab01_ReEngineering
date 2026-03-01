# legacy_system.py
import datetime

def calculate_discount(total):
    """
    Calculate discount based on total amount.
    10% discount if total > 1000.
    """
    if total > 1000:
        return total * 0.1
    return 0

def get_item_prices():
    """
    Prompt user to enter item prices until 'q' is entered.
    Returns the total sum of all items.
    Handles invalid inputs gracefully.
    """
    total = 0
    while True:
        item = input("Enter item price (or 'q' to quit): ")
        if item.lower() == 'q':
            break
        try:
            price = float(item)
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            total += price
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    return total

def process():
    """
    Main process for the shop system:
    - Get customer name
    - Get total item prices
    - Calculate discount
    - Display summary
    """
    print("Welcome to Shop System")
    name = input("Enter customer name: ")

    total = get_item_prices()
    discount = calculate_discount(total)
    final_total = total - discount

    print("\n--- Receipt ---")
    print(f"Customer: {name}")
    print(f"Total: {total:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Total: {final_total:.2f}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    process()