import torch.nn.functional as F
import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision.models as models
from torchvision import transforms,utils
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import numpy as np
import torch.optim as optim
import os

learning_rate = 0.0001

root = os.getcwd() + '/'

def default_loader(path):
    return Image.open(path).convert('RGB')

class myDataset(Dataset):
    def __init__(self, txt, transform=None, target_transform=None, loader=default_loader):
        # super(myDataset, self).__init__()
        fh = open(txt,'r')
        imgs = []
        for line in fh:
            line = line.strip('\n')
            line = line.rstrip('\n')
            words = line.split()
            imgs.append((words[0], int(words[1])))

        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader

    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = Image.open(fn).convert('RGB')
        if self.transform is not None:
            img = self.transform(img)
        return img, label

    def __len__(self):
        return len(self.imgs)

# train_transforms = transforms.Compose([
#     transforms.RandomResizedCrop((32, 32)),
#     transforms.ToTensor(),
# ])
# text_transforms = transforms.Compose([
#     transforms.RandomResizedCrop((32, 32)),
#     transforms.ToTensor(),
# ])
#
# train_data = myDataset(txt=root + 'train.txt', transform=transforms.ToTensor())
# test_data = myDataset(txt=root + 'test.txt', transform=transforms.ToTensor())
#
# train_loader = DataLoader(dataset=train_data, batch_size=6, shuffle=True, num_workers=4)
# test_loader = DataLoader(dataset=test_data, batch_size=6, shuffle=False, num_workers=4)
#
# print('num of trainData:', len(train_data))
# print('num of testData:', len(test_data))