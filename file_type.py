#Script que busca archivos del tipo shell scripts indicando el número total encontrado, y cuantos de cada tipo hay
#Realizado por Juan Felipe Tapasco Henao - Alvaro Sebastian Tabares Gaviria

import subprocess #Importacion necesaria para ejecutar comandos desde python

#Metodo que contabiliza cuantos scripts hay por cada tipo
#word_list: lista de palabras retornadas por el comando
#return un diccionario con los tipos de script encontrados y el numero de los mismos
def count(word_list):

	counts = dict()

	for w in word_list:
		if w in counts: #si el tipo ya esta en el diccionario le suma 1 al numero de veces que se ha encontrado
			counts[w]+=1
		else: #sino lo agrega al diccionario con un valor de 1
			counts[w]=1

	sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True) #Organiza el diccionario de mayor a menor de acuerdo a la cantidad de veces encontrada una palabra
	return sorted_counts


input_dir = str(input('Ingrese el directorio a inspeccionar: '))

#ejecucion del comando
p = subprocess.run("file -b " + input_dir + "/* | egrep -w 'script|source' | awk {'print $1'}",
	stdout=subprocess.PIPE,
	shell=True)

#Esta variable almacena lo que devuelve el comando ejecutado
file_lines = p.stdout.splitlines()
lines = []


for line in file_lines:
	lines.append(line.decode())

dict_of_script_types = count(lines)

print('En total hay', len(lines),'scripts. Estos scripts se distribuyen de la siguiente manera: ')
for k,v in dict_of_script_types:
	print('{0:2d} {1:3} {2:4}'.format(v,'tipo',k))