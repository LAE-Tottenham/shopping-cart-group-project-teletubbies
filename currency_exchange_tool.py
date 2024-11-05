def valid_price(price):
    global currency
    if price<10 or price>1000:
        return False
    else:
        return price


curr_rate = {"USD": 1.3, "EURO": 1.2, "CAD": 1.8, "NAIRA": 2121, "COP": 5543,"GBP":1}

def curr_convert(currency, price):
    global curr_rate
    if currency in curr_rate:
        rate = curr_rate[currency]
        result = round(rate*price,2)
        return str(price) + " in " + currency + " is " + str(result)
    else:
        return False
