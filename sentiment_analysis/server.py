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


openai.api_key = os.getenv("OPENAI_API_KEY")


app=Flask(__name__)
valence_map = {
    'positive': 1,
    'negative': -1,
}
arousal_map = {
    'high': 1,
    'mid': 0,
    'low': -1,
}


@app.route('/api/test', methods=['GET'])
def test():
    return "Hello World"


@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    request.files['audio'].save(USER_AUDIO)

    audio_file = USER_AUDIO.open('rb')
    transcript = openai.Audio.transcribe('whisper-1', audio_file)["text"]

    audio_file.close()

    return transcript


@app.route('/api/valence_and_arousal', methods=['POST']) #endpoint definition
def valence_and_arousal():
    #expected input: wav/str
    #expected output: png/jpeg

    valence = 0.5
    arousal = 0.5

    request.files['audio'].save(USER_AUDIO)
    user_turn = request.form.get('transcript')

    print('analyzing text:', user_turn)

    # valence processing
    v_analysis_out = module_sentiment.API(user_turn)
    print('valence analysis: ' + str(v_analysis_out))

    # arousal processing
    a_analysis_out = module_arousal.API(USER_AUDIO)
    print('arousal analysis: ' + str(a_analysis_out))

    #valence = valence_map[v_analysis_out[0]] * float(v_analysis_out[1])
    #arousal = arousal_map[a_analysis_out[0]] * float(a_analysis_out[1])

    #plot.plt_va([valence], [arousal], str(PLOT_PATH))

    os.remove(USER_AUDIO)

    print('sending back plot of user emotion')
    return f'{v_analysis_out[0]},{a_analysis_out[0]}'
    #return send_file(PLOT_PATH, mimetype='image/png', as_attachment=True, download_name='%s.jpg' % PLOT_PATH.name)


if __name__=='__main__':
    app.run(host=IP, port=PORT)