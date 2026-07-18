
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout

VOCAB_SIZE = 10000
EMBEDDING_DIM = 128
MAX_LENGTH = 100

def build_bilstm_model():

    model = Sequential()

    model.add(
        Embedding(
            input_dim=VOCAB_SIZE,
            output_dim=EMBEDDING_DIM,
            input_length=MAX_LENGTH
        )
    )

    model.add(Bidirectional(LSTM(64)))

    model.add(Dropout(0.5))

    model.add(Dense(32, activation="relu"))

    model.add(Dense(5, activation="softmax"))

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
