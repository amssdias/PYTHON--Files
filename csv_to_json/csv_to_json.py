import json

clubs = open('csv_file.txt')
clubs_content = [club.strip() for club in clubs.readlines()]
clubs.close()

sender = []

for i in clubs_content:

    club = i.split(',')
    club = {
        'club': club[0],
        'city': club[1],
        'country': club[2]
    }
    sender.append(club)

json_file = open('json_file.txt', 'w')
json.dump(sender, json_file)
json_file.close()