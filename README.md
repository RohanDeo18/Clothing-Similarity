# Clothing Similarity Project

This project aims to provide a clothing similarity search functionality using natural language processing techniques. Given a user's input text describing a desired clothing item, the system retrieves and ranks similar clothing items from a pre-defined dataset.


## Overview

The clothing similarity project leverages the power of word embeddings and cosine similarity to find similarities between clothing items based on their descriptions. The Word2Vec model is used to encode text into numerical feature vectors, and cosine similarity is used to calculate the similarity scores. The dataset used in this project is created by scraping a diverse set of clothing data from Myntra.com and Ajio.com.


## Dataset Information

The dataset used in this project is created by scraping clothing data from Myntra.com and Ajio.com. It contains a collection of clothing items along with their descriptions, brands and URLs. The file preprocess.py is used to clean and process the dataset - it also stores the cleaned data in a json format (cleaned_data.json). This cleaned json dataset is then used in the similarity search algorithm.

## Model and Algorithm

For finding similar clothing items, we used the Word2Vec model and cosine similarity algorithm. Here's a brief overview of the approach:

1. Word2Vec Model:
We trained a Word2Vec model using a dataset of clothing descriptions. The Word2Vec model represents words as dense vectors in a high-dimensional space, capturing semantic relationships between words. By training the model on a large corpus of clothing data, it learns to embed similar clothing-related words close to each other in the vector space.


2. Extracting Features:
To find similar items, we extract features from the input text using the trained Word2Vec model. The input text is preprocessed by tokenizing, lowercasing, and splitting it into words. Each word is then mapped to its corresponding vector representation obtained from the Word2Vec model. We compute the average vector representation of all the words in the input text as the feature vector.


3. Cosine Similarity:
We compute the cosine similarity between the input text's feature vector and the feature vectors of all the items in the database. The cosine similarity measures the similarity in direction between two vectors and ranges from -1 to 1, where 1 indicates identical vectors and -1 indicates completely opposite vectors. By calculating the cosine similarity between the input text and each item's feature vector, we can determine their similarity.


4. Ranking and Retrieval:
Based on the computed similarities, we rank the items in the database in descending order. The top-ranked items are considered the most similar to the input text. We return a ranked list of URLs for the similar clothing items.



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
