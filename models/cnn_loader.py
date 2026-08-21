import tensorflow as tf

MODEL_PATH = "trained_models/pneumonia_model_ga.h5"

model = None

def load_model():

    global model

    if model is None:

        model = tf.keras.models.load_model(MODEL_PATH)

    return model