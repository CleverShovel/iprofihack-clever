from transformers import BertForSequenceClassification
from transformers import BertTokenizerFast

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizerFast.from_pretrained('./rubert-base-cased')

class CleverDataset(Dataset):
    def __init__(self, sentences, labels):
        self.sentences = sentences
        self.labels = labels
    
    def __len__(self):
        return len(self.sentences)
    
    def __getitem__(self, i):
        return {'text': self.sentences[i], 'targets': self.labels[i]}

def open_data(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    lines = [line.replace(';', '\t', 1) for line in lines]
    with open('data_other_sep.csv', 'w') as f:
        for line in lines:
            print(line, file=f)
    
