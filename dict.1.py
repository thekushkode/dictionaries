# Using one dictionary
# Hotel has 5 rooms
# names are 101-105
# store occupant name for each room

# Make sure you can put someone in unoccupied room
# make a room available by setting the occupant name to ""
# check if room number is valid
# check if room is occupied or not

hotel = {
    'room 101' : '',
    'room 102' : '',
    'room 103' : '',
    'room 104' : '',
    'room 105' : '',
}

while True:
    for x in hotel:
        print(x)
        if hotel[x] == '':
            print('This room is available')
        else:
            print('Room occupied')
        need_room = input('Do you need to add someone to a room? yes or no: ')
        need_room = need_room.lower()
        if need_room == 'yes':
            name = input('What name should we use on the reservation? ')
            name = name.lower()
            hotel[x] = name
            print(f'Your bookings list is now: {hotel}')
        elif need_room == 'no':
            pass
        elif need_room == 'no' and hotel[x] == 'room 105':
            break

# OR
# hotel = {
#     'room' : [101, 102, 103, 104, 105]
#     'guest' : ['', '', '', '', '']
# }

#OR
# hotel = {
#     'room1' : 101,
#     'guest1' : '',
#     'room2' : 102,
#     'guest2' : '',
#     'room3' : 103,
#     'guest3' : '',
#     'room4' : 104,
#     'guest4' : '',
#     'room5' : 105,
#     'guest5' : '',
# }