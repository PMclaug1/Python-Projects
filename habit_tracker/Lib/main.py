import requests
from datetime import datetime

USERNAME = "pmclaug1-github"
TOKEN = "secret-password"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# pixela set up - completed
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# pixela set up graph - completed
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#    "id": "graph1",
#    "name": "Practice Hours Graph",
#    "unit": "Hours",
#    "type": "float",
#    "color": "ajisai"
# }

# headers = {
#    "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# create pixela post

# can put any date below, will format in the graph_params
today = datetime.now()
print(today.strftime("%Y%m%d"))

graph_entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0.5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_entry_endpoint, json=graph_params, headers=headers)
print(response.text)

# update a pixel - put


put_params = {
    "quantity": "0.5"
}

# change put_entry_endpoint to reflect date to modify
# put_entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# put_response = requests.put(url=put_entry_endpoint, json=put_params, headers=headers)
# print(put_response.text)

# delete a pixel

# change delete_endpoint to reflect date to modify

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# delete_response = requests.delete(url=delete_entry_endpoint, headers=headers)
# print(put_response.text)