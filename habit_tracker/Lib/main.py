import requests

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

graph_entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_params = {
    "date": "20231103",
    "quantity": "0.5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_entry_endpoint, json=graph_params, headers=headers)
print(response.text)

#
