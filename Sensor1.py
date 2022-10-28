from requests import post
import time
import json
save_url = 'https://europe-west1-projectlv.cloudfunctions.net/save_data'
email_url = 'https://europe-west1-projectlv.cloudfunctions.net/email'
with open ('Input.csv') as f:
    next(f)
    for r in f:
        r = r.strip()
        t, useKW, generateKW, house_overallKW, dishwasherKW, furnace1KW, furnace2KW, officeKW, fridgeKW, wine_cellarKW, garage_doorKW, \
        kitchen1KW, kitchen2KW, kitchen3KW, barnKW, wellKW, microwaveKW, living_roomKW, solarKW, temperature, icon, humidity, visibility, \
        summary, apparentTemperature, pressure, windSpeed, cloudCover, windBearing, precipIntensity, dewPoint, precipProbability = r.split(',')
        r = post(save_url, data= {'data': json.dumps({'sensor':'sensor1', 'time':t, 'use[kW]':useKW, 'gen[kW]':generateKW, 'House_overall[kW]':house_overallKW,
             'Dishwasher[kW]':dishwasherKW, 'Furnace1[kW]':furnace1KW, 'Furnace2[kW]':furnace2KW, 'Home_office[kW]':officeKW,
             'Fridge_[kW]':fridgeKW, 'Wine_cellar[kW]':wine_cellarKW, 'Garage_door[kW]':garage_doorKW, 'Kitchen1[kW]':kitchen1KW,
             'Kitchen2[kW]':kitchen2KW, 'Kitchen3[kW]':kitchen3KW, 'Barn[kW]':barnKW, 'Well[kW]':wellKW, 'Microwave[kW]':microwaveKW,
             'Living_room[kW]':living_roomKW, 'Solar[kW]':solarKW, 'temperature':temperature, 'icon':icon, 'humidity':humidity,
             'visibility':visibility, 'summary':summary, 'apparentTemperature':apparentTemperature, 'pressure':pressure, 'windSpeed':windSpeed,
             'cloudCover':cloudCover, 'windBearing':windBearing, 'precipIntensity':precipIntensity, 'dewPoint':dewPoint, 'precipProbability':precipProbability})})
        print('save status:', r.status_code)
        r1 = post(email_url, data={'data': json.dumps({'sensor': 'sensor1', 'time': t, 'use[kW]': useKW, 'gen[kW]': generateKW, 'House_overall[kW]': house_overallKW,
             'Dishwasher[kW]': dishwasherKW, 'Furnace1[kW]': furnace1KW, 'Furnace2[kW]': furnace2KW, 'Home_office[kW]': officeKW,
             'Fridge_[kW]': fridgeKW, 'Wine_cellar[kW]': wine_cellarKW, 'Garage_door[kW]': garage_doorKW, 'Kitchen1[kW]': kitchen1KW,
             'Kitchen2[kW]': kitchen2KW, 'Kitchen3[kW]': kitchen3KW, 'Barn[kW]': barnKW, 'Well[kW]': wellKW, 'Microwave[kW]': microwaveKW,
             'Living_room[kW]': living_roomKW, 'Solar[kW]': solarKW, 'temperature': temperature, 'icon': icon, 'humidity': humidity,
             'visibility': visibility, 'summary': summary, 'apparentTemperature': apparentTemperature, 'pressure': pressure, 'windSpeed': windSpeed,
             'cloudCover': cloudCover, 'windBearing': windBearing, 'precipIntensity': precipIntensity, 'dewPoint': dewPoint, 'precipProbability': precipProbability})})
        print('email status:', r1.status_code)
        print('sending', t,useKW,generateKW,house_overallKW,dishwasherKW,furnace1KW,furnace2KW,officeKW,fridgeKW,wine_cellarKW,garage_doorKW,
        kitchen1KW,kitchen2KW,kitchen3KW,barnKW,wellKW,microwaveKW,living_roomKW,solarKW,temperature,icon,humidity,visibility,
        summary,apparentTemperature,pressure,windSpeed,cloudCover,windBearing,precipIntensity,dewPoint,precipProbability)
        time.sleep(10)

