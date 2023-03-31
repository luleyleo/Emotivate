# Emotivate

Introducing Emotivate, the ultimate mood-matching app that helps you navigate your emotions with ease. With Emotivate, you can tell your story and let the app analyze your mood. Then, based on your current emotional state, Emotivate suggests a variety of activities and actions to help you feel better. Whether you're feeling sad, anxious, or angry, Emotivate has got you covered with personalized suggestions that match your mood. From cute animal pictures to games that let you vent your frustration, Emotivate has something for everyone. Download Emotivate now and take control of your emotions like never before.

## Structure

```
.
├── app                         Android app
└── sentiment_analysis          Server related code
    ├── server.py               Entrypoint for the server
    ├── test_readme.py          Run comparison between GoEmotions and sustAGE models
    ├── test_readme_results.py  Contains results and creates plot
    ├── module_sentiment.py     sustAGE model for valence analysis
    ├── module_arousal.py       sustAGE model for arousal detection
    ├── go_emotions             GoEmotions pre-built model
    ├── data                    Outputs such as plots
    └── FIPsustAGE3.yml         Conda environment file for the server
```

## How to run

Run the server:
```sh
$ cd sentiment_analysis
$ conda create -f FIPsustAGE3.yml
$ conda activate FIPsustAGE
$ python server.py
```

Make the server available:
```sh
ngrok http 5000
```

Run the app:
- Open `.` in Android Studio
- Copy `ngrok` url into `Client.kt` file
- Run the app