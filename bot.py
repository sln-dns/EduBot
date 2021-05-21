import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import date
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

logging.basicConfig(filename='bot.log', level=logging.INFO)

# PROXY = {'proxy_url': 'settings.PROXY_URL',             #Если не будет работать
#    'urllib3_proxy_kwargs': {
#       'username': 'settings.PROXY_USERNAME', 
#       'password': 'settings.PROXY_PASSWORD'
#      }
# }                                                         # запустить с прокси

def greet_user(update, context):
    print('Вызван /start')
    #print(update)
    update.message.reply_text("Привет, друг! Неужто ты нажал /start")

def talk_to_me(update, context):
    text  = update.message.text
    print(text)
    update.message.reply_text(text)

def planet(update, context):
    list_planet = {'sun': 'Sun', 'moon': 'Moon', 'mercury': 'Mercury', 
       'venus': 'Venus', 'mars': 'Mars', 'phobos': 'Phobos', 'deimos': 'Deimos', 
       'jupiter': 'Jupiter', 'io': 'Io', 'europa': 'Europa', 'ganymede': 'Ganymede',
       'callisto': 'Callisto', 'saturn': 'Saturn', 'mimas': 'Mimas', 'enceladus': 'Enceladus', 
       'tethys': 'Tethys', 'dione': 'Dione', 'rhea': 'Rhea', 'titan': 'Titan', 
       'hyperion': 'Hyperion', 'iapetus': 'Iapetus', 'uranus': 'Uranus', 'ariel': 'Ariel', 
       'umbriel': 'Umbriel', 'titania': 'Titania', 'oberon': 'Oberon', 'miranda': 'Miranda', 
       'neptune': 'Neptune','pluto': 'Pluto'
    }
   
    text  = update.message.text
    text = text.lower()
    text = text.split()
    
    try:
        name_planet = text[1]
        name_planet = list_planet.get(name_planet)
        planet = getattr(ephem, name_planet)(date.today())
        constellation = ephem.constellation(planet)
        text = f'Сегодня {name_planet} в созвездии {constellation}'
        update.message.reply_text(text)
        
        
    except TypeError: 
        text = 'не припомню такой планеты. Попробуй ещё раз' 
        update.message.reply_text(text)
    except IndexError:
        text = 'сначала набери /planet'
        update.message.reply_text(text)


def main():
#    mybot = Updater('settings.API_KEY', use_context=True, request_kwargs=PROXY) #поставить это для прокси
    mybot = Updater(settings.API_KEY, use_context=True) # а эту строку просто убрать
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()