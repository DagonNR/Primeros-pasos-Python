# Declaramos una variable
juegoscompletos = input("¿Cúantos juegos has completado al 100%?: ")

# Volvemos la variable a int
juegoscompletos = int(juegoscompletos)

# Preguntamos si los juegos son menores a 5
if juegoscompletos < 5 :
    print("Son pocos") # Si es menor a 5 muestra esto
elif juegoscompletos > 100 :
    print("Eh calmate tantito carnal")
elif juegoscompletos < 0 :
    print("Mira carnal, a mi no me gusta tratar con mentirosos, saquese")
else :
    print("Eh medio le sobas") # Si lo anterior no se cumple aparece esto

# Otro ejemplo
materiasactivas = input("Introduce el número de materias que cursas actualmente: ")
materiasactivas = int(materiasactivas)

if materiasactivas >= 6 and materiasactivas <= 10 :
    print("Ten cuidado, administra bien tu tiempo")
elif materiasactivas > 10:
    print("Que diosito te bendiga")
elif materiasactivas < 0 :
    print ("Entonces no estudias, ¿Qué haces contestando esto?")
else :
    print("¿Por qué contestas esto?")