export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') throw TypeError('Amount must be a number');
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
