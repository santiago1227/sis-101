# menor que
variable_1 = 10
variable_2 = 7
resultado = variable_1 < variable_2 
print=(resultado)
# mayor igual que 
variable_3 = "messi"
variable_4 = "cr7"
resultado = variable_3 >  variable_4
print( " mayor igual que")
print(resultado)

#menor igual que
variable_5 = "cr7"
variable_6 = " MESSI"
RESULTADO =variable_5 < variable_6
print ("menor igual que")
print( resultado)
# igual
resultado_igual  = "messi" == "cr7"
print("igual")
print ( resultado_igual)
 # diferente 
RESULTADO_diferente = 500 != 500
print("diferente")
print (RESULTADO_diferente)

#and
resultado_and = 500 == 500 and 200
print("and")
print (resultado_and)
#or
resultado_or= 500 == 500  or 200 != 201 or 80 > 100
print("or")
print(resultado_or)
#not
resultado_or = "Not False"
print ( "not")
print ( resultado_or)


# Calcular el descuento de un producto

precio_original = 100

descuento= 20

precio_final=precio_original - (precio_original * descuento / 100)
# comprobar si un año es bisiesto

año=2024

if (año %  4 == 0 and año % 100 != 0) or año  % 400 == 0:
    print("si un año es bisiesto")

#Calcular el área de un círculo
radio = 5
pi = 3.14159 
area = pi * radio **2
#Verificar si un número es par
numero = 12 
if numero % 2 == 0:
   print("El número es par")
   # Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Verificar si puede votar
if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")
    # Solicita dos números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Compara los números
if num1 > num2:
    print(f"El número mayor es {num1}")
elif num2 > num1:
    print(f"El número mayor es {num2}")
else:
    print("Ambos números son iguales")
    #validador de rango de calidad
    calidad = int(input("Ingresa un valor de calidad entre 0 y 100: "))

if calidad >= 80 and calidad <= 90:
    print("Calidad Aceptable")

    # clasificacion de producto por peso 
    peso = float(input("Ingresa el peso del producto (kg): "))

if peso < 5:
    print("Ligero")
elif peso <= 20:
    print("Medio")
else:
    print("Pesado")
    # evaluacion de bonificacion
    salario = float (input( " ingresar el salario"))
    antiguedad = input("ingresar la antiguedad en años")
    if antiguedad >= 10:
        bono = salario * 0,20
    elif antiguedad >=5:
        bono * salario = 0.10
    else: bono = 0
salario_final = salario + bono
print("salario con bono (salario final"))