import os
from numpy import asarray
import json
from torch import zeros, Tensor

import pdb

from valence_recognition import config

import torchtext
from torchtext.data import get_tokenizer
from pathlib import Path


def tokenizeSentence(sentence):

	tokenizer = get_tokenizer(None)
	tokens = tokenizer(sentence.replace('&#39;','\''))

	return tokens


def extractEmbeddings(tokens, info = True):
	from module_sentiment_mod import embeddingsDict

	if info: print('[MSG] Loading embeddings ...')

	if info:  print('[MSG] Initialising embeddings ...')
	
	embeddings = zeros((min(config._max_seqLen, len(tokens)), 1, config._embeddings_dim))

	for ID, token in enumerate(tokens):

		if token in embeddingsDict.keys():
			embeddings[ID,:,:] = Tensor(asarray(embeddingsDict[token]))

		else:
			print('[ERROR] Unrecognised token {}'.format(token))

		if (ID + 1) == config._max_seqLen:
			break
	
	return embeddings
