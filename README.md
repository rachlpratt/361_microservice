# Days Left Microservice

This microservice takes a due date via **HTTP GET request** and returns a message in JSON format indicating how much time remains until the due date (or how much time has passed since the due date). The current date is obtained using Python's datetime module, which is compared to the given due date in order to calculate the difference in days. The number of days is used to generate the return message.

_Note: For the purposes of this class project, we will be using localhost and running the service on the same machine as the client._

## To Request Data:

Send a GET request to the following URL:
http://localhost:8080/due/{date}

**A few things to note:**
-In place of {date}, include the due date in MM-DD-YYY format.
-Include dashes between the month, day, and year.
-The port number must be 8080.

Example URL:
http://localhost:8080/due/03-14-2023
(The due date is March 14th, 2023)

## To Receive Data:
After the request has been made, obtain the text from the HTTP reponse and parse the JSON data using the language of your choice.

**Example Python script:**
```sh
import requests
import json

def get_message(date):
    url = f'http://localhost:8080/due/{date}'
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['message']
```
Calling **get_message('02-11-2023')** will return the string **'in 3 days'** if today's date is 02-08-2023.
