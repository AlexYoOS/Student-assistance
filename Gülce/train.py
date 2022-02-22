import torch
import argparse
from utils.trainig_fns import train_model, load_model
from utils.load_data import load_data
from torch.optim import Adam
import torch.nn as nn 

parser = argparse.ArgumentParser(description='train a nn for image classification.')
parser.add_argument('train_dir')
parser.add_argument('--device', default ="gpu")
parser.add_argument('--architecture', default = "vgg16")
parser.add_argument('--epochs', default = 25) # SEE BELOW, OR ALTERNATIVE ADD INSIDE ARGUMENT: "type=int"

args = parser.parse_args()
train_dir = args.train_dir
model_name = args.architecture
epochs = int(args.epochs) # LINE WAS RESULING IN ERROR, YOU DID NOT SPECIFY THE INPUT BEING AN INTEGER IN THE ARGPARSER, YOU CAN SOLVE THIS LIKE SO, OR SEE ABOVE IN THE ARGUMENT
device = args.device
train_load, val_load, test_load = load_data(train_dir)

model = load_model(model_name)
optimizer = Adam(model.classifier[6].parameters(), lr=0.0001) # LEARNING RATE HARDCUDED, BUT MUST BE SET FROM THE ARGPARSER, TOO
loss = nn.CrossEntropyLoss()

if device == "gpu":
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
else:
    device == "cpu"
train_model(model, loss, optimizer,train_load,val_load,device = device,num_epochs=epochs)