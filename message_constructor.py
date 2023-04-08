import openweather_api as opwapi
import emoji

class ForecastMessageConstructor:

    def getCurrentWeatherMessage():
        Opw = opwapi.OpwApi()
        data = Opw.get_current_weather(0)
        msg = ''
        msg += ("\U0001F321 Сейчас на улице: ")
        msg += str((data["main"]["temp"]))
        return msg 

    