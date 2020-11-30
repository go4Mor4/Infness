import googlemaps
import googletrans
# ty google :)

import argparse
from time import sleep, time
import sys
import itertools
import threading
import pandas as pd

parser = argparse.ArgumentParser(description='Parser that gets google maps key.')
parser.add_argument('--key', '-k', type=str, help='Put your google maps key.', default=False)
args = parser.parse_args()

pd.set_option('display.max_columns', None, 'display.max_rows', None)

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
__SLEEP_TIME_3 = 2
__SLEEP_TIME_4 = 0.1
__SLEEP_TIME_5 = 1
__REQUIRED_TYPE = False
__REQUIRED_RADIUS = True

__Bad_Types = ['locality']
__Place_Types = ['establishment', 'department_store', 'accounting', '[more]', 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'atm', 'bakery', 'bank', 'bar', 'beauty_salon', 'bicycle_store', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetery', 'church', 'city_hall', 'clothing_store', 'convenience_store', 'courthouse', 'dentist', 'doctor', 'drugstore', 'electrician', 'electronics_store', 'embassy', 'fire_station', 'florist', 'funeral_home', 'furniture_store', 'gas_station', 'gym', 'hair_care', 'hardware_store', 'hindu_temple', 'home_goods_store', 'hospital', 'insurance_agency', 'jewelry_store', 'laundry', 'lawyer', 'library', 'light_rail_station', 'liquor_store', 'local_government_office', 'locksmith', 'lodging', 'meal_delivery', 'meal_takeaway', 'mosque', 'movie_rental', 'movie_theater', 'moving_company', 'museum', 'night_club', 'painter', 'park', 'parking', 'pet_store', 'pharmacy', 'physiotherapist', 'plumber', 'police', 'post_office', 'primary_school', 'real_estate_agency', 'restaurant', 'roofing_contractor', 'rv_park', 'school', 'secondary_school', 'shoe_store', 'shopping_mall', 'spa', 'stadium', 'storage', 'store', 'subway_station', 'supermarket', 'synagogue', 'taxi_stand', 'tourist_attraction', 'train_station', 'transit_station', 'travel_agency', 'university', 'veterinary_care', 'zoo']
__Additional_Types = ['administrative_area_level_1', 'administrative_area_level_2', 'administrative_area_level_3', 'administrative_area_level_4', 'administrative_area_level_5', 'archipelago', 'colloquial_area', 'continent', 'country', 'finance', 'floor', 'food', 'general_contractor', 'geocode', 'health', 'intersection', 'locality', 'natural_feature', 'neighborhood', 'place_of_worship', 'plus_code', 'point_of_interest', 'political', 'post_box', 'postal_code', 'postal_code_prefix', 'postal_code_suffix', 'postal_town', 'premise', 'room', 'route', 'street_address', 'street_number', 'sublocality', 'sublocality_level_1', 'sublocality_level_2', 'sublocality_level_3', 'sublocality_level_4', 'sublocality_level_5', 'subpremise', 'town_square']
__ptBR_Place_Types = ['estabelecimento', 'loja_de_partamento', 'contabilidade', 'aeroporto', 'parque de diversões', 'aquário', 'galeria de arte', 'caixa eletrônico', 'padaria', 'banco', ' bar ',' beauty_salon ',' bike_store ',' book_store ',' bowling_alley ',' bus_station ',' cafe ',' campground ',' car_dealer ',' car_rental ',' car_repair ',' car_wash ',' casino ' , 'cemitério', 'igreja', 'salão da cidade', 'loja de roupas', 'loja de conveniência', 'tribunal', 'dentista', 'médico', 'drogaria', 'eletricista', 'loja de eletrônicos', 'embaixada', ' posto de bombeiros ',' florista ',' funeral_home ',' loja_de_móveis ',' posto_de_gasolina ',' ginásio ',' cuidados_cabelo ',' loja_de_ferramentas ',' templo_mundo ',' loja_de_destinos_de_ casa ',' hospital ',' agência_seguro ','loja de joias' , 'lavanderia', 'advogado', 'biblioteca', 'light_rail_station', 'liquor_store', 'local_government_office', 'chaveiro', 'hospedagem', 'meal_delivery', 'meal_takeaway', 'mesquita', 'movie_rental', ' movie_theater ',' moving_company ',' museum ',' night_club ',' painter ',' park ',' parking ',' pet_store ',' pharmacy ',' phys ioterapeuta ',' encanador ',' polícia ',' agência postal ',' escola_primária ',' agência_real_estado ',' restaurante ',' contratante_de_tratamento ',' parque_vir_vista ',' escola ',' escola_secundária ',' loja de sapatos ',' pequeno_projeto ' , 'spa', 'stadium', 'storage', 'store', 'metrway_station', 'supermercado', 'synagogue', 'taxi_stand', 'tourist_attraction', 'train_station', 'transit_station', 'travel_agency', ' universidade ',' veterinary_care ',' zoo ']
__Translate_tags = zip(__Place_Types, __ptBR_Place_Types)
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
        sleep(__SLEEP_TIME_4)
    sys.stdout.write('\r[Done!      ]')


def common_items(x, y):
   common = 0
   for value in x:
      if value in y: common = 1
   if not common: return False
   else: return True


def get_key():
    if not __KEY: return [False, 'Key has not been assigned.']
    else:
        try: gmaps = googlemaps.Client(key=args.key)
        except: return [False, 'Invalid key.']
        else: return [True, 'Valid key.', gmaps]


def get_address(gmaps):
    address = input('\nProvide an address\n >> ')
    t = threading.Thread(target=animate)
    t.start()
    place_data = gmaps.geocode(address)
    global done
    done = True
    sleep(1)
    if place_data:
        question = False
        formatted_address = place_data[0].get("formatted_address")
        print(f'\n\n That is the correct address ?\n -> {formatted_address}\n\n1  -  YES\n0  -  NO\n')
        while question != 1:
            try: question = int(input(' >> '))
            except:
                print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
                continue
            else:
                if question == 1: return place_data[0].get('geometry').get('location').get('lat'), place_data[0].get('geometry').get('location').get('lng')
                elif not question: return get_address(gmaps)
                else: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
    else:
        print('\nInvalid address, try again!')
        return get_address(gmaps)


def get_radius(required):
    if required:
        options, values = ['1 KM', '3 KM', '5 KM', '10 KM'], [1000, 3000, 5000, 10000]
        print('\n==============================\nGET RADIUS:\n')
        for n in options:
            print(f'{options.index(n)}   -   {n}')
            sleep(__SLEEP_TIME_2)
        radius_choice = -1
        print('\nWrite the number corresponding to the radius you want\n')
        while radius_choice not in list(range(len(options))):
            try: radius_choice = int(input(' >> '))
            except: print('[WRITE A NUMBER BETWEEN "1" AND "8"]')
            else:
                if radius_choice in list(range(1, 8)):
                    print(f'\n[SELECTED OPTION: { options[radius_choice]}]')
                    sleep(__SLEEP_TIME_2)
                    return values[radius_choice]
                else: print('\n[WRITE A NUMBER BETWEEN "1" AND "8"]')
    else:
        question = False
        while question != 1:
            try: question = int(input('\nDo you want to add a RADIUS ?\n\n1  -  YES\n0  -  NO\n\n >> '))
            except: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
            else:
                if question == 1: return get_type(True)
                elif not question: return False
                else: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')


def get_type(required):
    if required:
        print('\n==============================\nGET TYPE:\n\n Choice one and type correspondent number:\n')
        for n in __Place_Types[:4]:
            print(f' -> {__Place_Types.index(n)}   -   {n} <-')
            sleep(__SLEEP_TIME_2)
        type_choice_1 = -1
        while type_choice_1 not in list(range(len(__Place_Types[:4]))):
            try: type_choice_1 = int(input('\nWrite the number corresponding to the option you want\n\n >> '))
            except: print(f'[WRITE A NUMBER BETWEEN "0" AND "{len(__Place_Types[:4])}"]')
            else:
                if type_choice_1 == 3: 
                    print('\nFULL TYPE LIST\nChoice ONLY one and TYPE:\n')
                    for item_type in __Place_Types[4:]:
                        print(f' -> {__Place_Types.index(item_type)}   -   {item_type} <-')
                        sleep(__SLEEP_TIME_1)
                    type_choice_2 = -1
                    while type_choice_2 not in list(range(4, len(__Place_Types[4:]) + 1)):
                        try: type_choice_2 = int(input('\nWrite the number corresponding to the option you want\n\n >> '))
                        except: print(f'\n[WRITE A NUMBER BETWEEN "4" AND "{len(__Place_Types)-1}"]')
                        else:
                            if type_choice_2 in list(range(4, len(__Place_Types))): return __Place_Types[type_choice_2]
                            else: print(f'\n[WRITE A NUMBER BETWEEN "4" AND "{len(__Place_Types)-1}"]')

                elif type_choice_1 in list(range(0, 4)): return __Place_Types[type_choice_1]
                else: print('\n[WRITE A NUMBER BETWEEN "0" AND "4"]')
    else:
        question = False
        while question != 1:
            try: question = int(input('\nDo you want to add a TYPE ?\n\n1  -  YES\n0  -  NO\n\n >> '))
            except: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')
            else:
                if question == 1: return get_type(True)
                elif not question: return False
                else: print('\n[ANSWER ONLY WITH "1" OR "0"!]', end='')


def cleaner(data):
    new_data, nomes, enderecos, tags, aberto_agora, ratings, ceps, telefones, website = [], [], [], [], [], [], [], [], []

    next_page_token = data.get('next_page_token')

    while True:
        for result in data.get('results'):
            if not common_items(result.get('types'), __Bad_Types): new_data.append(result)
        if not next_page_token: break
        sleep(__SLEEP_TIME_3)
        data = gmaps.places_nearby(page_token=str(next_page_token))
        next_page_token = data.get('next_page_token', False)


    for i in new_data:
        nomes.append(i.get('name', 'NA'))
        enderecos.append(i.get('vicinity', 'NA'))
        tags.append(i.get('types', 'NA'))
        aberto_agora.append(i.get('opening_hours', {}).get('open_now', 'NA'))
        ratings.append(i.get('rating', 'NA'))

        result = gmaps.place(i.get('place_id')).get('result')
        ceps.append(result.get('address_components', {})[-1].get('long_name', 'NA'))
        telefones.append(result.get('formatted_phone_number', 'NA'))
        website.append(result.get('website', 'NA'))

    translator = googletrans.Translator()

    #tags = [[(translator.translate(item, dest='pt')).text for item in t] for t in tags]

    return list(zip(nomes, enderecos, telefones, aberto_agora, ratings, ceps, website, tags))


def format_output(df):
    writer = pd.ExcelWriter("output4.xlsx", engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Dados Coletados', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Dados Coletados']
    worksheet.set_zoom(90)

    for idx, col in enumerate(df.columns):
        series = df[col]
        max_len = max((series.astype(str).map(len).max(), len(str(series.name)))) + 1
        worksheet.set_column(idx, idx, max_len)


    writer.save()


def app():
    stats = get_key()
    print(f'\nSTATS: {stats[0:2]}\n')
    if stats[0]:
        for line in __TITLE:
            sys.stderr.write(line)
            sleep(__SLEEP_TIME_1)
        global gmaps
        gmaps = stats[2]
        lat, lng = get_address(gmaps)
        radius = get_radius(__REQUIRED_RADIUS)
        type_ = get_type(__REQUIRED_TYPE)

        if not type_: print('\nNo type filter selected.')
        else: print(f'Type filter selected: {type_}')

        global done
        done = False
        t = threading.Thread(target=animate)
        t.start()

        try: locations = gmaps.places_nearby(location=(lat, lng), radius=radius, language='pt-BR')
        except Exception as e: return [False, f'FAIL IN "PLACES_NEARBY" FUNCTION EXECUTION\n{e}']
        else:
            cleared_data = cleaner(locations)
            df = pd.DataFrame(cleared_data, columns=['Nome', 'Endereço', 'Telefone', 'Aberto agora?', 'Rating', 'CEP', 'Website', 'Tags'])
            format_output(df)

        done = True
        sleep(__SLEEP_TIME_5)
        return [True]
    else:
        print(__OVER)
        return [False]



start = time()

if __name__ == "__main__":
    r = app()[0]
    if not r:
        done = True
        raise Exception
    print(r)



end = time()

print(f'\n  ~ PROCESS TIME - {end - start} SECONDS')




