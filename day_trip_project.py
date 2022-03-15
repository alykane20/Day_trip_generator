import random

# options for building trip
destinations = ["Boston, MA", "Dublin, Ireland", "Costa Rica", "Kenya"]
transportations = ["Car", "Private jet", "Train", "Yacht"]
restaurants = ["McDonalds", "California Taco", "Smashburger", "Pizzagando"]
entertainment = ["Patriots game", "Adele concert", "Jungle safari", "Duck boat tour"]


def welcome_to_pick_your_trip():
    user_wants_trip = input("Would you like to go on a trip this weekend? y/n:")
    if user_wants_trip == "y":
        print("Great! Let's pick a destination to start!")
    else:
        print("Enjoy your weekend at home!")

def chose_random_option(list, decription_of_item):
    option_chosen = (random.choice(list))
    print(decription_of_item) 
    print(f"{option_chosen}")
    option_ok_by_user = input("Is this ok? y/n:")
    while option_ok_by_user != "y":
        option_chosen = (random.choice(list))
        print(f"No worries, how about: {option_chosen}")
        option_ok_by_user = input("Is this ok? y/n:")
    print("Awesome!")
    return option_chosen
  
def build_your_weekend_trip():
    welcome_to_pick_your_trip()
    final_destination = chose_random_option(destinations, "You will be traveling to:")
    final_transportation = chose_random_option(transportations, "You will arrive by:")
    final_restaurant = chose_random_option(restaurants, "Dinner reservations at:")
    final_entertainment = chose_random_option(entertainment, "You will have fun at:")
    print("Congrats! Here is what you've decided to do:") 
    print(f"Destination: {final_destination}")
    print(f"Transportation: {final_transportation}")
    print(f"Restaurant: {final_restaurant}")
    print(f"Entertainment: {final_entertainment}")
    confirmation_user_choice = input("Does this trip look good? y/n:")
    while confirmation_user_choice != "y":
        print("Ok, let's start over and pick a trip that you like!")
        build_your_weekend_trip()
    print(f"You will be traveling to {final_destination} by {final_transportation}. For dinner, you will eat at local favorite {final_restaurant}, and then attend {final_entertainment}")


build_your_weekend_trip()


             





