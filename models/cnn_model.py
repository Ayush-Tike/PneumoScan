import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn(chromosome):

    conv1, conv2, dense_units, lr, dropout = chromosome

    model = models.Sequential([

        layers.Conv2D(conv1,(3,3),activation='relu',input_shape=(128,128,3)),
        layers.MaxPooling2D(2,2),

        layers.Conv2D(conv2,(3,3),activation='relu'),
        layers.MaxPooling2D(2,2),

        layers.Flatten(),

        layers.Dense(dense_units,activation='relu'),

        layers.Dropout(dropout),

        layers.Dense(1,activation='sigmoid')

    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=lr)

    model.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model