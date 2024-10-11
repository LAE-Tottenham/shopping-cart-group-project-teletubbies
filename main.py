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

def cart():
    items = {'caviar':0,'wagyu':0,'white truffle':0,'saffron':0,'watermelon':0,'milk':0,'shortbread':0,'bluefin tuna':0,'ham':0,'butter':0}
    stop = 0
    while stop == 0:
        keys = [k for k in items]
        choice = input("Select product %s: " %(keys))
        choice = valid_choice(items, choice)

        amount = input('Enter quantity needed: ')
        amount = valid(amount)

        items[choice] = amount
        stop = input("Enter '1' to quit: ")
        stop = valid(stop)
    return items

def value(user_cart):
    items = {'caviar':5,'wagyu':10,'white truffle':13,'saffron':2,'watermelon':0.50,'milk':1,'shortbread':4,'bluefin tuna':15,'ham':6,'butter':2.50}
    total = 0
    for x in user_cart:
        total += user_cart[x]*items[x]
    return total

print(value(cart()))