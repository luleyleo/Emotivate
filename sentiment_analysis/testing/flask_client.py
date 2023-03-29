from pathlib import Path
import requests
import json

IP='127.0.0.1'
PORT='5000'
AUDIO_TEST=Path('../../app/src/main/res/raw/sample_audio.wav').resolve()


def send_audio():

    url = 'http://' + str(IP) + ':' + PORT + '/api/transcribe'

    with open(str(AUDIO_TEST), 'rb') as file:
        files = {'audio': file}

        req = requests.post(url, files=files)

        print(req.status_code)
        print(req.text)


def send_audio_and_transcript():

    url = 'http://' + str(IP) + ':' + PORT + '/api/audio'

    with open(str(AUDIO_TEST), 'rb') as file:
        data = {'transcript': 'I am meeting with friends in the afternoon and we are going to the cinema'}
        files = {'audio': file}

        req = requests.post(url, files=files, params=data)

        print(req.status_code)
        print(req.text)

if __name__=='__main__':
    send_audio()