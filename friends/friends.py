# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

friends = input('List 3 friends separeted by a comma: ').title().split(',')
friends = [friend.strip() for friend in friends]

people_file = open('people.txt', 'r')
people_file_content = [line.strip() for line in people_file.readlines()]
people_file.close()

friends_set = set(friends)
people_nearby_set = set(people_file_content) 

friends_nearby_set = friends_set.intersection(people_nearby_set)

if len(friends_nearby_set) != 0:
    nearby_friends = open('nearby_friends.txt', 'w')
    for friend in friends_nearby_set:
        nearby_friends.writelines(friend+"\n")
    nearby_friends.close()
    print('Friends added to nearby_friends list.')
else:
    print('No friends near.')