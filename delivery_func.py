
from datetime import date
from datetime import timedelta
def delivery(postcode):
    price = ord(postcode[0]) * 2
    return price

def delivery_day_time():
    today = date.today()
    delivery_date = today + timedelta(days=7)
    print("Choose a slot for delivery on",delivery_date,"\n1) 9:00AM\n2) 12:00PM\n3) 18:00PM")
    choice = input()
    times = [
        ['1' , "9:00AM"],
        ['2' , "12:00PM"],
        ['3' , "18:00PM"]
    ]
    while choice not in ['1','2','3']:
        print("Choose a slot for delivery on",delivery_date,"\n1) 9:00AM\n2) 12:00PM\n3) 18:00PM")
        choice = input()

    for counter in times:
        if choice == counter[0]:
            timeslot = counter[1]

    return [delivery_date,timeslot]
    # delivery details are stored as array [day,timeslot] (use index [0] for day and [1] for time)

