from valence_recognition import config

import torch
import torch.nn as nn
import torch.nn.functional as F


class network_RNNandHA(nn.Module):

	def __init__(self, input_dim, output_dim):
		super(network_RNNandHA, self).__init__()


		torch.manual_seed(51)
		torch.cuda.manual_seed_all(51)

		self.gru = nn.GRU(input_dim, 128, num_layers=1, batch_first=False, bidirectional=True).float()

		self.attention = nn.Sequential(
			nn.Linear(256, config._sent_classes - 1, bias=True).float(),
			nn.Tanh().float()
		)

		self.context_vector = nn.Parameter(torch.empty(config._sent_classes - 1,256)).float()
		nn.init.xavier_uniform_(self.context_vector)

		self.layer_fullyConnected = nn.Sequential(
			nn.Dropout(p=0.3),
			nn.Linear(2*128, 32, bias=True).float(),
			nn.ReLU(),
			nn.Dropout(p=0.3),
			nn.Linear(32, output_dim, bias=True).float()
		)

		self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

		self.name = 'RNNandHA'

	def forward(self, X):

		output, _ = self.gru(X)

		output = output.view(X.shape[0], X.shape[1], 2, 128).reshape(X.shape[0], X.shape[1], -1)

		attentionLayer_output = self.attention(output.permute(1,0,2))
		attentionLayer_output_matmul = torch.matmul(attentionLayer_output.permute(1,0,2), self.context_vector)
		attention_scores = torch.softmax(torch.exp(attentionLayer_output_matmul), dim=0)
		
		hn = torch.sum(attention_scores * output, 0, keepdim=True)

		y_hat = self.layer_fullyConnected(hn.permute(1,0,2))

		return y_hat
