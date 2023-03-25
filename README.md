#Useful Forecast Bot

Useful Forecast Bot is a Telegram bot that provides weather information in a clear and understandable way. Instead of just providing raw data, it interprets it to give users a useful insight into what to expect and how to prepare.

Features
Provides current weather conditions, including temperature, humidity, wind speed, and cloud cover.
Provides a 7-day weather forecast, including daily highs and lows, as well as an overall summary of the expected weather conditions.
Provides personalized recommendations based on the weather forecast, such as what type of clothing to wear or whether to bring an umbrella.
Provides information on air quality and UV index.
Provides alerts for severe weather conditions.
Technologies Used
Aiogram - a Python library for developing Telegram bots.
PostgreSQL - an open-source relational database management system.
OpenWeatherAPI - an API for accessing weather data.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/username/UsefulForecastBot.git
Install the necessary dependencies:
Copy code
pip install -r requirements.txt
Set up a PostgreSQL database and create the necessary tables (refer to database.sql).

Create a .env file in the root directory and add the following information:

makefile
Copy code
TELEGRAM_API_TOKEN=<Your Telegram API Token>
OPENWEATHER_API_KEY=<Your OpenWeather API Key>
DATABASE_URL=<Your PostgreSQL database URL>
Start the bot:
css
Copy code
python main.py
Usage
To use the bot, simply search for "Useful Forecast Bot" on Telegram and start a conversation. The bot will guide you through the available commands and provide information on how to use them.

Contributions
Contributions are welcome! Feel free to submit pull requests or open issues if you find any bugs or have suggestions for new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.