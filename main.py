def graph(request):
    from flask import render_template
    from google.cloud import firestore
    import json

    def read_all(sensor, typeData):
        db = firestore.Client()
        data = []
        for doc in db.collection(sensor).stream():
            x = doc.to_dict()
            data.append([x['time'].split(' ')[0], float(x[typeData])])
        return json.dumps(data)

    sensor = request.values['sensor']
    typeData = request.values['typedata']
    data = json.loads(read_all(sensor, typeData))
    data.insert(0, ['time', typeData])
    return render_template('graph.html', data=data)