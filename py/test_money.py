import unittest

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, __o: object) -> bool:
        return self.amount == __o.amount and self.currency == __o.currency
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divider):
        return Money(self.amount / divider, self.currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollar(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuro(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = Money(20, 'EUR')
        self.assertEqual(twentyEuros, tenEuros.times(2))
    
    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)
    
if __name__ == '__main__':
    unittest.main()