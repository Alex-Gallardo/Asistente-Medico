#!/usr/bin/env python
#_*_ coding: utf8 _*_
# Botiquin
# Enfermedades basicas
# Accidentes
# Banner
import helper

print('\u001b[32;1m\n     _____  \u001b[0;m                                  \u001b[32;1m                                        \u001b[0;m')
print('\u001b[32;1m  __|_    |__ \u001b[0;m\u001b[31;1m     __     \u001b[0;m\u001b[32;1m ______    ____   _    ______    ____    _____    ____   _  \u001b[0;m')
print('\u001b[32;1m |    \      |\u001b[0;m\u001b[31;1m   _|  |_   \u001b[0;m\u001b[32;1m|   ___|  |    \ | |  |   ___|  |    |  /     \  |    \ | | \u001b[0;m')
print('\u001b[32;1m |     \     |\u001b[0;m\u001b[31;1m  |_    _|  \u001b[0;m\u001b[32;1m|   ___|  |     \| |  |   |__   |    |  |     |  |     \| | \u001b[0;m')
print('\u001b[32;1m |__|\__\  __|\u001b[0;m\u001b[31;1m    |__|    \u001b[0;m\u001b[32;1m|______|  |__/\____|  |______|  |____|  \_____/  |__/\____| \u001b[0;m')
print('\u001b[32;1m    |_____|   \u001b[0;m                                  \u001b[32;1m                                      \u001b[0;m')
print('\u001b[31;1m\t\t                  ______________                ')
print('\t\t_______ ___ _____ ______  /___(_)_____________ _')
print('\t\t__  __ `__ \_  _ \_  __  / __  / _  ___/_  __ `/')
print('\t\t_  / / / / //  __// /_/ /  _  /  / /__  / /_/ / ')
print('\t\t/_/ /_/ /_/ \___/ \__,_/   /_/   \___/  \__,_/  \u001b[0;m')

# Area de variables globales
a = True

# Area de funciones (helpers)
def set_texto( cad_texto ):
    ordenado = []
    for texto in cad_texto:
            palabra_compuesta = ''
            for letra in texto:
                if letra != ' ':
                    palabra_compuesta += letra 
            ordenado.append(palabra_compuesta)
    return ordenado

def searh_symptoms( cad_texto ):
    helper.node_searh_symptoms( cad_texto )
    

# Algoritm
while a == True:
    print('\x1b[33;3m\n[*] Secuencia de atencion.\x1b[0;m\n')
    print(' [0] \u001b[31;1mUrgencia...\u001b[0;m')
    print(' [1] Ayuda asistida')
    atencion = input(' - : ')
    if atencion == '-E' or atencion == ' -E' or atencion == '-E ':
        print('\n\n\u001b[32;6m----------------------------------------\n*-*-*  Modo de edicion habilitada  *-*-*\n----------------------------------------\u001b[0;m\n')
        nombre = input('[*] Ingrese el nombre la enfermedad: ').lower()
        sintomas = input('[*] Ingresa los sintomas: ').lower()
        solucion = input('[*] Ingrese la solucion: ')
        data_tmp = set_texto([nombre])
        helper.write_information([data_tmp[0], set_texto(sintomas.split(',')), solucion])
    elif int(atencion) == 0:
        print('\u001b[32;1m\n[*] Ingrese los sintomas separado por "," Ej: dolor de cabeza, vomitos, nauseas,etc\u001b[0;m')
        sintomas = input(' - : ').lower()
        sintomas2 = sintomas.split(',')
        sintomas3 = set_texto(sintomas2)
        # Buscar en el archivo correspondiente
        searh_symptoms(sintomas3)
        a = True
    elif int(atencion) == 1:
        print('\n----------------------------------\n[1]\u001b[32;1m Que hacer con un Botiquin.\u001b[0;m')
        print('[2] Enfermedades basicas.')
        print('[3] \u001b[31;1mAccidentes ( dentro de casa )\u001b[0;m')
        print('[4] \u001b[31;1mAccidentes ( fuere de casa )\u001b[0;m')
        print('[5] Ayuda sobre el programa')
        print('[6] Salir')
        opciones = int(input(' - : '))
        if opciones == 1:
            response = helper.node_read_botiquin();
            for a_txt in response:
                for i in range(len(a_txt)):
                    if i == 0:
                        print('\u001b[32;1m'+a_txt[i]+'\u001b[0;m')
                    else:
                        print(' · '+a_txt[i])
                
        elif opciones == 2:
                print('\u001b[32;1m\n[*] Ingrese los sintomas separado por "," Ej: dolor de cabeza, vomitos, nauseas,etc\u001b[0;m')
                sintomas = input(' - : ').lower()
                sintomas2 = sintomas.split(',')
                sintomas3 = set_texto(sintomas2)

        elif opciones == 3:
            # print('\u001b[32;1m\n[*] Idique el tipo de accidente\u001b[0;m')
            res = helper.node_accidents()
            print(res[0])
        elif opciones == 4:
            pass
        elif opciones == 5:
            pass
        elif opciones == 6:
            pass
        a = True
    else:
        print('\tIngrese un valor correcto, no estamos para bromas xd!!')
