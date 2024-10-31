print()
print("Edgar Gael Garcia Camacho 1182: Examen")
print()

#Se agrega un diccionario vacío.

Diccionario ={}

print(" ")

#se agrega el nombre del usuario.

lo=str(input("Ingresa tu nombre :"))

print(" ")

Diccionario["Nombre"] = lo

print(Diccionario)

#se agrega la edad del usuario.

print(" ")

Edad =int(input("Ingresa tu edad :"))

print(" ")

Diccionario["Edad"] = Edad

print(Diccionario)

#Se agrega el genero del usuario.

print(" ")

Sexo =str(input("Ingresa tu sexo :"))

print(" ")

Diccionario["Sexo"] = Sexo

print(Diccionario)

#se agrega el numero telefnico.

print(" ")

Telefono = int(input("Ingresa tu numero telefonico :"))

print(" ")

Diccionario["Telefono"] = Telefono

print(Diccionario)

for x,y in Diccionario.items():

    print(x,y)