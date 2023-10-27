import requests

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": "secret-password",
    "username": "pmclaug1-github",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# pixela set up - completed
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

