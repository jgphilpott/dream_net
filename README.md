<p align="center">
  <img width="250" height="250" src="https://github.com/jgphilpott/dream_net/blob/main/icon.jpg">
</p>

# Dream Net

The Dream Net is a neural networking tool used to create visual art! It uses a technique known as '[neural style transfer](https://en.wikipedia.org/wiki/Neural_Style_Transfer)' to blend images together. There are also a few online tools you can use such as the [Deep Dream Generator](https://deepdreamgenerator.com) if programming isn't your thing.

This project uses two pretrained [models from TensorFlow Hub](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256) to make the image generation process as simple and speedy as possible. If you want to take a deeper dive and learn how to build your own models from scratch I recommend [this tutorial](https://www.tensorflow.org/tutorials/generative/style_transfer).

For a few examples take a look at [this short video](https://youtu.be/krihwKy9ckg).

# Usage

This repository contains two helpful files to get you started, a Jupyter Notebook and a Python file.

## Jupyter Notebook

The easiest way to get started is to simply upload [this Jupyter Notebook file](https://github.com/jgphilpott/dream_net/blob/main/dream_net.ipynb) to [Google Colab](https://colab.research.google.com/notebooks) and just read and run the cells. If you haven't used Colaboratory before check out [this intro](https://colab.research.google.com/notebooks/intro.ipynb), it's a great tool!

## Python File

The first thing you will need to do is to make sure you have all the requirements installed. Run the commands below and the modules will be installed, if they aren't already.

```
pip install numpy
pip install Pillow
pip install tensorflow
pip install tensorflow_hub
```

Once that's done you can download [this python file](https://github.com/jgphilpott/dream_net/blob/main/dream_net.py) and execute it with the command `python3 dream_net.py`. Then simply follow the prompts in the terminal window and if all goes well the program will generate two different results for you and you can pick your favorite!
