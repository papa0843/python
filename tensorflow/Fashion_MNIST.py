#파이썬 3.9버전이라서 안 되는 것 같음//일단 미완
#https://www.tensorflow.org/tutorials/keras/classification?hl=ko
#tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

#헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

#패션 MNIST 샘플

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images.shape)

print(len(train_labels))

print(train_labels)