from src.guest import Guest


class Payment:
    """
    Class to handle payment transactions made by guests.
        Attributes:
    guest (Guest): Guest object representing the guest making the payment.
    amount (float): The amount of the payment.
    is_paid (bool): A boolean flag indicating whether the payment has been made or not.
    """

    def init(self, guest, amount):
        """
        Initializes a new Payment object with the given guest and payment amount.

        Args:
        guest (Guest): Guest object representing the guest making the payment.
        amount (float): The amount of the payment.
        """
        self.guest = guest
        self.amount = amount
        self.is_paid = False

    def make_payment(self):
        """
        Simulates a payment process and updates the payment status to "paid" once payment is successful.

        Returns:
        None
        """
        self.is_paid = True
        print(f"{self.guest.name} has successfully paid {self.amount}.")

    def get_payment_details(self):
        """
        Returns a string representation of the payment details.

        Returns:
        str: A string containing the guest name, payment amount, and payment status.
        """
        payment_status = "paid" if self.is_paid else "not paid"
        return f"Guest name: {self.guest.name}\nPayment amount: {self.amount}\nPayment status: {payment_status}"


def main():
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    phone_number = input("Enter guest phone number: ")

    while True:
        try:
            amount = float(input("Enter payment amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    guest = Guest(name, email, phone_number)
    payment = Payment(guest, amount)

    payment.make_payment()
    print(payment.get_payment_details())


if __name__ == "__main__":
    main()
