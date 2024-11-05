import time
import greeting
import currency_exchange_tool as cet
import cart_func as cf
import delivery_func as ddt

wel1 = greeting.welcome()
wel2 = greeting.dots()
wel3 = greeting.title()
wel4 = greeting.listofoptions()
end = greeting.exit()

print(wel1)
time.sleep(2)
print(wel2)
time.sleep(2)
print(wel3)
time.sleep(2)
print(wel4)
time.sleep(2)


price = cf.value(cf.cart())

# DELIVERY STUFF
del_price = ddt.delivery(input("Enter your postcode: "))
print('deliver price: £', del_price)
price += del_price
val = ddt.delivery_day_time()
print('date: ', val[0],'time: ', val[1])

# CURRENCY EXCHANGE
x = cet.valid_price(price)
if x == False:
    print("Invalid price\n")
else:
    currency = input("What currency do you want (default: GBP): " + str(list(cet.curr_rate.keys())) + "\n").upper()
    y = cet.curr_convert(currency, price)
    if y == False:
        print("Invalid currency\n")
    else:
        print(y)


    
print(end)