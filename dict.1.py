# Using one dictionary
# Hotel has 5 rooms
# names are 101-105
# store occupant name for each room

# Make sure you can put someone in unoccupied room
# make a room available by setting the occupant name to ""
# check if room number is valid
# check if room is occupied or not

#any one room should have occupant name, number, and if pre-paid          


hotel_atl = {
    'room_101' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
    'room_102' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available'
        },
    'room_103' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
}

hotel_ny = {
    'room_101' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
    'room_102' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
    'room_103' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
}

hotel_la = {
    'room_101' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
    'room_102' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
    'room_103' : {
        'occupant' : '',
        'phone_number' : '',
        'prepaid?' : '',
        'status' : 'Available',
        },
}

main_menu = '''

1. Print Hotel Room Status
2. Check-In Customer
3. Check-Out Customer
4. Quit

'''

while True:
    choice = int(input(main_menu))
    if choice == 1:
        for i in hotel_atl.keys():
            print(f"{i} at Hotel ATL is {hotel_atl[i]['status']}")
        for i in hotel_ny.keys():
            print(f"{i} at Hotel NY is {hotel_ny[i]['status']}")
        for i in hotel_la.keys():
            print(f"{i} at Hotel LA is {hotel_la[i]['status']}")
    if choice == 2:
        need_room = input('Do you need a room?yes/no ')
        if need_room == 'yes':
            where = input('Where do you want to stay? hotel_atl, hotel_ny, or hotel_la: ')
            name = input('Enter your name: ')
            phone = input('Enter your phone number: ')
            prepay = input('Would you like to prepay? yes, no: ')
            if where == 'hotel_atl':
                if hotel_atl['room_101']['status'] == 'Available':
                    hotel_atl['room_101']['name'] = name
                    hotel_atl['room_101']['phone number'] = phone
                    hotel_atl['room_101']['status'] = 'Occupied'
                    hotel_atl['room_101']['prepaid?'] = prepay
                elif hotel_atl['room_102']['status'] == 'Available':
                    hotel_atl['room_102']['name'] = name
                    hotel_atl['room_102']['phone number'] = phone
                    hotel_atl['room_102']['status'] = 'Occupied'
                    hotel_atl['room_102']['prepaid?'] = prepay
                elif hotel_atl['room_103']['status'] == 'Available':
                    hotel_atl['room_103']['name'] = name
                    hotel_atl['room_103']['phone number'] = phone
                    hotel_atl['room_103']['status'] = 'Occupied'
                    hotel_atl['room_103']['prepaid?'] = prepay
                else:
                    print('Sorry, Hotel ATL is at capacity!')
            if where == 'hotel_ny':
                if hotel_ny['room_101']['status'] == 'Available':
                    hotel_ny['room_101']['name'] = name
                    hotel_ny['room_101']['phone number'] = phone
                    hotel_ny['room_101']['status'] = 'Occupied'
                    hotel_ny['room_101']['prepaid?'] = prepay
                elif hotel_ny['room_102']['status'] == 'Available':
                    hotel_ny['room_102']['name'] = name
                    hotel_ny['room_102']['phone number'] = phone
                    hotel_ny['room_102']['status'] = 'Occupied'
                    hotel_ny['room_102']['prepaid?'] = prepay
                elif hotel_ny['room_103']['status'] == 'Available':
                    hotel_ny['room_103']['name'] = name
                    hotel_ny['room_103']['phone number'] = phone
                    hotel_ny['room_103']['status'] = 'Occupied'
                    hotel_ny['room_103']['prepaid?'] = prepay
                else:
                    print('Sorry, Hotel NY is at capacity!')
            if where == 'hotel_la':
                if hotel_la['room_101']['status'] == 'Available':
                    hotel_la['room_101']['name'] = name
                    hotel_la['room_101']['phone number'] = phone
                    hotel_la['room_101']['status'] = 'Occupied'
                    hotel_la['room_101']['prepaid?'] = prepay
                elif hotel_la['room_102']['status'] == 'Available':
                    hotel_la['room_102']['name'] = name
                    hotel_la['room_102']['phone number'] = phone
                    hotel_la['room_102']['status'] = 'Occupied'
                    hotel_la['room_102']['prepaid?'] = prepay
                elif hotel_la['room_103']['status'] == 'Available':
                    hotel_la['room_103']['name'] = name
                    hotel_la['room_103']['phone number'] = phone
                    hotel_la['room_103']['status'] = 'Occupied'
                    hotel_la['room_103']['prepaid?'] = prepay
                else:
                    print('Sorry, Hotel LA is at capacity!')
        elif need_room == 'no':
            print('ok bye!')
        else:
            print('Try entering a valid response...')
    if choice == 3:
        leaving_from = input('Which hotel are you checking out of? hotel_atl, hotel_ny, hotel_la: ')
        exit_room = input('What room are you staying in? room_101, room_102, or room_103: ')
        if leaving_from == 'hotel_atl':
            hotel_atl[exit_room]['name'] = ''
            hotel_atl[exit_room]['phone number'] = ''
            hotel_atl[exit_room]['status'] = 'Available'
            if hotel_atl[exit_room]['prepaid?'] == 'yes':
                print('We hope you enjoyed your stay. Come back soon!')
            else:
                print('Please provide a payment method..')
        elif leaving_from == 'hotel_ny':
            hotel_ny[exit_room]['name'] = ''
            hotel_ny[exit_room]['phone number'] = ''
            hotel_ny[exit_room]['status'] = 'Available'
            if hotel_ny[exit_room]['prepaid?'] == 'yes':
                print('We hope you enjoyed your stay. Come back soon!')
            else:
                print('Please provide a payment method..')
        elif leaving_from == 'hotel_la':
            hotel_la[exit_room]['name'] = ''
            hotel_la[exit_room]['phone number'] = ''
            hotel_la[exit_room]['status'] = 'Available'
            if hotel_la[exit_room]['prepaid?'] == 'yes':
                print('We hope you enjoyed your stay. Come back soon!')
            else:
                print('Please provide a payment method..')
        else:
            print('Invalid response. Try again.')
    if choice == 4:
        break
