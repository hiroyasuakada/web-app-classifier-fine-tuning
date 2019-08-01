

Name
====

djangoai

## Description

Web application for Image Recognition of car and moterbike using Keras, Django

keyword: Python, Django, TensorFlow, cnn, transfer learning, fine-tuning

## Demo

1. Uploading images including a car or a bike
![car1](https://github.com/akadahiroyasu/djangoai/blob/master/images_for_readme/window_1.png)

2. Predicting what's inside of the pictures you uploaded
![car2](https://github.com/akadahiroyasu/djangoai/blob/master/images_for_readme/window_2.png)


## Dependency

## Usage

#1. Collecting data by cloning (FlickerAPI + urlretrieve)#

download.py

#2. Converting the collected data values to numpy file#

generate_data.py: normalizing numbers

generate_data_224.py: imagesize is 224×224 for next phase

#3. Processing learning phase on cnn, transfer learning#

cnn.py: learning train data on cnn

vgg16_transfer.py: learning train data (image size is 224×224) on vgg16

#4. Saving the result of learning as h5 file#

predict.py: showing the result of learning on commandprompt


#5. Implementing web application using django 2.2#

aiapps/carbike: officail website for django in more detail

#6. Uploading images and predicting it with AI model created in phase 1~4#

just following the instruction on the website

#7. Optimizing layout by using Bootstrap 4#




## References

<https://www.udemy.com/django-ai-app/>

<https://docs.djangoproject.com/en/2.2/intro/tutorial01/>
