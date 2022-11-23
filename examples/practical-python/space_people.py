import json
import urllib.request

url = 'http://api.open-notify.org/astros.json'

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    if data['message'] == 'success':
        count = data['number']
        print(f'There are currently {count} people in space:\n')
        for person in data['people']:
            print(person['name'])
    else:
        print('The response does not contain valid data.')
except Exception as e:
    print(f"Unable to load data. {str(e)}")