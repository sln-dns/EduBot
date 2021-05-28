import ephem 
from datetime import date
import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

text = input('ввести /planet и планету    ')

try:
    date_year = int(input('введите дату, интересующую вас. Введите год в формате ХХХХ  '))
    date_month = int(input('введите номер месяца '))
    date_date = int(input('введите число '))
    date_interes = datetime.date(date_year, date_month, date_date)
    
except ValueError:
    print('введена неверная дата, результат на сегодняшнюю дату')
    date_interes = date.today()
    
 
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
        'Scorpius': 'Скорпион',
        'Sagittarius': 'Стрелец',
        'Capricornus': 'Козерог',
        'Aquarius': 'Водолей',
        'Pisces': 'Рыбы',
        'Bootes': 'Волопас',
        'Ophiuchus': 'Змееносец'
        }

dict_planet = {
    'Mercury': 'Меркурий',
    'Venus': 'Венера',
    'Mars': 'Марс',
    'Jupiter': 'Юпитер',
    'Saturn': 'Сатурн',
    'Uranus': 'Уран',
    'Neptune': 'Нептун',
    'Pluto': 'Плутон, хоть он больше и не планета',
    'Sun': 'Солнце',
    'Moon': 'Луна' 
    }
try:
    name_planet = text[1]
    name_planet = name_planet.title()
    planet = getattr(ephem, name_planet)(date_interes)
    constellation = ephem.constellation(planet)
    name_planet = dict_planet[name_planet]
    constellation = dict_zodiack[constellation[1]]
    date_interes = date_interes.strftime("%d %B %Y")
    print(f'На дату {date_interes} небесное тело {name_planet}  находилось в созвездии {constellation}')
    #print(constellation[1])

except (TypeError, AttributeError): 
    print('не припомню такой планеты. Попробуй ещё раз')

except IndexError:
    print('сначала набери /planet')

