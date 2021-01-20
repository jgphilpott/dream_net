import os
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub

os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "COMPRESSED"

hub_model_one = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1")
hub_model_two = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")

content_image = ""
style_image = ""

print("\nPlease provide the path to the desired content image (including the extension).\n")

while not os.path.isfile(content_image):

    content_image = input()

    if not os.path.isfile(content_image):

        print("\nThe path you provided does not exist, please try again.\n")

print("\nPlease provide the path to the desired style image (including the extension).\n")

while not os.path.isfile(style_image):

    style_image = input()

    if not os.path.isfile(style_image):

        print("\nThe path you provided does not exist, please try again.\n")

max_size = None

print("\nPlease provide the desired size of the output image (about 500px is recommended).\n")

while not type(max_size) == int:

    try:

        max_size = int(input())

    except:

        print("\nThe input you provided is not an integer, please try again.\n")

def load_image(path_to_image):

  def resize_image(image):

    shape = tf.cast(tf.shape(image)[:-1], tf.float32)
    scale = max_size / max(shape)
    new_shape = tf.cast(shape * scale, tf.int32)

    return tf.image.resize(image, new_shape)[tf.newaxis, :]

  image = tf.io.read_file(path_to_image)
  image = tf.image.decode_image(image, channels=3)
  image = tf.image.convert_image_dtype(image, tf.float32)

  return resize_image(image)

stylized_image_one = hub_model_one(tf.constant(load_image(content_image)), tf.constant(load_image(style_image)))[0]
stylized_image_two = hub_model_two(tf.constant(load_image(content_image)), tf.constant(load_image(style_image)))[0]

Image.fromarray(np.array(stylized_image_one * 255, dtype=np.uint8)[0]).save("stylized_image_one.jpg")
Image.fromarray(np.array(stylized_image_two * 255, dtype=np.uint8)[0]).save("stylized_image_two.jpg")

print("\nDone!\n")
