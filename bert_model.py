from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf

MODEL_NAME = "bert-base-uncased"
NUM_CLASSES = 5

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

model = TFBertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=NUM_CLASSES
)

optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)

loss = tf.keras.losses.CategoricalCrossentropy(from_logits=True)

class_weights = {
    0: 1.0,
    1: 1.2,
    2: 1.3,
    3: 1.1,
    4: 1.4
}

def predict_emotion(text):

    inputs = tokenizer(
        text,
        return_tensors="tf",
        truncation=True,
        padding=True,
        max_length=128
    )

    outputs = model(inputs)

    prediction = tf.argmax(outputs.logits, axis=1)

    return prediction.numpy()[0]
