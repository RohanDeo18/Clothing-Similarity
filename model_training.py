import csv
from gensim.models import Word2Vec

def train_word2vec_model(csv_file):
    descriptions = []
  
    # Read the CSV file and extract the descriptions
    with open('Clothing Data.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            descriptions.append(row['Description'])

    # Tokenize and preprocess the text data
    sentences = [description.lower().split() for description in descriptions]

    # Train the Word2Vec model
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    # Save the trained model
    model.save("word2vec_model.bin")

# Save the model
train_word2vec_model('D:\Rohan\Work\Mercor ML Engineer Project')
