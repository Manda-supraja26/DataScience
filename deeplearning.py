#!/usr/bin/env python
# coding: utf-8

# # deep learning

# In[12]:


get_ipython().system('pip install tensorflow')


# In[13]:


import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt


# In[14]:


from keras.datasets import mnist
objects = mnist
(train_img,train_lab),(test_img,test_lab) = objects.load_data()


# In[15]:


for i in range(20):
    plt.subplot(4,5,i+1)
    plt.imshow(train_img[i],cmap='gray_r')
    plt.title("Digit:{}".format(train_lab[i]))
    plt.subplots_adjust(hspace=0.5)
    plt.axis('off')


# In[17]:


from keras.models import Sequential
from keras.layers import Flatten,Dense
model = Sequential()
input_layer=Flatten(input_shape=(28,28))
model.add(input_layer)
hidden_layer1=Dense(512,activation='relu')
model.add(hidden_layer1)
hidden_layer2=Dense(512,activation='relu')
model.add(hidden_layer2)
output_layer=Dense(10,activation='softmax')
model.add(output_layer)


# In[18]:


model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])


# In[22]:


model.fit(train_img,train_lab,epochs=5)


# In[ ]:




