# Clothing Similarity Project

This project aims to provide a clothing similarity search functionality using natural language processing techniques. Given a user's input text describing a desired clothing item, the system retrieves and ranks similar clothing items from a pre-defined dataset.
Overview

The clothing similarity project leverages the power of word embeddings and cosine similarity to find similarities between clothing items based on their descriptions. The Word2Vec model is used to encode text into numerical feature vectors, and cosine similarity is used to calculate the similarity scores. The dataset used in this project is created by scraping clothing data from Myntra.com and Ajio.com.
Instructions for Deployment

## Dataset Information

The dataset used in this project is created by scraping clothing data from Myntra.com and Ajio.com. It contains a collection of clothing items along with their descriptions and URLs. The dataset is pre-processed and cleaned for use in the similarity search algorithm.

To deploy the clothing similarity application, follow these steps:

## Prerequisites

1. Python 3.7 or later
2. Docker
3. Google Cloud SDK (optional, for deploying on Google Cloud Run)

## Installation

1. Clone the project repository from GitHub:

        git clone <repository_url>


2. Navigate to the project directory:

        cd Clothing-Similarity-Project


3. Install the required Python packages using pip:

        pip install -r requirements.txt


## Running Locally

4. Start the Flask development server:

        python app.py

Access the application by visiting http://localhost:5000 in your web browser.


## Containerization with Docker

6. Build the Docker image:

        docker build -t clothing-similarity .


7. Run the Docker container:

        docker run -p 5000:5000 clothing-similarity

    
8. Access the application by visiting http://localhost:5000 in your web browser.


## Deploying on Google Cloud Run

9. Make sure you have the Google Cloud SDK installed and authenticated with your Google Cloud account.


10. Build the Docker image and tag it with the Google Container Registry URL:

        docker build -t gcr.io/<project_id>/clothing-similarity .


11. Push the Docker image to the Google Container Registry:

        docker push gcr.io/<project_id>/clothing-similarity


12. Deploy the application on Google Cloud Run:

        gcloud run deploy clothing-similarity \
        --image gcr.io/<project_id>/clothing-similarity \
        --platform managed \
        --region <region> \
        --allow-unauthenticated

    Replace <project_id> with your Google Cloud project ID and <region> with the desired region for deployment.

    
13. Access the deployed application using the provided URL.


## Conclusion

The clothing similarity project provides an efficient and accurate way to find similar clothing items based on the user input. By leveraging natural language processing techniques (Word2Vec for this project), it enables users to discover relevant clothing options quickly. Follow the deployment instructions to set up the application and start exploring the world of clothing similarity.
