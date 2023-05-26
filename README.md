# Clothing Similarity Project

This project aims to provide a clothing similarity search functionality using natural language processing techniques. Given a user's input text describing a desired clothing item, the system retrieves and ranks similar clothing items from a pre-defined dataset.
Overview

The clothing similarity project leverages the power of word embeddings and cosine similarity to find similarities between clothing items based on their descriptions. The Word2Vec model is used to encode text into numerical feature vectors, and cosine similarity is used to calculate the similarity scores. The dataset used in this project is created by scraping clothing data from Myntra.com and Ajio.com.
Instructions for Deployment

To deploy the clothing similarity application, follow these steps:

Prerequisites

1. Python 3.7 or later
2. Docker
3. Google Cloud SDK (optional, for deploying on Google Cloud Run)

Installation

    Clone the project repository from GitHub:

    bash

git clone <repository_url>

Navigate to the project directory:

bash

cd Clothing-Similarity-Project

Install the required Python packages using pip:

bash

    pip install -r requirements.txt

Running Locally

    Start the Flask development server:

    bash

    python app.py

    Access the application by visiting http://localhost:5000 in your web browser.

Containerization with Docker

    Build the Docker image:

    bash

docker build -t clothing-similarity .

Run the Docker container:

bash

    docker run -p 5000:5000 clothing-similarity

    Access the application by visiting http://localhost:5000 in your web browser.

Deploying on Google Cloud Run (Optional)

    Make sure you have the Google Cloud SDK installed and authenticated with your Google Cloud account.

    Build the Docker image and tag it with the Google Container Registry URL:

    bash

docker build -t gcr.io/<project_id>/clothing-similarity .

Push the Docker image to the Google Container Registry:

bash

docker push gcr.io/<project_id>/clothing-similarity

Deploy the application on Google Cloud Run:

bash

    gcloud run deploy clothing-similarity \
      --image gcr.io/<project_id>/clothing-similarity \
      --platform managed \
      --region <region> \
      --allow-unauthenticated

    Replace <project_id> with your Google Cloud project ID and <region> with the desired region for deployment.

    Access the deployed application using the provided URL.

Dataset Information

The dataset used in this project is created by scraping clothing data from Myntra.com and Ajio.com. It contains a collection of clothing items along with their descriptions and URLs. The dataset is pre-processed and cleaned for use in the similarity search algorithm.
Conclusion

The clothing similarity project provides an efficient and accurate way to find similar clothing items based on user input. By leveraging natural language processing techniques, it enables users to discover relevant clothing options quickly. Follow the deployment instructions to set up the application and start exploring the world of clothing similarity.
