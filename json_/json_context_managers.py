import json

with open('friends_json.txt', 'r') as file_:
    file_contents = json.load(file_) # Read file and turns it to dictionary


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file_:
    json.dump(cars, file_)

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])