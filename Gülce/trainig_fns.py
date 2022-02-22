import torchvision
import torch
import torch.nn as nn
def load_model(model_name):
    #try:
    model = eval("torchvision.models.{}".format(model_name))
    model = model(pretrained = False)
        
    for param in model.parameters():
        param.requires_grad = False
        
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, 102)
    #except:
       # print("model doesn’t exist")

    return model


def train_model(model, criterion, optimizer, train_loader, val_loader, device, num_epochs=25):
   
     # Set model to training mode


    for epoch in range(num_epochs):
        model.train() 
        model.to(device) # MODEL AND DATA MUST BOTH BE SET TO DEVICE, SO THAT THEY ARE ON THE SAME MACHINE, THIS IS THE MAJOR ISSUE OF THIS ERROR
        print('Epoch {}/{}'.format(epoch, num_epochs)) # THIS LINE IS CHANGED, YOU INCORRECT SET (NUM_EPOCHS - 1) WHICH RESULTS IN WRONG STATICTICS
        print('-' * 10)
        

        # Each epoch has a training and validation phase
        
        running_loss = 0.0
        running_corrects = 0.0
        val_loss = 0.0
        val_corrects = 0.0
            

            # Iterate over data.
        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

                # zero the parameter gradients
            optimizer.zero_grad()
                
            outputs = model(inputs)
            _, preds = torch.max(outputs.data, 1)
        
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            
                # statistics
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)


        epoch_loss = running_loss / len(train_loader)
        epoch_acc = running_corrects / len(train_loader)

        print('Epoch Loss: {}'.format(epoch_loss))
        print('Epoch accurecy: {}'.format(epoch_loss))

        model.eval()
        for inputs, labels in val_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)

                # zero the parameter gradients
            optimizer.zero_grad()
                
            outputs = model_ft(inputs) ## VARIABLE NAMING ERROR - PLEASE WORK FROM HERE ON BY YOURSELF AND SOLVE PROBLEM
                
            vloss = criterion(outputs, labels)
            
            val_loss += vloss.item() * inputs.size(0)
            val_corrects += torch.sum(preds == labels.data)

            
            
        total_val_loss = val_loss / len(val_loader)
        total_val_acc = val_corrects / len(val_loader)

        
        print('validation Loss: {}'.format(total_val_loss))
        print('validation Loss: {}'.format(total_val_loss))


    return model

