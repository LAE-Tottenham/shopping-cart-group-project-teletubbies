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

    while stop != '1':
        keys = [k for k in items]
        choice = input("Select product %s: " %(keys))
        choice = valid_choice(items, choice)

        amount = input('Enter quantity needed: ')
        amount = valid(amount)

        items[choice] = amount
        stop = input("Enter '1' to quit: ")
    return items

#Return value of cart
def value(user_cart):
    items = {'caviar':3,'wagyu':5,'white truffle':8.5,'saffron':2,'watermelon':1,'milk':1.5,'shortbread':2,'bluefin tuna':10,'ham':5,'butter':1.5}
    total = 0
    for x in user_cart:
        total += user_cart[x]*items[x]
    print("Cart value: £", total)
    return total
