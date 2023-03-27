import os
from numpy import asarray
import json
from torch import zeros, Tensor

import pdb

from valence_recognition import config

import torchtext
from torchtext.data import get_tokenizer


def tokenizeSentence(sentence):

	tokenizer = get_tokenizer(None)
	tokens = tokenizer(sentence.replace('&#39;','\''))

	return tokens


def extractEmbeddings(tokens, embeddingsDictFileName, path, info = True):

	if info: print('[MSG] Loading embeddings ...')

	with open(os.path.join(path, embeddingsDictFileName + '.json')) as f:
		embeddingsDict = json.load(f)

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
