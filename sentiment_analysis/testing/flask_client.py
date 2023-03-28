from pathlib import Path
import requests
import json

IP='127.0.0.1'
PORT='5000'
AUDIO_TEST=Path('..','data', 'datasets','emo_db', 'wav', '03a05Wb.wav').resolve()


def send_audio():

    url = 'http://' + str(IP) + ':' + PORT + '/api/audio'

    with open(str(AUDIO_TEST), 'rb') as file:
        data = {'transcript': 'I am meeting with friends in the afternoon and we are going to the cinema'}
        files = {'audio': file}

        req = requests.post(url, files=files, params=data)

        print(req.status_code)
        print(req.text)

if __name__=='__main__':
    send_audio()