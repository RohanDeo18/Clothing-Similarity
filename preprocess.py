import numpy as np
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
import json
from torch import cosine_similarity

def clean_text(text):
    # Remove numerical values
    text = ''.join([i for i in text if not i.isdigit()])

    # Remove special characters
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    return text

def apply_lemmatization(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(lemmatized_tokens)

def clean_and_normalize_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Clean and normalize the 'Name' column
    df['Description'] = df['Description'].apply(clean_text)
    df['Description'] = df['Description'].apply(apply_lemmatization)

    df['Brand'] = df['Brand'].apply(clean_text)
    df['Brand'] = df['Brand'].apply(apply_lemmatization)

    # Convert DataFrame to JSON
    data = df.to_dict(orient='records')

    # Save cleaned data to JSON file
    with open(output_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Cleaned and normalized data saved successfully to {output_file}")

# Provide the paths of input CSV file and desired output JSON file
input_csv_file = 'Clothing Data.csv'
output_json_file = 'cleaned_data.json'

# Clean and normalize data, and save it to JSON
clean_and_normalize_data(input_csv_file, output_json_file)