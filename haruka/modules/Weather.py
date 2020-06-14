from typing import Optional, List

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from haruka import dispatcher, LOGGER
from haruka.modules.disable import DisableAbleCommandHandler

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pyowm
import TOKEN,OW_TOKEN

@run_async
def weather(bot: Bot, update: Update, args: List[str]):
	"""Define weather at certain location"""
    owm = pyowm.OWM(OW_TOKEN)
    text_location = "".join(str(x) for x in args)
    observation = owm.weather_at_place(text_location)
    w = observation.get_weather()
    humidity = w.get_humidity()
    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    convert_temp = temp.get('temp')
    convert_wind = wind.get('speed')
    convert_humidity = humidity
    text_temp = str(convert_temp)
    text_wind = str(convert_wind)
    text_humidity = str(convert_humidity)
    update.message.reply_text("Temperature, celsius: {}".format(text_temp))
    update.message.reply_text("Wind speed, m/s: {}".format(text_wind))
    update.message.reply_text("Humidity, %: {}".format(text_humidity))


__mod_name__ = "Weather"
	
