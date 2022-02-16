planeta={
    'name':'Mars',
    'moons':2
    }
print(f'{planeta["name"]} tiene {planeta["moons"]} Lunas')

planeta['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}


print(f'{planeta["name"]} Tiene una circunferencia polar de:{planeta["circumference (km)"]["polar"]}')

print('Ejercio 2\n')
print('\n') 

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

print(planet_moons)

lunas = 0
for item in planet_moons.values():
    lunas  += item 

#print('Numero de lunas:', sum(planet_moons.values()))

print('Numero de lunas:'+str(lunas))
planetas = len(planet_moons.keys())
print('Numero de Planetas:'+str(planetas))

promedio = lunas / planetas

print('Promedio:'+str(promedio)) 