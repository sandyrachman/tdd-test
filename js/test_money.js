const assert = require('assert');

class Dollar {
    constructor(amount) {
        this.amount = amount;
    }

    times(multiplier) {
        return new Dollar(this.amount * multiplier);
    }    
}

class Money {
    constructor(amount, currency) {
        this.amount = amount;
        this.currency = currency;
    }

    times(multiplier){
        return new Money(this.amount * multiplier, this.currency);
    }

    divide(divider){
        return new Money(this.amount / divider, this.currency);
    }
}

let fiveDollars = new Money(5, "USD");
let tenDollars = fiveDollars.times(2);
assert.strictEqual(tenDollars.amount, 10);
assert.strictEqual(tenDollars.currency, "USD");
assert.deepStrictEqual(fiveDollars.times(2), tenDollars);

let tenEuros = new Money(10, "EUR");
let twentyEuros = tenEuros.times(2);
assert.strictEqual(twentyEuros.amount, 20);
assert.strictEqual(twentyEuros.currency, "EUR");
assert.deepStrictEqual(tenEuros.times(2), twentyEuros);

let originalMoney = new Money(4002, "KRW");
let actualMoneyAfterDivision = originalMoney.divide(4);
let expectedMoneyAfterDivision = new Money(1000.5, "KRW");
assert.deepStrictEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision);