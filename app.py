# Import all necessary libraries
import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Load the Word2Vec model
model = Word2Vec.load('word2vec_model.bin')

def extract_features(texts):
    """
    Extracts features from text using Word2Vec model.

    Args:
        texts (list): List of input texts.

    Returns:
        list: List of text features.
    """
    features = []
    for text in texts:
        words = text.lower().split()
        text_vector = np.zeros(model.vector_size)
        count = 0
        for word in words:
            if word in model.wv:
                text_vector += model.wv[word]
                count += 1
        if count > 0:
            text_vector /= count
        features.append(text_vector)
    return features

def compute_similarity(input_text, database, top_n=5):
    """
    Computes similarity between input text and items in the database.

    Args:
        input_text (str): Input text for similarity comparison.
        database (list): List of items in the database.
        top_n (int): Number of top similar items to retrieve.

    Returns:
        list: List of ranked similar item URLs.
    """
    input_feature = extract_features([input_text])
    database_texts = [item['Description'] for item in database]
    database_features = extract_features(database_texts)
    similarities = np.squeeze(cosine_similarity(input_feature, database_features))
    top_indices = np.argsort(similarities)[::-1][:top_n]
    ranked_results = [database[index]['URL'] for index in top_indices]
    return ranked_results

@app.route('/', methods=['GET', 'POST'])
def similarity_search():
    """
    Endpoint for the similarity search API.

    Accepts POST requests with input text and top_n parameters,
    and returns a JSON response with ranked similar item URLs.
    If accessed with a GET request, renders the index.html template.
    """
    if request.method == 'POST':
        input_text = request.json['input_text']
        top_n = int(request.json['top_n'])
        with open('cleaned_data.json', 'r') as f:
            database = json.load(f)
        ranked_results = compute_similarity(input_text, database, top_n)
        response = {
            'similar_items': ranked_results
        }
        return jsonify(response)
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
