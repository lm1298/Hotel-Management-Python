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

def process_payment(guest_name, amount):
    guest = Guest(guest_name)
    payment = Payment(guest, amount)
    payment.make_payment()
    return payment.get_payment_details()

details = process_payment("John Smith", 100)
print(details)