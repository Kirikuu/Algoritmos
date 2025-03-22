'''
Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división
'''

Numero1 = int(input("Ingrese su primer numero: "))  #Dividendo
Numero2 = int(input("ingrese su segundo numero: "))  #Divisor

Division = Numero1 / Numero2
Residuo = Numero1 % Numero2

print(f"Su dividendo es {Numero1} y su divisor es {Numero2}, el resultado de esta operación es: {Division} y su residuo es {Residuo}")