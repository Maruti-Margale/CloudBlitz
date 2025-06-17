import requests
import geopy.distance
from datetime import datetime
from zoneinfo import ZoneInfo


class Cab:
    def __init__(self):
        self.distance = 0
        self.amount = 0

    def get_city_locations(self, city1, city2):
        api_key = "abc7e74fada486e88d6b22f5ce803319"
        url1 = f"http://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}&units=metric"
        url2 = f"http://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units=metric"
        
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        data1 = response1.json()
        data2 = response2.json()

        coord1 = (data1["coord"]["lat"], data1["coord"]["lon"])
        coord2 = (data2["coord"]["lat"], data2["coord"]["lon"])

        self.distance = geopy.distance.distance(coord1, coord2).km

    def get_km(self):
        now = datetime.now(ZoneInfo("Asia/Kolkata")).time()
        hour = now.hour

        if 0 <= hour <= 4:
            self.amount = 25
        elif 5 <= hour <= 10:
            self.amount = 20
        elif 11 <= hour <= 20:
            self.amount = 15
        elif 21 <= hour <= 23:
            self.amount = 25
        else:
            self.amount = 20


class Bill(Cab):
    def get_total_price(self):
        return round(self.distance * self.amount, 2)


def get_city():
    city1 = input("Enter Pick up location: ")
    city2 = input("Enter Drop location: ")

    obj = Bill()
    obj.get_city_locations(city1, city2)
    obj.get_km()
    total = obj.get_total_price()
    print(f"Distance between {city1} and {city2}: {obj.distance:.2f} km")
    print(f"Rate per km: ₹{obj.amount}")
    print(f"Total Price: ₹{total}")


# Call the function to run
get_city()
