import os
import requests
from requests.auth import HTTPBasicAuth

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3378154640654e2a63c00915beaf3331/day39FlightDeals/prices"


class DataManager:

    def __init__(self):
        return
        # self._user = os.environ["Flight"]
        # self._password = os.environ["sheakchilly"]
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        # self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)