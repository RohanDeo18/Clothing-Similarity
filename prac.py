import requests

url = 'http://localhost:8080/similarity_search'
data = {'text': 'tshirt', 'top_n': 10}  # Adjust the input text and top_n value as needed

response = requests.post(url, json=data)
print(response.json())  # Print the response JSON