class Guest:
    def __init__(self, name):
        self.name = name

class Payment:
    """
    Args
    - guest (str): The name of the guest making the payment
    - amount(int): The cost of the bill
    - is_paid (boolean): Whether the customer has paid, set to False
    """
    def __init__(self, guest, amount):
        self.guest = guest
        self.amount = amount
        self.is_paid = False

    def make_payment(self):
        """
    Sets is_paid boolean to true, and makes the payment for the customer.

    Returns: 
    - string of the customer name and integer of the amount paid
    """
        self.is_paid = True
        print(f"{self.guest.name} has paid {self.amount}.")

    def get_payment_details(self): 
        """
    Checks if customer has paid.

    Returns:
    - string of customer name, integer of the amount paid, and boolean of whether
      the custer has made a payment
    """
        if self.is_paid:
            status = "Paid"
        else: 
            status = "Unpaid"
        return f"Guest: {self.guest.name}, Amount: {self.amount}, Status: {status}"

def process_payment_unpaid(guest_name, amount):
    """
    One of two entry points into the functions which uses the outputs of my other functions, and is used when 
    customer makes a reservation but doesn't pay.

    Returns:
    - return of get_payment_details, string of customer name, integer of the amount 
      paid, and boolean of whether the customer has made a payment
    """
    guest = Guest(guest_name)
    payment = Payment(guest, amount)
    return payment.get_payment_details()

def process_payment_paid(guest_name, amount):
    """
    One of two entry points into the functions which uses the outputs of my other functions, and calls
    make_payment after giving name and amount, and is used when customer makes a reservation and pays.

    Returns:
    - return of get_payment_details, string of customer name, integer of the amount 
      paid, and boolean of whether the custer has made a payment
    """
    guest = Guest(guest_name)
    payment = Payment(guest, amount)
    payment.make_payment()
    return payment.get_payment_details()

test1 = process_payment_unpaid("John Smith", 100)
test2 = process_payment_paid("John Smith", 100)
print(test1)
print(test2)