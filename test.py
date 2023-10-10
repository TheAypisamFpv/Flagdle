# small program to use, and display all country from countries.geojson using cv2
# create a image with all borders of countries
# example of one country:
# { "type": "Feature", "properties": { "ADMIN": "Aruba", "ISO_A3": "ABW" }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -69.936390753999945, 12.531724351000051 ], [ -69.924672003999945, 12.519232489000046 ], [ -69.915760870999918, 12.497015692000076 ], [ -69.880197719999842, 12.453558661000045 ], [ -69.876820441999939, 12.427394924000097 ], [ -69.888091600999928, 12.417669989000046 ], [ -69.908802863999938, 12.417792059000107 ], [ -69.930531378999888, 12.425970770000035 ], [ -69.945139126999919, 12.44037506700009 ], [ -69.924672003999945, 12.44037506700009 ], [ -69.924672003999945, 12.447211005000014 ], [ -69.958566860999923, 12.463202216000099 ], [ -70.027658657999922, 12.522935289000088 ], [ -70.048085089999887, 12.531154690000079 ], [ -70.058094855999883, 12.537176825000088 ], [ -70.062408006999874, 12.546820380000057 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } }

import cv2
import numpy as np
import json

# read geojson file
with open('countries.geojson') as f:
    data = json.load(f)


countries = {}


DEFAULT_SIZE = (18000, 36000)
SIZE = .3
SCALED_SIZE = (int(DEFAULT_SIZE[0]/SIZE), int(DEFAULT_SIZE[1]/SIZE))

# for coord in feature['geometry']['coordinates']:
#     for i in range(len(coord)):
#         if type(coord[i][0]) == list:
#             for j in range(len(coord[i])):
#                 x = int((coord[i][j][0]+180)*5)-1
#                 y = int((-coord[i][j][1]+90)*5)-1
#                 img[y, x] = (255, 255, 255)
#         else:
#             x = int((coord[i][0]+180)*5)-1
#             y = int((-coord[i][1]+90)*5)-1
#             img[y, x] = (255, 255, 255)

        


# create a image with all borders of countries
img = np.zeros((SCALED_SIZE[0], SCALED_SIZE[1], 3), np.uint8)
# cv2.imshow('img', img)
for feature in data['features']:
    countries[feature['properties']['ADMIN']] = feature['geometry']['coordinates']
            


# save all country as images with the right size (16:9 aspect ration)
for country in countries:
    pixels = 0
    img = np.zeros((SCALED_SIZE[0], SCALED_SIZE[1], 3), np.uint8)
    for coord in countries[country]:
        for i in range(len(coord)):
            if type(coord[i][0]) == list:
                for j in range(len(coord[i])):
                    pixels +=1
                    x = int((coord[i][j][0]+180)*int(10/SIZE))-1
                    y = int((-coord[i][j][1]+90)*int(10/SIZE))-1
                    img[y, x] = (255, 255, 255)
            else:
                pixels +=1
                x = int((coord[i][0]+180)*int(10/SIZE))-1
                y = int((-coord[i][1]+90)*int(10/SIZE))-1
                img[y, x] = (255, 255, 255)

    # don't save images with too little data
    if pixels < 300:
        print('❌ skipped', country)
        continue

    # crop to only contain the country, with a bit of padding
    #  find the min and max x and y
    min_x = 100_000_000
    min_y = 100_000_000
    max_x = 0
    max_y = 0

    for coord in countries[country]:
        for i in range(len(coord)):
            if type(coord[i][0]) == list:
                for j in range(len(coord[i])):
                    x = int((coord[i][j][0]+180)*int(10/SIZE))-1
                    y = int((-coord[i][j][1]+90)*int(10/SIZE))-1
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y < min_y:
                        min_y = y
                    if y > max_y:
                        max_y = y
            else:
                x = int((coord[i][0]+180)*int(10/SIZE))-1
                y = int((-coord[i][1]+90)*int(10/SIZE))-1
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y

    # add padding
    min_x -= 10 if min_x > 10 else min_x
    max_x += 10 if max_x < SCALED_SIZE[1]-10 else SCALED_SIZE[1]-max_x
    min_y -= 10 if min_y > 10 else min_y
    max_y += 10 if max_y < SCALED_SIZE[0]-10 else SCALED_SIZE[0]-max_y

    # crop
    img = img[min_y:max_y, min_x:max_x]
    # resize
    
    cv2.imwrite('country/'+country+'.png', img)
    print("✅",country)