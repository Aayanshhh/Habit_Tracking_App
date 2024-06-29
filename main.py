from datetime import datetime
import requests

# Pixela API credentials
USERNAME = "aayansh"
TOKEN = "qwertyuiop"
GRAPH_ID = "graph"

# Pixela API endpoints
pixela_endpoint = "https://pixe.la/v1/users"

# User creation parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user
response = requests.post(url=pixela_endpoint, json=user_params)
print("User creation response:", response.text)

# Graph creation endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration parameters
graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# Headers with user token
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("Graph creation response:", response.text)

# Endpoint to post data to the graph
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date in the required format
today = datetime.now().strftime("%Y%m%d")

# Data to be added to the graph
pixel_data = {
    "date": today,
    "quantity": "3",
}

# Post data to the graph
response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
print("Data posting response:", response.text)

# Endpoint to update data in the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# New data to update the existing entry
new_pixel_data = {
    "quantity": "5"
}

# Update data in the graph
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print("Data update response:", response.text)

# Endpoint to delete data from the graph
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# Delete data from the graph
response = requests.delete(url=delete_endpoint, headers=headers)
print("Data deletion response:", response.text)
