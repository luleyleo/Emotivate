# import module_sentiment as sentiment
# a=sentiment.API('I am meeting with friends in the afternoon and we are going to the cinema')
#
# print('valence analysis: ' + str(a))
#
# print()
#
#
# import module_arousal as arousal
# from pathlib import Path
# audio_path=Path('data','emo_db', '03a05Wb.wav').resolve()
# a=arousal.API(audio_path)
#
# print('arousal analysis: ' + str(a))
# print()

from plotting import plot
from pathlib import Path
img_path=Path('data', 'plots', 'v_a_plot.png')
plot.plt_va([0.5,0.3],[0.3,0.4],img_path.__str__())


