import pyfiglet
import time

def welcome():
    one = pyfiglet.figlet_format("Welcome", font= "slant")
    time.sleep(1)
    return one

def dots():
    two = pyfiglet.figlet_format("to the...", font= "slant")
    time.sleep(1)
    return two

def title():
    three = pyfiglet.figlet_format("Food-4-U Shop!", font= "slant")
    time.sleep(1)
    return three

def listofoptions():
    four = pyfiglet.figlet_format("Items:", font= "contessa")
    time.sleep(1)
    return four

def exit():
    five = pyfiglet.figlet_format("Thanks for shopping at Food-4-U!", font= "contessa")
    return five