from __future__ import print_function
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.opti     mizers import SGD
from keras.utils import np_utils
np.random.seed(1671) # for reproducibility

from pandas import read_csv
import pandas as pd




#training
train = read_csv("/home/sergio/Documents/KAGGLE/CervicalCancerScreening/output/features/Andrei/old/ccs.new_trainOK2.csv")
array_train = train.values
X= array_train[:,3:189]
y = array_train[:,0]

