import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# Load the Word2Vec model
model = Word2Vec.load('word2vec_model.bin')

# Extract features using Word2Vec
def extract_features(texts):
    features = []
    for text in texts:
        # Split the text into individual words
        words = text.lower().split()
        text_vector = np.zeros(model.vector_size)
        count = 0

        # Calculate the average vector for the words in the text
        for word in words:
            if word in model.wv:
                text_vector += model.wv[word]
                count += 1

        if count > 0:
            text_vector /= count

        features.append(text_vector)

    return features

# Compute similarity using cosine similarity and return ranked results
def compute_similarity(input_text, database, top_n=5):
    input_feature = extract_features([input_text])

    # Extract the text descriptions from the JSON database
    database_texts = [item['Description'] for item in database]

    # Convert the database texts into features
    database_features = extract_features(database_texts)

    # Calculate cosine similarity between the input feature and the database features
    similarities = np.squeeze(cosine_similarity(input_feature, database_features))

    # Get the indices of the top-N most similar items
    top_indices = np.argsort(similarities)[::-1][:top_n]

    # Create a ranked list of URLs based on the top indices
    ranked_results = [database[index]['URL'] for index in top_indices]

    return ranked_results

# Load the cleaned data from JSON
def load_cleaned_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
