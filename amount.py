from datetime import datetime


class Amount:
    def __init__(self, amount, transaction_type):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.amount = amount
        self.timestamp = dt_string
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Amount: {self.amount}, Time: {self.timestamp}, Transaction_type: {self.transaction_type}"

