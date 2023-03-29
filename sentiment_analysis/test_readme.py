import csv
from pathlib import Path
from valence_recognition.module_NLPtools import tokenizeSentence
from go_emotions.run_goemotions import get_prediction_from_inputs

emo_dict={
"positive": ["amusement", "excitement", "joy", "love", "desire", "optimism", "caring", "pride", "admiration", "gratitude", "relief", "approval"],
"negative": ["fear", "nervousness", "remorse", "embarrassment", "disappointment", "sadness", "grief", "disgust", "anger", "annoyance", "disapproval"],
"ambiguous": ["realization", "surprise", "curiosity", "confusion"]
}
label_mapping={'0': 'ambiguous', '1': 'negative', '2': 'neutral', '3': 'positive'}

test_data_path=Path('go_emotions', 'data', 'group', 'test.tsv').resolve()
data = {}


with open(test_data_path, encoding='UTF-8') as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:

        # ambiguous==0, neutral==2, double-entries excluded
        if '0' not in row[1] and '2' not in row[1] and ',' not in row[1]:
            tokens = tokenizeSentence(row[0].lower().replace(',', '').replace('.', ''))
            #contains enough token?
            if len(tokens)>3:
                # if dict entry doesnt exist--> create list for it
                if row[1] not in data:
                    data[row[1]]=[]
                data[row[1]].append(row[0])


import module_sentiment

confusion_sustAGE={'true_1':0, 'false_1':0,
 'true_3':0, 'false_3':0}
confusion_goEmotions={'true_1':0, 'false_1':0,
 'true_3':0, 'false_3':0}


for neg_input in data['1']:

    # analysis from sustAGE
    v_analysis_out=module_sentiment.API(neg_input)
    if v_analysis_out[0]=='negative':
        confusion_sustAGE['true_1']+=1
    else:
        confusion_sustAGE['false_1'] += 1

    #analysis for goEmotions
    output=get_prediction_from_inputs([neg_input])
    max_prob=max(output[-1], key=lambda x:x['score'])
    if max_prob['label']=='negative':
        confusion_goEmotions['true_1'] += 1
    else:
        confusion_goEmotions['false_1'] += 1

for pos_input in data['3']:
    # analysis for sustAGE
    v_analysis_out=module_sentiment.API(pos_input)
    if v_analysis_out[0]=='positive':
        confusion_sustAGE['true_3']+=1
    else:
        confusion_sustAGE['false_3'] += 1

    #analysis for goEmotions
    output=get_prediction_from_inputs([pos_input])
    max_prob=max(output[-1], key=lambda x:x['score'])
    if max_prob['label']=='positive':
        confusion_goEmotions['true_3'] += 1
    else:
        confusion_goEmotions['false_3'] += 1

print(str(confusion_sustAGE))
print(str(confusion_goEmotions))












