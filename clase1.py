print("¿Cuáles son los dos valores del tipo de datos booleano? ¿Cómo se escriben?")
print("Verdadero y falso, se escriben True y False")
print("")
print("¿Cuáles son los tres operadores booleanos?")
print("not, and y or")

print("")

print("Escriba una rutina que genere todas las tablas de verdad de cada operador booleano (es decir, cada combinación posible de valores booleanos para cada  operador).")

print("")
A=[True , False]
B=[True , False]
print("")
print("NOT")
print("A     not A")
for n in A:
	print(str(n)+"   "+str(not (n)))

print("")
print("")

print("AND") 
print("A       B      A and B")
for n in A:
	for m in B:
		print(str(n)+"   "+(str(m))+"   "+str(m and n))
print("")
print("")

print("OR")

print("A       B      A or B")
for n in A:
        for m in B:
                print(str(n)+"   "+(str(m))+"   "+str(n or m))
print("")

print("¿Cuáles son los seis operadores de comparación?")
print("")
print("igualdad (==), no igualdad (!=), mayor que (>), menor que (<), mayor o igual que(>=), menor o igual que(<=) ")

print("")

print("¿Cuál es la diferencia entre el operador igual y el operador de asignación?")

print("")

print("el operador igual (==) sirve para comparar y cuando se usa resulta en un True o False, el operador asignación sierve para asignarle un valor a una variable")
print("")
print("Explique qué es una condición y dónde la usaría.")
print("")
print("Es una sentencia que puede resultar en True o False y dependiendo del resultado hace o no alguna acción. Puede utilizarse para delimitar cuando termina un bucle")
print("")
print("¿Qué puede hacer si su programa está atascado en un bucle infinito?")
print("presionar (ctrl+c) o insertar en la consola top, encontrar el número del proceso que está en el bucle, regresar a la consola e insertar kill -9 (numero de proceso)")
print("")
print("¿Cuál es la diferencia entre romper y continuar?")
print("")
print("Romper sirve para salir de un bucle cuando se cumpla alguna condición, continuar sirve para no hacer una parte del ciclo pero continuar con el ciclo normal")
print("")
print("¿Cuál es la diferencia entre rango (10), rango (0, 10) y rango (0, 10, 1) en un bucle for?")
print("")
print("en este caso no hay diferencia, pero si en vez de (0,10) y (0,10,1) furean (1,10) o (0,10,2) si habría ya que los otros parámetros marcan desde donde inicia y si se salta numeros o no")

print("Escribe un programa corto que imprima los primeros N números y la suma de mismos N usando un bucle for. Luego escribe un programa equivalente que imprima los números del 1 al 10 usando un bucle while.")
#XXXXXXXXXXXXXXXXXXXXXXXXXXX Xcon for XXXXXXXXXXXXXXXXXXXX 

#a es la suma acumulada
a=0
print("dime un numero")
N=int(input())
#N es el número que uso para delimitar el rango
#n va a contar desde el 0 hasta n-1 
for n in range(N):
#uso (n+1) para empezar en 0 y terminar en N
	print (n+1)
	a=a+n+1
print("la suma de 1 hasta "+str(N)+" es: "+  str(a))

#con while
n=1
a=0
while n<11:
	print(n)
	a=a+n
	n=n+1
print(a)

print("")
print("Un ciclo que imprima los primeros M números impares.")
print("dime un número")
M=int(input())
print("los primeros "+str(M)+" numeros impares son")
for a in range(M):
	print(2*(a+1)-1)

print("")

print("Escriba un programa que calcule los primeros N términos de la serie de fibonacci.")
print("dime un número")
N=int(input())
print("los primeros "+str(N)+" términos de fivonacci son:")
#primero tengo una lista L con los primeros dos términos
L=[1,1]
nuevo=0
if N==1:
	print(1)
else:
	while len(L)<N:
		nuevo=L[-1]+L[-2]
		L.append(nuevo)
	print(L)
print("")
print("Escriba un programa que calcule el factorial de un número N.")
producto=1
print("Dime un número")
N=int(input())
print(str(N) + "! es:")
for x in range(N):
	producto=producto*(x+1)
print(producto)

