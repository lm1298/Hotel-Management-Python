class Guest:
    def __init__(self, name):
        self.name = name

class Payment:
    def __init__(self, guest, amount):
        self.guest = guest
        self.amount = amount
        self.is_paid = False

    def make_payment(self):
        self.is_paid = True
        print(f"{self.guest.name} has paid {self.amount}.")

    def get_payment_details(self):
        if self.is_paid:
            status = "Paid" 
        else: "Unpaid"

        return f"Guest: {self.guest.name}, Amount: {self.amount}, Status: {status}"

guest = Guest("John Smith")

payment = Payment(guest, 100)

payment.make_payment()

details = payment.get_payment_details()

print(details)