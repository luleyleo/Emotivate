import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


# neural networks:
#   - is a module
#   - comprises of modules (layers)
# modules subclass torch.nn.Module
# a mini-batch passed through the nn always maintains the first "batch-dimension"
# autograd:
#   calculating the gradient of the loss with respect to the parameters
#   normally "requires_grad=True" needed for gradient computation support of tensors
#   sometimes not needed, e.g. in case of:
#       -training finished (-->speedup computation)
#       -freeze several parameters
# switch autograd off:
#       with torch.no_grad():
#           pass
#       or
#       tensor=tensor.detach()

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

class NeuralNetwork(nn.Module):
    # required:
    # __init__, forward(self,x)
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(     # == ordered container of modules
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


# code from datasets
from torchvision import datasets
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import Lambda, ToTensor
import os


training_data = datasets.FashionMNIST(
    root="../data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

test_data = datasets.FashionMNIST(
    root="../data",
    train=False,
    download=True,
    transform=ToTensor()
)

# Define Loss fkt + Hyperparameter + optimizer
loss_fn = nn.CrossEntropyLoss()
learning_rate = 1e-3
batch_size = 64
epochs = 5
state_dict_path='../models/intro_pytorch/model_weights.pth'

model = NeuralNetwork()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)


# prepare dataset through dataloader --> iterable, batches, reshuffled after epochs
train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=True)

import torchvision.models as models
from pathlib import Path
if Path.is_file(Path(state_dict_path)):
    model.load_state_dict(torch.load(state_dict_path))
else:
    if not Path(state_dict_path).parent.exists():
        os.makedirs(Path(state_dict_path).parent)


for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")

torch.save(model.state_dict(), state_dict_path)





# device='cuda' if torch.cuda.is_available() else 'cpu'
# model = NeuralNetwork().to(device)
# print(model)
#
# X = torch.rand(1, 28, 28, device=device)
# logits = model(X)
# pred_probab = nn.Softmax(dim=1)(logits)
# y_pred = pred_probab.argmax(1)
# print(f"Predicted class: {y_pred}")