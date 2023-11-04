import requests
import datetime as dt


TOKEN = "65357h23" #Your Pixela token
USERNAME = "xyz"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

today = dt.datetime.now()
#now_date = today.strftime("%Y%m%d")

y_dat = dt.datetime(year=2023,month=9, day=20)
y_date = y_dat.strftime("%Y%m%d")



pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_param = {
    "date": y_date,
    "quantity": "12.7"
}

# response = requests.post(url=pixel_endpoint, json=pixel_param, headers=headers)


update_endpoint = f"{pixel_endpoint}/20230921"

update_param ={
    "quantity": "8.4"
    }

requests.put(url=update_endpoint, json=update_param, headers=headers)

response = requests.delete(url = update_endpoint, headers=headers)
print(response.text)


