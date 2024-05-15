'''
Este algoritmo administra el stock de una tienda
'''
import os
stock = {'Escobas': 5, 'Huevos':25, 'Leche':9, 'Harina':0}
menup = ['Ver stock de productos', 'Añadir nuevo prducto', 'Ajustar stock', 'Eliminar producto', 'Salir']

while True:
    for ind, opt in enumerate(menup):
        print(f'{ind + 1}. {opt}')
    respuesta = input('Que quieres hacer:\n')
    if respuesta == '1':
        os.system('cls')
        for numero, productito in stock.items():
            print(f'{numero}, {productito}')
    elif respuesta == '2':
        os.system('cls')
        for llave in stock:
          newproducto = input('Ingresa el nombre del nuevo producto:\n')
          newcantidad =int (input('Ingresa la Cantidad que deseas añadir:\n'))
          respuesta = input('Estas seguro que quieres añadir este producto al stock (s/n)\n')
          if respuesta.lower() ['s', 'si']:
              print('Su producto se guardo exitosamente:\n')
              break
          elif respuesta.lower() ['n', 'no']:
            continue
    elif respuesta == '3':
        os.system('cls')
    elif respuesta == '4':
        os.system('cls')
        while True:
            try:
                respuesta = str(input('Que producto desea eliminar:\n'))
                continue
            except:
                os.system('cls')
                print('Error: Ingrese un producto de la lista ')
                break
    elif respuesta == '5':
        os.system('cls')
        exit('Hasta pronto\n')
    else:
        os.system('cls')
        print('Error: la respuesta que ingresaste es invalida:\n')
    

