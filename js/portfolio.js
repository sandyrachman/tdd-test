const Money = require("./money");

class Portfolio {
  constructor() {
    this.moneys = [];
  }

  add(...moneys) {
    this.moneys = this.moneys.concat(moneys);
  }

  evaluate(currency) {
    let total = this.moneys.reduce((sum, money) => {
      return sum + this.convert(money, currency);
    }, 0);

    return new Money(total, currency);
  }

  convert(money, currency) {
    // let eurToUsd = 1.2;
    let exchangeRates = new Map();
    exchangeRates.set("EUR->USD", 1.2);
    exchangeRates.set("USD->KRW", 1100);
    let key = money.currency + "->" + currency;

    if (money.currency === currency) {
      return money.amount;
    }
    // return money.amount * eurToUsd;
    return money.amount * exchangeRates.get(key);
  }
}

module.exports = Portfolio;
