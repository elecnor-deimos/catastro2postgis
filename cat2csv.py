#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import csv

from catstruct import catstruct # define la estructura de un .CAT

if (len(sys.argv)<3):
	print """Convierte un .cat de Catastro a .csv.
	
	Uso: cat2csv.py fichero.cat path_destino
"""
	sys.exit(2)
	
inputfile=sys.argv[1]
basedir=sys.argv[2]

rf = open(inputfile) # input file
wf = {}              # output files

# Generamos un CSV por cada tipo de registro
for tipo in catstruct:
    filename = basedir+'/cat_'+str(tipo)+'.csv'
    print 'Creando ' + filename;
    wf[tipo] = open(filename, 'w')
    # Escribimos primer registro con nombres de campos
    csv.writer(wf[tipo]).writerow(zip(*catstruct[tipo])[3])

# Leemos .cat registro a registro
for line in rf.readlines():
    line = line.decode("UTF8")
    row = []
    tipo = int(line[0:2])
    # Parseamos si conocemos la estructura del tipo de registro
    if tipo in catstruct:
        for campos in catstruct[tipo]:
            ini = campos[0]-1 # offset
            fin = ini + campos[1] # longitud
            valor = line[ini:fin].strip().encode("UTF8") # valor
            row.append(valor)
        csv.writer(wf[tipo]).writerow(row)

# close input file handle
rf.close()  

# close output file handles
for f in wf:
    wf[f].close()

