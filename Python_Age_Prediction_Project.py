import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
#naming modules
abalone_train = pd.read_csv(
  "abalone_data.csv",
  names=[
    "Length", "Diameter", "Height", "Whole weight", 
    "Shucked weight", "Viscera weight", "Shell weight", "Age"
  ]
  #csv has 8 columns
)

abalone_features = abalone_train.copy()
abalone_labels = abalone_features.pop('Age')
# print(abalone_labels)
# convert to np array
np_features = abalone_features.to_numpy()
np_rings = abalone_labels.to_numpy()
# todo
# print(np_features.shape[1])
# implement model (using tf.keras) to predict age
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=[7]))
model.add(Dense(1, activation='relu'))
# todo

# compile the model here
model.compile(optimizer= Adam(), loss = MeanSquaredError())
# todo

# fit the model here
history = model.fit(np_features, np_rings, epochs=10, verbose = 0)

# todo

print("Training History:")
print(history.history)
print("\nmodel summary")
model.summary()
