import module_sentiment as sentiment
a=sentiment.API('I am meeting with friends in the afternoon and we are going to the cinema')
#
# print('valence analysis: ' + str(a))
#
# print()

import module_arousal as arousal
from pathlib import Path
audio_path=Path('data','emo_db', '03a05Wb.wav')
if audio_path.is_file():
    print("is file")
else:
    print(audio_path)

audio_path=audio_path.resolve()
arousal.API(audio_path)

print()
print()