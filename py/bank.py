from money import Money

class Bank:
    def __init__(self) -> None:
        self.exchangeRates = {}
    
    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchangeRates[key] = rate
    
    def convert(self, aMoney, aCurency):
        if aMoney.currency == aCurency:
            return Money(aMoney.amount, aCurency)
        
        key = aMoney.currency + "->" + aCurency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurency)
        
        raise Exception(key)