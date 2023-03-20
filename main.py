import random

def generate_trip():
    destinations = ['New York', 'London', 'Rome', 'Barcelona']
    restaurants = ['JJs Pizza', 'Gordos', 'Le Calandre', 'Alkimia']
    transportations = ['Plane', 'Cruise', 'Train', 'Car']
    entertainments = ['Knicks Game', 'Theater', 'Ballet', 'Art show']


    destination = random.choice(destinations)
    restaurant =random.choice(restaurants)
    transportation = random.choice(transportations)
    entertainment = random.choice(entertainments)

    trip = [destination, restaurant, transportation, entertainment]
    return trip


def display_trip(selections_list):
    print()
    for selection in selections_list:
        print(selection)
    print()

user_response = 'N'

while user_response != 'Y':
    trip = generate_trip()
    display_trip(trip)
    user_response = input('Are you satisfied with your trip?' 'Y/N')

if user_response == 'Y':
    print('Enjoy your trip!')