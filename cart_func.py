
def delivery_price(postcode):
    price = ord(postcode[0]) * 2
    return price

def delivery_day_time():
    from datetime import date
    today = date.today()
    delivery_date = int(today.day) + 7 
    print("Choose a slot for delivery on",delivery_date,"\n1) 9:00AM\n2) 12:00PM\n3) 18:00PM")
    choice = int(input())
    times = [
        [1 , "9:00AM"],
        [2 , "12:00PM"],
        [3 , "18:00PM"]
    ]
    while choice not in [1,2,3]:
        print("Choose a slot for delivery on",delivery_date,"\n1) 9:00AM\n2) 12:00PM\n3) 18:00PM")
        choice = int(input())

    for counter in times:
        if choice == counter[0]:
            timeslot = counter[1]

    return [delivery_date,timeslot]
    # delivery details are stored as array [day,timeslot] (use index [0] for day and [1] for time)

#------------------------------------------------------------------------------------------------

#Validates user inputs 
def valid(entry):
    check = False
    while not check:
        count = 0
        for x in entry:
            if x.isalpha() or x in '}/$!&*()_-+=[]{#~@''""\\|<>,.:;£%? ':
                count = 1
                break
        if count != 1:
            check = True
        else:
            entry = input("Invalid. Enter again: ")
    return int(entry)

def valid_choice(products,user):
    while user.lower() not in products:
        user = input("Product unrecognised. Select product from %s:" %(products))
    return user

#Shows lists of items in baskets & quantity of items
def cart():
    items = {'caviar':0,'wagyu':0,'white truffle':0,'saffron':0,'watermelon':0,'milk':0,'shortbread':0,'bluefin tuna':0,'ham':0,'butter':0}
    stop = 0
    for i in items:
        order = "{:^5}"
        print(order.format(i))

    while stop != 1:
        keys = [k for k in items]
        choice = input("Select product %s: " %(keys))
        choice = valid_choice(items, choice)

        amount = input('Enter quantity needed: ')
        amount = valid(amount)

        items[choice] = amount
        stop = input("Enter '1' to quit: ")
        stop = valid(stop)
    return items

#Return value of cart
def value(user_cart):
    items = {'caviar':5,'wagyu':10,'white truffle':13,'saffron':2,'watermelon':0.50,'milk':1,'shortbread':4,'bluefin tuna':15,'ham':6,'butter':2.50}
    total = 0
    for x in user_cart:
        total += user_cart[x]*items[x]
    return total

print(value(cart()))