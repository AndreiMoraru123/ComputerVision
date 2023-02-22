# TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # TODO: Define all the layers of this CNN, the only requirements are:
        # 1. This network takes in a square (same width and height), grayscale image as input
        # 2. It ends with a linear layer that represents the keypoints
        # it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs

        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel

        # (W-F)/S + 1 = (224 - 5)/1 + 1 = 219, passed through max pool => 219//2 = 109
        # 222 // 2 = 111
        self.conv1 = nn.Conv2d(1, 32, 5)

        I.kaiming_normal_(self.conv1.weight)

        # Max Pool
        self.pool = nn.MaxPool2d(2, 2)

        # (W-F)/S + 1 = (109 - 5)/1 + 1 = 105, passed through max pool => 105//2 = 52
        # 109 // 2 = 54
        self.conv2 = nn.Conv2d(32, 64, 5)

        I.kaiming_normal_(self.conv2.weight)

        # (W-F)/S + 1 = (52 - 5)/1 + 1 = 48, passed through max pool => 48//2 = 24
        # 52 // 2 = 26
        self.conv3 = nn.Conv2d(64, 128, 5)

        I.kaiming_normal_(self.conv3.weight)

        # (W-F)/S + 1 = (24 - 5)/1 + 1 = 20, passed through max pool => 20//2 = 10
        # 24 // 2 = 12
        self.conv4 = nn.Conv2d(128, 256, 5)

        I.kaiming_normal_(self.conv4.weight)

        # (W-F)/S + 1 = (10 - 5)/1 + 1 = 6, passed through max pool => 6//2 = 3
        # 10 // 2  = 5
        self.conv5 = nn.Conv2d(256, 512, 5)

        I.kaiming_normal_(self.conv5.weight)

        self.fc1 = nn.Linear(512 * 3 * 3, 136*10)
        # self.fc1 = nn.Linear(512 * 5 * 5, 136 * 10)

        # self.fc1_bn = nn.BatchNorm1d(136*10)

        self.fc2 = nn.Linear(136*10, 136*5)

        self.drop = nn.Dropout(p=0.8)

        # finally, create 136 output channels (for the key points)
        self.fc3 = nn.Linear(136*5, 136)

        # Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting

    def forward(self, x):
        # TODO: Define the feedforward behavior of this model
        # x is the input image and, as an example, here you may choose to include a pool/conv step:
        x = self.pool(F.relu(self.conv1(x)))
        x = self.drop(x)
        x = self.pool(F.relu(self.conv2(x)))
        x = self.drop(x)
        x = self.pool(F.relu(self.conv3(x)))
        x = self.drop(x)
        x = self.pool(F.relu(self.conv4(x)))
        x = self.drop(x)
        x = self.pool(F.relu(self.conv5(x)))

        x = x.view(x.size(0), -1)

        x = F.relu(self.fc1(x))
        # x = self.fc1(x)
        # x = self.fc1_bn(x)
        x = self.drop(x)
        x = F.relu(self.fc2(x))
        # x = self.fc2(x)
        x = self.drop(x)
        x = self.fc3(x)

        # a modified x, having gone through all the layers of your model, should be returned
        return x
