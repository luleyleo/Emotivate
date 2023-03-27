import os
import sys
import pdb
sys.path.append('src')

import random
import time

import torch
from torch import load
import torch.nn.functional as F

from valence_recognition.module_NLPtools import tokenizeSentence, extractEmbeddings
from valence_recognition.network_sentiment import network_RNNandHA

from valence_recognition import config


def infer_sentiment(model, embeddings):

	model.eval()

	with torch.no_grad():
		y_hat = model(embeddings)

	probs = F.softmax(y_hat, dim=2)

	confidence = torch.max(probs, dim=2)[0].item()

	pred = torch.argmax(y_hat, dim=2)

	if pred.item() == 0: label = 'negative'
	
	elif pred.item() == 1: label = 'positive'	

	return label, confidence


def API(sentence):
	from pathlib import Path
	storagePath = Path('valence_recognition','Models_Sentiment')

	tokens = tokenizeSentence(sentence.lower().replace(',','').replace('.',''))

	if len(tokens) >= 3:

		embeddings = extractEmbeddings(tokens, 'MOSEI_GloVe_300d', storagePath, info = False)

		modelStoredPath = 'BinarySentimentModel_RNNandHA.pth'

		model = network_RNNandHA(config._embeddings_dim, config._sent_classes)
		model.load_state_dict(load(os.path.join(storagePath, modelStoredPath)))

		label, confidence = infer_sentiment(model, embeddings)	

		confidence = '{:.3f}'.format(confidence)

		return label, confidence

	else:
		raise Exception("Sorry, the input sentence requires at least 3 tokens")
