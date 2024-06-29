# Habit_Tracking_App

This Python script interacts with the Pixela API to create a user, set up a graph, and manage data points. It demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on Pixela's graph data.

## Features

- **User Creation**: Create a new user on Pixela.
- **Graph Setup**: Set up a graph with specific configurations (ID, name, unit, type, color).
- **Post Data**: Add data points to the graph (e.g., hours spent programming).
- **Update Data**: Update existing data points on the graph.
- **Delete Data**: Remove data points from the graph.


 **Script output**:

    The script will perform the following actions and print the responses to the console:
    - Create a user
    - Set up a graph
    - Post data to the graph
    - Update the data
    - Delete the data

## Code Overview

The script performs the following steps:

1. **Import necessary libraries**:

    ```python
    from datetime import datetime
    import requests
    import os
    ```
    
3. **Define endpoints and user parameters**:

    ```python
    pixela_endpoint = "https://pixe.la/v1/users"
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    ```

4. **Create a new user**:

    ```python
    response = requests.post(url=pixela_endpoint, json=user_params)
    print("User creation response:", response.text)
    ```

5. **Set up a graph**:

    ```python
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Programming Graph",
        "unit": "hours",
        "type": "float",
        "color": "ajisai"
    }
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print("Graph creation response:", response.text)
    ```

6. **Post data to the graph**:

    ```python
    pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {"date": today, "quantity": "3"}
    response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
    print("Data posting response:", response.text)
    ```

7. **Update data in the graph**:

    ```python
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    new_pixel_data = {"quantity": "5"}
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print("Data update response:", response.text)
    ```

8. **Delete data from the graph**:

    ```python
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print("Data deletion response:", response.text)
    ```


## Acknowledgments

- [Pixela API](https://pixe.la/)
- [Requests Library](https://docs.python-requests.org/en/latest/)
- [dotenv Library](https://pypi.org/project/python-dotenv/)

