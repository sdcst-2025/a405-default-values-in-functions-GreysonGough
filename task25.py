#!python3
# Currency Conversion
"""
Most of the time, in Canada, we convert our money
into USD. But we could also travel to other places

Create a function that accepts:
required: 1 positional argument - amount of money to convert
optional:
1 argument: currency to convert from default CAD
1 argument: currency to covnert to default USD

Conversion rates to use:
1 USD = 1.35 CAD
1 BTC = 62000 USD
1 USD = 1.51 AUD
1 USD = 155 Yen
1 Eur = 1.07 USD

Units must be in ["USD","CAD","BTC","AUD","Yen","Eur"]
"""

def convert(amount, from_currency="CAD", to_currency="USD"):
    rates_to_usd = {
        "USD": 1,
        "CAD": 1 / 1.35,
        "BTC": 62000,  
        "AUD": 1 / 1.51,     
        "Yen": 1 / 155,
        "Eur": 1.07           
    }
      
    usd_amount = amount * rates_to_usd[from_currency]
    result = usd_amount / rates_to_usd[to_currency]
    # inputs
    # required: amount of currency
    # optional: original currency type default CAD
    # optional: converted currency type default USD
    return round(result, 2) 
    # returns the number of what you are converting to along with units
    # round answers to 4 decimals


if __name__ == "__main__":
    assert convert(1.35) == 1
    assert convert(1,"USD") == 1
    assert convert(1,"USD","CAD") == 1.35
    assert convert(1,"BTC") == 62000
    assert convert(1,"BTC","CAD") == 83700
    assert convert(1,"BTC","Eur") == 57943.93
    
    
