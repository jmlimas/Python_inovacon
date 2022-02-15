new_planet=''
planets=[]

while new_planet != 'donde':
    if new_planet:
        planets.append(new_planet)  
        #for item in planets:
        # print(item)
    new_planet=input('Escriba el Nombre de un nuevo planeta o donde para salir:')
for item in planets:
     print(item)