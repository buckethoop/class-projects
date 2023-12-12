You need the following dependencies:
    from datasets import load_dataset
    from torch.utils.data import DataLoader
    import torch
    from torch.utils.data import Dataset, DataLoader
    from torch import nn
    from torch.optim import Adam
    from torch.nn.utils.rnn import pad_sequence
    from datasets import load_dataset
    import itertools
    from collections import Counter
    from conlleval import evaluate
    import datasets
    import csv
    import numpy as np

*NOTE: I HAVE USED glove.6B.100d.txt
* I am assuming this will already be in the directory


TO PRODUCE PREDICTIONS FILES:

For task1 test split:
    %python3 test_task1.py

for task2 test split:
    %python3 test_task2.py


