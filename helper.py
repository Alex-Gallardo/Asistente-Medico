"""
@license
Copyright (c) 2020 Autor Alex G. Todos los derechos reservados.
Se trabaja con la edicion y modificacion de ficheros para almacenar informacion importante y
decidi hacer este modulo que contiene poca informacion y algunas funciones.
Cabe a destacar que este programa solo cubre algunas de las enfermedades basicas y accidentes basicos, aun asi
esta programado para guardar nuevas enfermedades/accidentes con sus respectivas atenciones medicas. Para ello
ingresar el comando -E en [*] Secuencia de atencion
"""
#!/usr/bin/env python
#_*_ coding: utf8 _*_
import re

# Buca en el fichero por sintoma y devuelve su informacion
def read_information(sintoma):
    information = {}
    data = open("data.txt", 'r')
    tmp = data.read()
    tmp2 = tmp.split('\n')
    for txt in tmp2:
        val = txt.split(':')
        if len(val) > 1:
            information[val[0]] = val[1].split('|')
    print(information)
    data.close()
    return information.get(sintoma)

# Escribe en el fichero un nuevo registro
def write_information( info ):
    data = open('data.txt','a')
    sintomas = ''
    for i in range(len(info[1])):
        if i == 0:
            sintomas += info[1][i]
        else:
            sintomas += ','+info[1][i]
    data.write(info[0]+':'+info[1]+'|'+info[2]+'\n')
    data.close()

# Funcion especial para el resultado de botiquin
def node_read_botiquin():
    information = []
    data = open("data.txt", 'r')
    tmp = data.readlines()[0]
    tmp2 = tmp.split('|')
    for txt in tmp2:
        val = txt.split(';')
        if val[0] != '':
            information.append(val)       
    data.close()
    return information

def node_searh_symptoms(cadena):
    information = {}
    data = open("data.txt", 'r')
    tmp = data.read()
    tmp2 = tmp.split('\n')
    for txt in tmp2:
        val = txt.split(':')
        if len(val) > 1:
            information[val[0]] = val[1].split('|')
    for sintoma in cadena:
        print(sintoma)
        for key in information:
            print(information[key][0].split(','))
    data.close()
    # return information.get(sintoma)

# Basado en "Valoración neurológica mediante la escala de Glasgow"
def node_accidents():
    info = []
    print('\u001b[32;1m · Tiene los ojos abiertos?\u001b[0;m\n[1] Nunca. \n[2] Sólo al estímulo doloroso. \n[3] Con estímulo verbal. \n[4] De manera espontánea.')
    ojos_abiertos = int(input(' -: '))
    print('\u001b[32;1m · Respuesta verval?\u001b[0;m\n[1] Sin respuesta. \n[2] No comprensible. \n[3] Incoherencia. \n[4] Habla desorientado. \n[5] Habla orientado. ')
    respuesta_verval = int(input(' -: '))
    print('\u001b[32;1m · Respuesta motora?\u001b[0;m\n[1]Sin respuesta. \n[2]Extensión ante el estímulo. \n[3]Flexión anormal. \n[4]Retira ante estímulos dolorosos. \n[5]Localiza el estímulo doloroso. \n[6]Obedece las órdenes. 6')
    respuesta_motora = int(input(' -: '))
    resultado = ojos_abiertos + respuesta_verval + respuesta_motora
    if resultado == 15:
        info = ['Paciente en estado normal', 0]
        return info
    elif resultado == 14:
        info = ['Traumatismo generalizado', 1]
        return info
    elif resultado <= 13 and resultado >= 9:
        info = ["Politraumatismo", 2]
        return info
    elif resultado < 9:
        info = ['Traumatismo craneoencefálico grave', 3]
        return info
