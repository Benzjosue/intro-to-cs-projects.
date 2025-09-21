'''
Program name: Highway Identifier
Author name: Huirong Chai
Description: This program gets a highway number from user, indicate whether it is a primary, 
            auxilary highway, or an invalid highway number. If auxiliary, indicate what primary highway
            it serves. Also, indicate if the (primary) highway runs north/south or east/west

'''

highway_number = int(input('Please enter an interstate number: '))
#================= Primary Highway ============================
if 1 <= highway_number <= 99: #Means primary highway 
    if highway_number  % 2 == 0: #Even number means east/west.
        print(f'I-{highway_number} is a primary, going east/west.')
    else:
        print(f'I-{highway_number} is a primary, going north/south.')

#================= Auxiliary Highway ===========================
elif 100 <= highway_number <=999: # Auxiliary highway.
    if (highway_number % 100) == 0 or (highway_number % 100) > 99:
        print(f'I-{highway_number} is not a valid interstate highway number.')
    elif (highway_number % 100) % 2 == 0:
        print(f'I-{highway_number} is an auxiliary, serving I-{highway_number % 100}, going east/west.')
    else: #odd number
        print(f'I-{highway_number} is an auziliary, serving I-{highway_number % 100}, going north/south.')

#============== Invalid Highway =============
else:
    print(f'I-{highway_number} is not a valid interstate highway number')
