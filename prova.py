from requests import get, post
import time
base_url = 'http://localhost:8080'
with open ('Input.csv') as f:
    next(f)
    for r in f:
        r = r.strip()
        t,useKW,generateKW,house_overallKW,dishwasherKW,furnace1KW,furnace2KW,officeKW,fridgeKW,wine_cellarKW,garage_doorKW,\
        kitchen1KW,kitchen2KW,kitchen3KW,barnKW,wellKW,microwaveKW,living_roomKW,solarKW,temperature,icon,humidity,visibility,\
        summary,apparentTemperature,pressure,windSpeed,cloudCover,windBearing,precipIntensity,dewPoint,precipProbability= r.split(',')
        r = get(f'{base_url}/sensors/sensors1', data={'time':t, 'use[kW]':useKW, 'gen[kW]':generateKW, 'House_overall[kW]':house_overallKW,
             'Dishwasher[kW]':dishwasherKW, 'Furnace1[kW]':furnace1KW, 'Furnace2[kW]':furnace2KW, 'Home_office[kW]':officeKW,
             'Fridge_[kW]':fridgeKW, 'Wine_cellar[kW]':wine_cellarKW, 'Garage_door[kW]':garage_doorKW, 'Kitchen1[kW]':kitchen1KW,
             'Kitchen2[kW]':kitchen2KW, 'Kitchen3[kW]':kitchen3KW, 'Barn[kW]':barnKW, 'Well[kW]':wellKW, 'Microwave[kW]':microwaveKW,
             'Living_room[kW]':living_roomKW, 'Solar[kW]':solarKW, 'temperature':temperature, 'icon':icon, 'humidity':humidity,
             'visibility':visibility, 'summary':summary, 'apparentTemperature':apparentTemperature, 'pressure':pressure, 'windSpeed':windSpeed,
             'cloudCover':cloudCover, 'windBearing':windBearing, 'precipIntensity':precipIntensity, 'dewPoint':dewPoint, 'precipProbability':precipProbability})
        print(r.status_code)
        print('sending -->',t,useKW,generateKW,house_overallKW,dishwasherKW,furnace1KW,furnace2KW,officeKW,fridgeKW,wine_cellarKW,garage_doorKW,
        kitchen1KW,kitchen2KW,kitchen3KW,barnKW,wellKW,microwaveKW,living_roomKW,solarKW,temperature,icon,humidity,visibility,
        summary,apparentTemperature,pressure,windSpeed,cloudCover,windBearing,precipIntensity,dewPoint,precipProbability)
        time.sleep(10)









with open ('Input.csv') as f:
    campi = ['time', 'use[kW]', 'gen[kW]', 'House_overall[kW]', 'Dishwasher[kW]', 'Furnace1[kW]', 'Furnace2[kW]',
             'Home_office[kW]', 'Fridge_[kW]', 'Wine_cellar[kW]', 'Garage_door[kW]', 'Kitchen1[kW]', 'Kitchen2[kW]',
             'Kitchen3[kW]', 'Barn[kW]', 'Well[kW]', 'Microwave[kW]', 'Living_room[kW]', 'Solar[kW]', 'temperature',
             'icon', 'humidity', 'visibility', 'summary', 'apparentTemperature', 'pressure', 'windSpeed', 'cloudCover',
             'windBearing', 'precipIntensity', 'dewPoint', 'precipProbability']
    next(f)
    for r in f:
        r = r.strip()
        l = r.split(',')
        var = {}
        for i in range(len(campi)):
            var[campi[i]] = l[i]
        #r = get(f'{base_url}/', data=var)
        r = post(function_url, data = var)
        print(r.status_code)
        print('sending', var)
        time.sleep(5)