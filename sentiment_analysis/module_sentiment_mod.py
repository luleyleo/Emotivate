import os
import sys
import pdb
sys.path.append('src')

import random
import time

import torch
from torch import load

from valence_recognition_mod.module_NLPtools import tokenizeSentence, extractEmbeddings
from valence_recognition_mod.network_sentiment import network_RNNandHA

from valence_recognition import config
from pathlib import Path
import json
from copy import deepcopy
from torch import nn

modelStoredPath = 'BinarySentimentModel_RNNandHA.pth'
storagePath = Path('valence_recognition_mod','Models_Sentiment')

# load network, initialize and remove last sequential layer
model = network_RNNandHA(config._embeddings_dim, config._sent_classes)
model.load_state_dict(load(os.path.join(storagePath, modelStoredPath)))
model.layer_fullyConnected=torch.nn.Sequential(*(list(deepcopy(model.layer_fullyConnected).children())[:-1]))
model.eval()

# for layer in model.layer_fullyConnected.modules():
#    b=layer

with open(os.path.join(storagePath, 'MOSEI_GloVe_300d' + '.json')) as f:
	embeddingsDict = json.load(f)


def API(sentence):
	global model

	tokens = tokenizeSentence(sentence.lower().replace(',','').replace('.',''))

	if len(tokens) >= 3:
		embeddings = extractEmbeddings(tokens, info = False)
		with torch.no_grad():
			net_out=model(embeddings)
			return net_out

if __name__=='__main__':
	API("I hate programming with python and its sad that it always crashes")