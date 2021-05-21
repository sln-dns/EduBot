import ephem 
from datetime import date
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

text = input('ввести /planet и планету    ')

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
        'Capricom': 'Козерог',
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
    planet = getattr(ephem, name_planet)(date.today())
    constellation = ephem.constellation(planet)
    name_planet = dict_planet[name_planet]
    constellation = dict_zodiack[constellation[1]]
    print(f'Сегодня {name_planet} в созвездии {constellation}')
    #print(constellation[1])

except TypeError: 
    print('не припомню такой планеты. Попробуй ещё раз')

except IndexError:
    print('сначала набери /planet')

