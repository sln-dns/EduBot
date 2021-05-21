import ephem 
from datetime import date
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

text = input('ввести /planet и планету    ')

#def planet(update, context):
list_planet = {'sun': 'Sun', 'moon': 'Moon', 'mercury': 'Mercury', 
       'venus': 'Venus', 'mars': 'Mars', 'phobos': 'Phobos', 'deimos': 'Deimos', 
       'jupiter': 'Jupiter', 'io': 'Io', 'europa': 'Europa', 'ganymede': 'Ganymede',
       'callisto': 'Callisto', 'saturn': 'Saturn', 'mimas': 'Mimas', 'enceladus': 'Enceladus', 
       'tethys': 'Tethys', 'dione': 'Dione', 'rhea': 'Rhea', 'titan': 'Titan', 
       'hyperion': 'Hyperion', 'iapetus': 'Iapetus', 'uranus': 'Uranus', 'ariel': 'Ariel', 
       'umbriel': 'Umbriel', 'titania': 'Titania', 'oberon': 'Oberon', 'miranda': 'Miranda', 
       'neptune': 'Neptune','pluto': 'Pluto'
    }
   
text = text.lower()
text = text.split()

try:
    name_planet = text[1]
    name_planet = list_planet.get(name_planet)
    planet = getattr(ephem, name_planet)(date.today())
    constellation = ephem.constellation(planet)
    print(f'Сегодня {name_planet} в созвездии {constellation}')
    print(constellation[1])

except TypeError: 
    print('не припомню такой планеты. Попробуй ещё раз')

except IndexError:
    print('сначала набери /planet')

