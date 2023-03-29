from flask import Flask
from flask import request
from flask import send_file
from plotting import plot
from pathlib import Path
import module_sentiment
import module_arousal
import os
import openai


IP='127.0.0.1'
PORT='5000'
USER_AUDIO=Path('data','user_audio', 'user_tmp.wav').resolve()
PLOT_PATH = Path('data', 'plots', 'v_a_plot.png')
app=Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "Hello World"

@app.route('/api/audio', methods=['POST']) #endpoint definition
def register():
    #expected input: wav/str
    #expected output: png/jpeg

    valence=0.5
    arousal=0.5

    if request.method == 'POST':
        request.files['audio'].save(USER_AUDIO)
        user_turn=request.form.get('transcript')
        #user_turn=transcript_lst[-1]

        # valence processing
        v_analysis_out=module_sentiment.API(user_turn)
        print('valence analysis: ' + str(valence))
        print()

        # arousal processing
        a_analysis_out=module_arousal.API(USER_AUDIO)
        print('arousal analysis: ' + str(arousal))
        print()

        valence=float(v_analysis_out[1])
        arousal=float(a_analysis_out[1])
        plot.plt_va([valence], [arousal], str(PLOT_PATH))
        print('send back plot of user emotion')
        os.remove(USER_AUDIO)

        return send_file(PLOT_PATH, mimetype='image/png', as_attachment=True,
                         download_name='%s.jpg' % PLOT_PATH.name)
    else:
        print('there was no post request')




if __name__=='__main__':
    app.run(host=IP, port=PORT)