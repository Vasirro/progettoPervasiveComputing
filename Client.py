from requests import get, post
import time
base_url = 'http://localhost:8080'
with open ('Input.csv') as f:
    next(f)
    for r in f:
        r = r.strip()
        l = r.split(',')
        r = get(f'{base_url}/', data={'dati': l})
        print(r.status_code)
        print('sending',l)
        time.sleep(5)