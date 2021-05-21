import ephem 
from datetime import date
import datetime
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

text = input('ввести /planet и планету    ')
date_year = int(input('введите дату, интересующую вас. Введите год в формате ХХХХ  '))
date_month = int(input('введите номер месяца '))
date_date = int(input('введите число '))

try:
    date_interes = datetime.datetime(date_year, date_month, date_date)
    #print(date_interes)
    #print(date.today())
    #mars = ephem.Mars(date_interes)
    #constellation = ephem.constellation(mars)
    #print(constellation)
except ValueError:
    print('введена неверная дата, результат на сегодняшнюю дату')
    date_interes = date.today()
    #mars = ephem.Mars(date_interes)
    #constellation = ephem.constellation(mars)
    #print(constellation)

#def planet(update, context):

   
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
    date_interes = date_interes.strftime("%d.%m.%y")
    print(f'На дату {date_interes} небесное тело {name_planet}  находилось в созвездии {constellation}')
    #print(constellation[1])

except TypeError: 
    print('не припомню такой планеты. Попробуй ещё раз')

except IndexError:
    print('сначала набери /planet')

