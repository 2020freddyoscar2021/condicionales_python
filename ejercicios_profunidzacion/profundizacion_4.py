# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

from array import array


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio


palabra_1 = str(input('Ingreso primer palabra: '))
palabra_2 = str(input('Ingrese segundo palabra: '))
palabra_3 = str(input('Ingrese tercer palabra: '))

my_list_alfabetico = [palabra_1, palabra_2, palabra_3]
my_list_cantida_letras = [len(palabra_1), len(palabra_2), len(palabra_3)]

orden = int(input('Ingrese valor 1 si quiere ordenar de forma alfabetica, y 2 si quiere orden cantidad letras: ')) # si es 1 es ordenar alfabetico y lo contrario es cantidad letras


if orden == 1 :
    my_list_alfabetico.sort()
    print(my_list_alfabetico)
else:
    my_list_cantida_letras.sort(reverse = True)
    print(my_list_cantida_letras)

print('Termino proceso ')
