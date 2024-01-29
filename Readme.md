# Sentiment Analysis API

## Overview
This project is a sentiment analysis service that processes textual comments and predicts whether the sentiment of the input text is positive or negative. It uses a simple yet effective machine learning model, Logistic Regression, to classify the sentiment.

The application performs several preprocessing steps on a dataset of positive and negative sentences, such as converting text to lowercase, removing stop words, and applying lemmatization to reduce words to their base or root form. These steps help in refining the data for better model performance.

Once the model is trained, the service exposes an endpoint `/predict` that accepts JSON input containing a sentence and returns the sentiment classification along with the associated probability.

## Model
The core of the service is a Logistic Regression model, which is a statistical method for analyzing a dataset in which there are one or more independent variables that determine an outcome. In this case, the outcome is binary (positive or negative sentiment). Logistic Regression is chosen for its efficiency and effectiveness for binary classification problems.

# Quick Guide to Cloning a GitHub Repository

Follow these three simple steps to clone a GitHub repository to your local machine.

## Step 1: Copy the Repository URL
Navigate to the repository on GitHub and click the green "Code" button. Copy the HTTPS URL provided.

## Step 2: Open Your Terminal
Open a terminal window on your machine and navigate to the directory where you want to clone the repository.

## Step 3: Clone the Repository
Enter the following command, replacing `URL` with the copied repository URL:

```bash
git clone https://github.com/parhaaaam/Comment_analyzer
```

After these steps, you will have a local copy of the GitHub repository.


## API Usage

### /predict
Perform a sentiment analysis of a given comment.

**Request:**
`POST /predict`

**Body:**
```json
{
  "comment": "Your input sentence here."
}
```

**Response**
```json
{
  "probability": 0.6837033395513167,
  "sentiment": "string"
}
```


# Docker Usage for Sentiment Analysis Service

## Introduction to Docker
Docker is a powerful platform that enables you to develop, deploy, and run applications inside lightweight, portable containers. Containers allow you to package your application with all of its dependencies into a single image, which can be run on any system that has Docker installed, ensuring consistency across different environments.

## Prerequisites
Before proceeding, ensure that Docker is installed on your system. If you haven't installed Docker, please follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

## Dockerizing the Sentiment Analysis Service
Our sentiment analysis service is containerized using Docker. This means you can easily build and run the service without worrying about setting up the Python environment or installing dependencies manually.

### Building the Docker Image
To build the Docker image for the sentiment analysis service, navigate to the directory containing the `Dockerfile` and run the following command:

```sh
docker build -t comment_analyzer .
```
This command tells Docker to build an image and tag it (-t) with the name comment_analyzer. The . at the end specifies that Docker should look for the Dockerfile in the current directory.

### Running the Docker Container

```shell
docker run -p 7000:5000 comment_analyzer
```
Here's what this command does:

&#8226; docker run: Tells Docker to run a container.

&#8226; -p 7000:5000: Maps port 7000 on your host machine to port 5000 inside the Docker container. This allows you to access the service running inside the container by visiting http://localhost:7000 on your host machine.

&#8226; comment_analyzer: The name of the image to run in the container.

## Accessing the Service

With the service running, you can now use an API client like Postman or cURL to send requests to http://localhost:7000/predict and get sentiment analysis predictions.
