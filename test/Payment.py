import csv

class Guest:
    """
    A class representing a guest.

    Attributes:
    -----------
    name : str
        The name of the guest.
    """

    def __init__(self, name):
        self.name = name

class Payment:
    """
    A class representing a payment.

    Attributes:
    guest : Guest
        The guest who made the payment.
    amount : int
        The amount of the payment.
    is_paid : bool, optional
        Whether the payment is paid or not, default is False.
    """
    def __init__(self, guest, amount):
        self.guest = guest
        self.amount = amount
        self.is_paid = False

    def make_payment(self):
        """
        Updates the payment status to "paid" and prints a message.
        """
        self.is_paid = True
        print(f"{self.guest.name} has paid {self.amount}.")

    def get_payment_details(self):
        """
        Returns the payment details.
        """
        if self.is_paid:
            status = "Paid"
        else:
            status = "Unpaid"
        return f"Guest: {self.guest.name}, Amount: ${self.amount}, Status: {status}"

def process_payment_unpaid(guest_name, amount):
    """
    Creates a new unpaid payment.

    Parameters:
    guest_name : str
        The name of the guest.
    amount : int
        The amount of the payment.

    Returns:
    str
        The payment details.
    """
    guest = Guest(guest_name)
    payment = Payment(guest, amount)
    return payment.get_payment_details()

def process_payment_paid(guest_name, amount):
    """
    Creates a new paid payment.

    Parameters:
    -----------
    guest_name : str
        The name of the guest.
    amount : int
        The amount of the payment.

    Returns:
    str
        The payment details.
    """
    guest = Guest(guest_name)
    payment = Payment(guest, amount)
    payment.make_payment()
    return payment.get_payment_details()

def paid():
    """
    Retrieves all paid payments from the CSV file.

    Returns:
    str
        A str of payment details for paid payments.
    """
    with open("payment.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest_name = row["Name"]
            amount = int(row["Amount"])
            status = row["Status"]
            if status == "Paid":
                test2 = process_payment_paid(guest_name, amount)
                print(test2)

def unpaid():
    """
    Retrieves all unpaid payments from the CSV file.

    Returns:
        str
        A str of payment details for unpaid payments.
    """
    with open("payment.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest_name = row["Name"]
            amount = int(row["Amount"])
            status = row["Status"]
            if status == "Unpaid":
                test1 = process_payment_unpaid(guest_name, amount)
                print(test1)

paid()
unpaid()
