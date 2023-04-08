from api_keys import OpenWeatherApiKeys
import requests
import json


class OpwApi:

    API_key = OpenWeatherApiKeys.API_KEY


    def get_5_day_forecast(self, user_cord):
        api_call = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        api_call = api_call.format(
            lat='54.6197', lon='39.74', API_key=OpwApi.API_key)
        response = requests.get(api_call)
        return response.json()

    def get_current_weather(self, user_cord):
        api_call = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        api_call = api_call.format(
            lat='54.6197', lon='39.74', API_key=OpwApi.API_key)
        response = requests.get(api_call)
        return response.json()

    def get_4_day_hourly_forecast(self, user_cord):
        api_call = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        api_call = api_call.format(
            lat='54.6197', lon='39.74', API_key=OpwApi.API_key)
        response = requests.get(api_call)
        return response.json()
