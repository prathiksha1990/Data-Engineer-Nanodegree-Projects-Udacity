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

## Project Implementation

## Implementation
<details>
<summary>
Landing Zone
</summary>

> In the Landing Zone I stored the customer, accelerometer and step trainer raw data in AWS S3 bucket. 

Using The AWS glue data catalog, I created a glue tables so that I can query the data using AWS athena.

1- Customer Landing Table:

<img width="895" alt="customer_landing" src="https://github.com/prathiksha1990/Data-Engineer-Nanodegree-Projects-Udacity/assets/16706973/bf46a0db-dc5b-448a-9e22-076b3a891020">


2- Accelerometer Landing Table: 

<img width="735" alt="accelerometer_landing" src="https://github.com/prathiksha1990/Data-Engineer-Nanodegree-Projects-Udacity/assets/16706973/91537795-e978-4180-a5e7-ec1228ba4f33">


3- Step Trainer Landing Table: 

<img width="669" alt="step_trainer_landing" src="https://github.com/prathiksha1990/Data-Engineer-Nanodegree-Projects-Udacity/assets/16706973/00739b28-c524-43b5-807e-88e140b0ce61">


</details>

<details>
<summary>
Trusted Zone
</summary>

> In the Trusted Zone, I created AWS Glue jobs to make transofrmations on the raw data in the landing zones.

**Glue job scripts**

[1. Customer_Landing_to_Trusted.py](customer_landing_to_trusted.py) - This script transfers customer data from the 'landing' to 'trusted' zones. It filters for customers who have agreed to share data with researchers.

[2. Accelerometer_Landing_to_Trusted.py](accelerometer_landing_to_trusted.py) - This script transfers accelerometer data from the 'landing' to 'trusted' zones. Using a join on customer_trusted and accelerometer_landing, It filters for Accelerometer readings from customers who have agreed to share data with researchers.

[3. Step_Trainer_Landing_to_Trusted.py](Trainer_landing_to_trusted.py) - This script transfers Step Trainer data from the 'landing' to 'trusted' zones. Using a join on customer_curated and step_trainer_landing, It filters for customers who have accelerometer data and have agreed to share their data for research with Step Trainer readings.

The customer_trusted table was queried in Athena to show that it only contains customer records from people who agreed to share their data.


</details>

<details>
<summary>
Curated Zone
</summary>

> In the Curated Zone I created AWS Glue jobs to make further transformations, to meet the specific needs of a particular analysis.

**Glue job scripts**

[customer_trusted_to_customer_curated.py](customer_trusted_to_customer_curated.py) - This script transfers customer data from the 'trusted' to 'curated' zones. Using a join on customer_trusted and accelerometer_landing, It filters for customers with Accelerometer readings and have agreed to share data with researchers.

[machine_learning_curated.py](machine_learning_curated.py): This script is used to build aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data.

</details>
