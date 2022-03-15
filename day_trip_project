destinations = ["Boston, MA", "Dublin, Ireland", "Costa Rica", "Kenya"]
transportations = ["Car", "Private jet", "Train", "Yacht"]
restaurants = ["McDonalds", "California Taco", "Smashburger", "Pizzagando"]
entertainment = ["Patriots game", "Adele concert", "Jungle safari", "Duck boat tour"]

import random

def welcome_to_pick_your_trip():
    user_wants_trip = input("Would you like to go on a trip this weekend? y/n:")
    if user_wants_trip == "y":
        print("Great! Let's pick a destination to start!")
    else:
        print("Enjoy your weekend at home!")

def chose_destination(list_of_destinations):
    location_chosen = (random.choice(destinations))
    print(f"We have chosen: {location_chosen}")
    location_ok_by_user = input("Is this ok? y/n:")
    while location_ok_by_user != "y":
        location_chosen = (random.choice(destinations))
        print(f"How about: {location_chosen}")
        location_ok_by_user = input("Is this ok? y/n:")
    print("Awesome, let's figure out how to get there!")
    return location_chosen


def chose_transport(list_of_transportation):
    transport_chosen = (random.choice(transportations))
    print(f"We will travel by: {transport_chosen}")
    transport_ok_by_user = input("Is this ok? y/n:")
    while transport_ok_by_user != "y":
        transport_chosen = (random.choice(transportations))
        print(f"How about: {transport_chosen}")
        transport_ok_by_user = input("Is this ok? y/n:")
    print("Sounds good, now we can pick somewhere to eat")
    return transport_chosen

def chose_restaurant(list_of_restaurants):
    restaurant_chosen = (random.choice(restaurants))
    print(f"We have chosen to eat at: {restaurant_chosen}")
    restaurant_ok_by_user = input("Is this ok? y/n:")
    while restaurant_ok_by_user != "y":
        restaurant_chosen = (random.choice(restaurants))
        print(f"How about: {restaurant_chosen}")
        restaurant_ok_by_user= input("Is this ok? y/n:")
    print("Great! Time to be entertained!")
    return restaurant_chosen
    

def chose_entertainment(list_of_entertainment):
    entertainment_chosen = (random.choice(entertainment))
    print(f"We have chosen to attend: {entertainment_chosen}")
    entertainment_ok_by_user = input("Is this ok? y/n:")
    while entertainment_ok_by_user != "y":
        entertainment_chosen = (random.choice(entertainment))
        print(f"How about: {entertainment_chosen}")
        entertainment_ok_by_user = input("Is this ok? y/n:")
    print("Sounds fun!")
    return entertainment_chosen
    
    
def build_your_weekend_trip():
    welcome_to_pick_your_trip()
    final_destination = chose_destination(destinations)
    final_transportation = chose_transport(transportations)
    final_restaurant = chose_restaurant(restaurants)
    final_entertainment = chose_entertainment(entertainment)
    travel_choices = [final_destination, final_transportation, final_restaurant, final_entertainment]
    print("Congrats! Here is what you've decided to do:") 
    for choice in travel_choices:
        print(choice)
    confirmation_user_choice = input("Does this trip look good? y/n:")
    while confirmation_user_choice != "y":
        print("Ok, let's start over and pick a trip that you like!")
        build_your_weekend_trip()
    print(f"You will be traveling to {final_destination} by {final_transportation}. For dinner, you will eat at local favorite {final_restaurant}, and then attend {final_entertainment}")


build_your_weekend_trip()


             





