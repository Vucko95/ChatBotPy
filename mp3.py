import requests
url = 'https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3'

req = requests.get(url)
content = req.content
# print(req.content)
with open('file.mp3', 'wb') as file:
    file.write(content)
