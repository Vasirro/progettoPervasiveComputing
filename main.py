def save_data(request):
    from google.cloud import firestore
    import json
    if request.method == 'OPTIONS':
        print('------ options')
        # Allows GET and POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    msg = json.loads(request.values['data'])
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    print(msg)
    db = firestore.Client()
    db.collection(msg['sensor']).document(msg['time']).set({'time': msg['time'], 'use': msg['use[kW]'], 'gen':msg['gen[kW]'], 'house_overall':msg['House_overall[kW]'],
                                                             'dishwasher':msg['Dishwasher[kW]'], 'furnace1':msg['Furnace1[kW]'], 'furnace2':msg['Furnace2[kW]'],
                                                             'office':msg['Home_office[kW]'], 'fridge':msg['Fridge_[kW]'], 'wine_cellar':msg['Wine_cellar[kW]'],
                                                             'garage':msg['Garage_door[kW]'], 'kitchen1':msg['Kitchen1[kW]'], 'kitchen2':msg['Kitchen2[kW]'],
                                                             'kitchen3':msg['Kitchen1[kW]'], 'barn':msg['Barn[kW]'], 'well':msg['Well[kW]'], 'microwave':msg['Microwave[kW]'],
                                                             'living_room':msg['Living_room[kW]'], 'solar':msg['Solar[kW]'], 'temperature':msg['temperature'],
                                                             'icon':msg['icon'], 'humidity':msg['humidity'], 'visibility':msg['visibility'], 'summary':msg['summary'],
                                                             'apparentTemperature':msg['apparentTemperature'], 'pressure':msg['pressure'], 'windSpeed':msg['windSpeed'],
                                                             'cloudCover':msg['cloudCover'], 'windBearing':msg['windBearing'], 'precipIntensity':msg['precipIntensity'],
                                                             'dewPoint':msg['dewPoint'], 'precipProbability':msg['precipProbability']})



    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return 'ok'