print('Thanks for using our service!')


#THIS WORKS THE SMALL EXERCISES

# hotel = {
#     'room_101' : {
#         'occupant' : '',
#         'phone_number' : '',
#         'prepaid?' : '',
#         },
#     'room_102' : {
#         'occupant' : '',
#         'phone_number' : '',
#         'prepaid?' : '',
#         },
#     'room_103' : {
#         'occupant' : 'rob',
#         'phone_number' : '4046973803',
#         'prepaid?' : True,
#         },
#     'room_104' : {
#         'occupant' : '',
#         'phone_number' : '',
#         'prepaid?' : '',
#         },
#     'room_105' : {
#         'occupant' : '',
#         'phone_number' : '',
#         'prepaid?' : '',
#         },
# }

# new_guest = {}

# def is_vacant(hotel_name, room_string, occ_key):
#     for i in hotel.keys():
#         if hotel_name[room_string][occ_key] == '':
#             return f'{room_string} is available.'
#         else:
#             return f"{room_string} is occupied by {hotel_name[room_string][occ_key]}."
# print(is_vacant(hotel, 'room_103', 'occupant'))

# def check_in(room_string, guest_dict):
#     need_room = input('Do you need a room? ')
#     if need_room == 'yes':
#         name = input('Enter your name: ')
#         phone = input('Enter your phone number: ')
#         prepay = input('Do you want to prepay? True/False: ')
#         prepay = prepay.capitalize()
#         new_guest['name'] = name
#         new_guest['phone_number'] = phone
#         new_guest['prepaid'] = prepay
#     elif need_room == 'no':
#         print('ok bye!')
#     if new_guest != {}:
#         hotel[room_string] = new_guest
# print(check_in('room_101', new_guest))
# print(hotel)

# def checkout(room_string):
#     leave = input('Want to checkout? True/ False: ')
#     leave = leave.capitalize()
#     if leave == 'True':
#         hotel[room_string]['occupant'] = ''
#         hotel[room_string]['phone_number'] = ''
#         hotel[room_string]['prepay?'] = ''
#         print('Thanks for your business!')
#         print(hotel)
#     else:
#         print('Great! Let us know if we can get you anything!')
# print(checkout('room_103'))

#CHECKS HOTEL FOR VACANCY AND DISPLAYS RESULTS
# for i in hotel.keys():
#     if hotel[i]['occupant'] == '':
#         print(f'{i} is available.')
#     else:
#         print(f"{i} is occupied by {hotel[i]['occupant']}.")




#THE FOLLOWING CODE WORKS FOR THE FIRST EXERCISE
# hotel = {
#     'room 101' : '',
#     'room 102' : '',
#     'room 103' : '',
#     'room 104' : '',
#     'room 105' : '',
# }

# while True:
#     for x in hotel:
#         print(x)
#         if hotel[x] == '':
#             print('This room is available')
#         else:
#             print('Room occupied')
#         need_room = input('Do you need to add someone to a room? yes or no: ')
#         need_room = need_room.lower()
#         if need_room == 'yes':
#             name = input('What name should we use on the reservation? ')
#             name = name.lower()
#             hotel[x] = name
#             print(f'Your bookings list is now: {hotel}')
#         elif need_room == 'no':
#             pass
#         else:
#             while need_room == 'no' and hotel[x] == 'room 105':
#                 break
#     break
