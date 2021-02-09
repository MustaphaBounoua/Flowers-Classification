# Flowers-Classification
Using Transfer Learning for Classification


# Inceptionv3

Inceptionv3 is a convolutional neural network for assisting in image analysis and object detection, and got its start as a module for Googlenet. It is the third edition of Google's Inception Convolutional Neural Network, originally introduced during the ImageNet Recognition Challenge. 

Just as ImageNet can be thought of as a database of classified visual objects, Inception helps classification of objects in the world of computer vision. One such use is in life sciences, where it aids in the research of Leukemia. The original name (Inception) was codenamed this way after a popular "'we need to go deeper' internet meme" went viral quoting a phrase from Inception film of Christopher Nolan.

<img src="https://i.kym-cdn.com/photos/images/newsfeed/000/531/557/a88.jpg">



# Fine-tuning InceptionV3 for flowers classification

We will use InceptionV3 Model for flowers classification task.

InceptionV3 architecture (https://research.googleblog.com/2016/03/train-your-own-image-classifier-with.html):
<img src="https://github.com/hse-aml/intro-to-dl/blob/master/week3/images/inceptionv3.png?raw=1" style="width:70%">

We will add a dense layer to the InceptionV3 model and retrain the last 50 layers to fine tune the model to the Flower data set

# Flower DataSet 

Flowers classification dataset (http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html) consists of 102 flower categories commonly occurring in the United Kingdom. Each class contains between 40 and 258 images:
# Model

Fine tune for 2 epochs (full passes through all training data)
We make 2*8 epochs, where epoch is 1/8 of our training data to see progress more often

loss='categorical_crossentropy',  # we train 102-way classification
optimizer=tf.keras.optimizers.Adamax(lr=1e-2),  # we can take big lr here because we fixed first layers
metrics=['accuracy']  

# Results 


