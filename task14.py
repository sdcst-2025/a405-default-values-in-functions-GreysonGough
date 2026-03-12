import random
def calcTax(price, percent = 7):
    tax = price * percent / 100  # you will need to add your arguments here
    return round(tax, 2)     # you will need to add a return value


if __name__ == "__main__":
    assert calcTax(61.49) == 4.3
    assert calcTax(121.71) == 8.52
    assert calcTax(106.83) == 7.48
    assert calcTax(101.66) == 7.12
    assert calcTax(125.12) == 8.76
    assert calcTax(141.78) == 9.92
    assert calcTax(23.23) == 1.63
    assert calcTax(94.61) == 6.62
    assert calcTax(44.85) == 3.14
    assert calcTax(145.52) == 10.19
    assert calcTax(42.7) == 2.99
    assert calcTax(125.67) == 8.8
    assert calcTax(40.33) == 2.82
    assert calcTax(75.34,9) == 6.78
    assert calcTax(138.38,11) == 15.22
    assert calcTax(121.88,12) == 14.63
    assert calcTax(42.99,9) == 3.87  
    assert calcTax(126.05,12) == 15.13
    assert calcTax(108.01,7) == 7.56  
    assert calcTax(100.35,11) == 11.04
    assert calcTax(86.46,6) == 5.19  
    assert calcTax(69.19,9) == 6.23  
    assert calcTax(69.85,6) == 4.19  
    assert calcTax(28.48,10) == 2.85  
    assert calcTax(16.41,7) == 1.15  
    assert calcTax(132.66,5) == 6.63
    assert calcTax(81.53,12) == 9.78
    assert calcTax(119.9,7) == 8.39
    assert calcTax(72.86,4) == 2.91
    assert calcTax(107.18,9) == 9.65
    assert calcTax(105.83,12) == 12.7
    assert calcTax(39.96,11) == 4.4
    assert calcTax(139.73,9) == 12.58  