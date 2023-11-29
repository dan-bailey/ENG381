## This script pulls random words from the API and writes them to a text file.

import requests
import json

api_url = 'https://api.api-ninjas.com/v1/randomword'

i = 1
while i <= 98700:
    response = requests.get(api_url, headers={'X-Api-Key': '75Us4M60+0IDLyhiQEAKOg==uaQqTNZeVu89ulCM'})
    if response.status_code == requests.codes.ok:
        output = json.loads(response.text)
        dumpit = output['word']
        print(dumpit)
        with open("./text_files/random.txt", "a") as f:
            f.write(dumpit)
            f.write('\n')
    else:
        print("Error:", response.status_code, response.text)
    i+=1