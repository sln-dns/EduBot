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
    update.message.reply_text("Привет, друг! Неужто ты нажал /start")

def talk_to_me(update, context):
    text  = update.message.text
    print(text)
    update.message.reply_text(text)

def planet(update, context):
       
    text  = update.message.text
    text = text.lower()
    text = text.split()

    dict_zodiack = {
        'Aries': 'Овен',
        'Taurus': 'Телец',
        'Gemini': 'Близнецы',
        'Cancer': 'Рак',
        'Leo': 'Лев',
        'Virgo': 'Дева',
        'Libra': 'Весы',
        'Scorpio': 'Скорпион',
        'Sagittarius': 'Стрелец',
        'Capricornus': 'Козерог',
        'Aquarius': 'Водолей',
        'Pisces': 'Рыбы'
        }
    
    dict_planet = {
        'Mercury': 'Меркурий',
        'Venus': 'Венера',
        'Mars': 'Марс',
        'Jupiter': 'Юпитер',
        'Saturn': 'Сатурн',
        'Uranus': 'Уран',
        'Neptune': 'Нептун',
        'Pluto': 'Плутон, хоть он больше и не планета,',
        'Sun': 'Солнце',
        'Moon': 'Луна' 
        }

    try:
        name_planet = text[1]
        name_planet = name_planet.title()        
        planet = getattr(ephem, name_planet)(date.today())
        constellation = ephem.constellation(planet)
        constellation = dict_zodiack[constellation[1]]
        name_planet = dict_planet[name_planet]
        text = f'Сегодня {name_planet} в созвездии {constellation}'
        update.message.reply_text(text)
        
        
    except (TypeError, AttributeError): 
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
    #dp.add_handler(MessageHandler(Filters.text, planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()