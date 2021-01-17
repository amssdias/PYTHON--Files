import json

file_ = open('friends_json.txt', 'r')
file_contents = json.load(file_) # Read file and turns it to dictionary

file_.close()

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file_ = open('cars_json.txt', 'w')
json.dump(cars, file_)
file_.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
