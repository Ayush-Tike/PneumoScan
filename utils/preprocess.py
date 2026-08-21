import numpy as np
from PIL import Image

def preprocess_image(uploaded_file):

    img = Image.open(uploaded_file)

    # convert grayscale → RGB
    img = img.convert("RGB")

    img = img.resize((128,128))

    img = np.array(img) / 255.0

    # add batch dimension
    img = np.expand_dims(img, axis=0)

    return img