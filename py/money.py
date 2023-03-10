class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, __o: object) -> bool:
        return self.amount == __o.amount and self.currency == __o.currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:0.2f}"
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divider):
        return Money(self.amount / divider, self.currency)