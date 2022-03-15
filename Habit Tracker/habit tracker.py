import requests
import datetime as dt

USERNAME = "ashish28"
TOKEN = "Ashish_28"
GRAPH_ID = "graph2"     ## https://pixe.la/v1/users/ashish28/graphs/graph2.html... to check and update daily
HEADER = {"X-USER-TOKEN": TOKEN}
TODAY = dt.datetime.now()

## -------------------------------STEP 1---------------------------
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,       # if this username is already taken previously, it cannot be used again... just like some sites
    "username": USERNAME,       # sort of password
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## all data passed in user_parameters is in json... although unintentionally.... string key, string value
# response = requests.post(url= pixela_endpoint, json= user_parameters)
# print(response.text)    # not using json as we do not want to work with it



## -------------------------------------------STEP 2 -------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    ## these parameters are visible in url bar...
    ## so passing the token (or even API keys) in parameters is not so safe... so they are passed separately a headers

    "id": GRAPH_ID,
    "name": "Daily udemy videos seen",
    "unit": "nos",
    "type": "int",
    "color": "shibafu",
}
## passing the token separately and securely.... although in API lesson , we passed in API key in parameters itself,
## there were other options available... like header


response= requests.post(url= graph_endpoint, json= graph_parameters, headers= HEADER)
print(response.text)



## --------------------------------STEP 4----------------------------------
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
graph_post_parameters = {
    "date": TODAY.strftime("%Y%m%d"),
    ## https://www.w3schools.com/python/python_datetime.asp... formats the date as redq and returns as a string
    ## instead of taking today's date, we can specify the days inside strfttime (year, month, day) in this order or keyword argumment
    "quantity": input("how many videos seen?")
}
response = requests.post(url= pixel_creation_endpoint, json= graph_post_parameters, headers= HEADER)
print(response.text)



## ----------------Examples of put and delete requests----------------------------
## update and delete both have same endpoints
##---------------- UPDATE -----------------------------------
update_endpoint = f"{pixel_creation_endpoint}/{TODAY.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": input("how many videos seen (corrected)?")
}

# response = requests.put(url= update_endpoint, json= new_pixel_data, headers= HEADER)
# print(response.text)

##---------------- DELETE -----------------------------------

# response = requests.delete(url= update_endpoint, headers= HEADER)
# print(response.text)