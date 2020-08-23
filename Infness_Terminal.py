# Imports
import googlemaps
import argparse
from time import sleep, time
import sys
import itertools
import threading

parser = argparse.ArgumentParser(description='Parser that gets google maps key.')
parser.add_argument('--key', '-k', type=str, help='Put your google maps key.', default=False)
args = parser.parse_args()

__TITLE = '''
88                 ad88                                                 
88                d8"                                                   
88                88                                                    
88  8b,dPPYba,  MM88MMM  8b,dPPYba,    ,adPPYba,  ,adPPYba,  ,adPPYba,  
88  88P'   `"8a   88     88P'   `"8a  a8P_____88  I8[    ""  I8[    ""  
88  88       88   88     88       88  8PP"""""""   `"Y8ba,    `"Y8ba,   
88  88       88   88     88       88  "8b,   ,aa  aa    ]8I  aa    ]8I  
88  88       88   88     88       88   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'                                                                    
'''
# font_name = 'Univers'
__KEY = args.key
__SLEEP_TIME_1 = 0.001
__SLEEP_TIME_2 = 0.3
__REQUIERED_TYPE = False
__Place_Types = ['establishment', 'department_store', 'accounting', '[more]', 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'atm', 'bakery', 'bank', 'bar', 'beauty_salon', 'bicycle_store', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetery', 'church', 'city_hall', 'clothing_store', 'convenience_store', 'courthouse', 'dentist', 'doctor', 'drugstore', 'electrician', 'electronics_store', 'embassy', 'fire_station', 'florist', 'funeral_home', 'furniture_store', 'gas_station', 'gym', 'hair_care', 'hardware_store', 'hindu_temple', 'home_goods_store', 'hospital', 'insurance_agency', 'jewelry_store', 'laundry', 'lawyer', 'library', 'light_rail_station', 'liquor_store', 'local_government_office', 'locksmith', 'lodging', 'meal_delivery', 'meal_takeaway', 'mosque', 'movie_rental', 'movie_theater', 'moving_company', 'museum', 'night_club', 'painter', 'park', 'parking', 'pet_store', 'pharmacy', 'physiotherapist', 'plumber', 'police', 'post_office', 'primary_school', 'real_estate_agency', 'restaurant', 'roofing_contractor', 'rv_park', 'school', 'secondary_school', 'shoe_store', 'shopping_mall', 'spa', 'stadium', 'storage', 'store', 'subway_station', 'supermarket', 'synagogue', 'taxi_stand', 'tourist_attraction', 'train_station', 'transit_station', 'travel_agency', 'university', 'veterinary_care', 'zoo']
__Additional_Types = ['administrative_area_level_1', 'administrative_area_level_2', 'administrative_area_level_3', 'administrative_area_level_4', 'administrative_area_level_5', 'archipelago', 'colloquial_area', 'continent', 'country', 'finance', 'floor', 'food', 'general_contractor', 'geocode', 'health', 'intersection', 'locality', 'natural_feature', 'neighborhood', 'place_of_worship', 'plus_code', 'point_of_interest', 'political', 'post_box', 'postal_code', 'postal_code_prefix', 'postal_code_suffix', 'postal_town', 'premise', 'room', 'route', 'street_address', 'street_number', 'sublocality', 'sublocality_level_1', 'sublocality_level_2', 'sublocality_level_3', 'sublocality_level_4', 'sublocality_level_5', 'subpremise', 'town_square']
__OVER = '''
         , ,\ ,'\,'\ ,'\ ,\ ,
   ,  ;\/ \' `'     `   '  /|
   |\/                      |
   :                        |
   :                        |
    |                       |
    |                       |
    :               -.     _|
     :                \     `.
     |         ________:______\\
     :       ,'o       / o    ;
     :       \       ,'-----./
      \_      `--.--'        )
     ,` `.              ,---'|
     : `                     |
      `,-'                   |
      /      ,---.          ,'
   ,-'            `-,------'
  '   `.        ,--'
        `-.____/
-hrr-           \\
'''
done = False


def animate():
    print('\n')
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done: break
        sys.stdout.write(f'\r[loading {c}]')
        sys.stdout.flush()
        sleep(0.1)
    sys.stdout.write('\rDone!        ')


def get_key():
    if not __KEY: return [False, 'Key has not been assigned.']
    else:
        try: gmaps = googlemaps.Client(key=args.key)
        except Exception: return [False, 'Invalid key.']
        else: return [True, 'Valid key.', gmaps]


def get_address(gmaps):
    addres = input('\nProvide an address\n >> ')
    t = threading.Thread(target=animate)
    t.start()
    place_data = gmaps.geocode(addres)
    global done
    done = True
    sleep(1)
    if place_data:
        question = False
        formatted_address = place_data[0].get('formatted_address')
        while question != 1:
            try: question = int(input(f'\n\n That is the correct address ?\n -> {formatted_address}\n\n1  -  YES\n0  -  NO\n\n >> '))
            except Exception: 
                print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
                continue
            else:
                if question == 1: return formatted_address, place_data[0].get('geometry').get('location').get('lat'), place_data[0].get('geometry').get('location').get('lng') 
                elif not question: return get_address(gmaps)
                else: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
    else:
        print('\nInvalid address, try again!')
        return get_address(gmaps)


def get_radius():
    options, values = ['1 KM', '3 KM', '5 KM', '10 KM', '20 KM', '30 KM', '40 KM', '50 KM'], [1000, 3000, 5000, 10000, 20000, 30000, 40000, 50000]
    print('\n==============================\nGET RADIUS:\n')
    for n in options: 
        print(f'{options.index(n)}   -   {n}')
        sleep(__SLEEP_TIME_2)
    radius_choice = -1
    while radius_choice not in list(range(len(options))):
        try: radius_choice = int(input('\nWrite the number corresponding to the radius you want\n\n >> '))
        except Exception: print('[WRITE A NUMBER BETWEEN "1" AND "8"]')
        else:
            if radius_choice in list(range(1, 8)): 
                print(f'\n[SELECTED OPTION: { options[radius_choice]}]')
                sleep(__SLEEP_TIME_2)
                return values[radius_choice]
            else: print('\n[WRITE A NUMBER BETWEEN "1" AND "8"]')
                

def get_type(requiered):
    if requiered:
        print('\n==============================\nGET TYPE:\n\n Choice ONLY one and TYPE:\n')
        for n in __Place_Types[:4]:
            print(f' -> {__Place_Types.index(n)}   -   {n} <-')
            sleep(__SLEEP_TIME_2)
        type_choice_1 = -1
        while type_choice_1 not in list(range(len(__Place_Types[:4]))):
            try: type_choice_1 = int(input('\nWrite the number corresponding to the option you want\n\n >> '))
            except Exception: print(f'[WRITE A NUMBER BETWEEN "0" AND "{len(__Place_Types[:4])}"]')
            else:
                if type_choice_1 == 3: 
                    print('\nFULL TYPE LIST\nChoice ONLY one and TYPE:\n')
                    for item_type in __Place_Types[4:]:
                        print(f' -> {__Place_Types.index(item_type)}   -   {item_type} <-')
                        sleep(__SLEEP_TIME_1)
                    type_choice_2 = -1
                    while type_choice_2 not in list(range(4, len(__Place_Types[4:]) + 1)):
                        try: type_choice_2 = int(input('\nWrite the number corresponding to the option you want\n\n >> '))
                        except Exception: print(f'\n[WRITE A NUMBER BETWEEN "4" AND "{len(__Place_Types)-1}"]')
                        else:
                            if type_choice_2 in list(range(4, len(__Place_Types))): return __Place_Types[type_choice_2]
                            else: print(f'\n[WRITE A NUMBER BETWEEN "4" AND "{len(__Place_Types)-1}"]')

                elif type_choice_1 in list(range(0, 4)): return __Place_Types[type_choice_1]
                else: print('\n[WRITE A NUMBER BETWEEN "0" AND "4"]')
    else:
        question = False
        while question != 1:
            try: question = int(input('\nDo you want to add a TYPE ?\n\n1  -  YES\n0  -  NO\n\n >> '))
            except Exception: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
            else:
                if question == 1: return get_type(True)
                elif not question: return False
                else: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')   
    

def app():
    stats = get_key()
    print(f'\nSTATS: {stats[0:2]}\n')
    if stats[0]:
        for line in __TITLE:
            sys.stderr.write(line)
            sleep(__SLEEP_TIME_1)
        gmaps = stats[2]
        address, lat, lng = get_address(gmaps)
        radius = get_radius()
        type_ = get_type(__REQUIERED_TYPE)
        if not type_: print('\nNo type filter selected ;-;')

        # locations = gmaps.places_nearby(location= (lat, lng), radius = radius)
    else: print(__OVER)


start = time()

if __name__ == "__main__": app()

end = time()
print(end - start)


