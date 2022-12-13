import random

destinations = ['New York', 'London', 'Rome', 'Barcelona']
restaurants = ['JJs Pizza', 'Gordos', 'Le Calandre', 'Alkimia']
transportation = ['Plane', 'Cruise', 'Train', 'Car']
entertainment = ['Knicks Game', 'Theater', 'Ballet', 'Art show']

for destination in destinations:
    print(destination)
for restaurant in restaurants:
    print(restaurant)
for transport in transportation:
    print(transport)
for mode in entertainment:
    print(mode)

print = input('Are you satisfied with your trip?' 'Y/N')

random = destination = random.choice(destinations)
random = restaurant =random.choice(restaurants)
random = transport = random.choice(transportation)
random = mode = random.choice(entertainment)
user_response = 'N'

if user_response != 'Y':
    print = random.choice (destination, restaurant, transport, mode)

if user_response == 'Y':
    print('Enjoy your trip!')