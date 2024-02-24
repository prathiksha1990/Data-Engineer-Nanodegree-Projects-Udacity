# Project: STEDI-Human Balance Analytics

## Introduction

The STEDI Team has been  developing a hardware STEDI Step Trainer that
1. trains the user to do a STEDI balance exercise 
2. has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
3. has a companion mobile app that collects customer data and interacts with the device sensors.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. 
The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion
 in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a 
primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data 
should be used in the training data for the machine learning model

## Project Description

In this project I will extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse 
solution on AWS using Python,AWS GLue, AWS Athena and AWS S3.

AWS Infrastruncture will be levarged to create 3 storage zones(Landing,trusted and curated), data catalog, data cleansing transformations 
between zones.

![image](https://github.com/prathiksha1990/Data-Engineer-Nanodegree-Projects-Udacity/assets/16706973/1f7ce902-5729-44ed-8f1a-265969ffc0e4)

 
## Project Data

This project includes the following datasets:

#### Customer Records: from fulfillment and the STEDI website.
#### Step Trainer Records: data from the motion sensor.
#### Accelerometer Records: data from the mobile app.

![image](https://github.com/prathiksha1990/Data-Engineer-Nanodegree-Projects-Udacity/assets/16706973/1a4d4689-0aa3-428c-a9a1-e13aaac0f2d8)


