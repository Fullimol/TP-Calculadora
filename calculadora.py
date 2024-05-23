from os import system
from operaciones import *

def clean_screen():
    system('cls')

def pause_screen():
    system('pause')

def menu_calculadora(num1, num2, operaciones):
    """Listado de funciones para la calculadora

    Args:
        num1 (float): recibe el primer operando
        num2 (float): recibe el segundo operando
        operaciones (list): recibe las operaciones seleccionadas

    Returns:
        _type_: _description_
    """
    clean_screen()
    print(f'\tMENU DE OPCIONES')
    print(f'1) Ingrese 1er operando: {num1}')
    print(f'2) Ingrese 2do operando: {num2}')
    print(f'3) Agregar operacion a realizar: {operaciones}')
    print('4) Informar resultados')
    print('5) Salir')

    seleccion =  input(f'\n\tIngrese opcion: ')
    while seleccion not in ['1', '2', '3', '4', '5']:
        print(f'ERROR: OPCION {seleccion} NO VALIDA')
        seleccion =  input(f'\n\tIngrese opcion: ')
    return seleccion
    

def menu_operaciones():
    """Submenu para elegir las operaciones a realizar
    """

    print(f'\n\tMENU DE OPERACIONES')
    print('a) Sumar')
    print('b) Restar')
    print('c) Division')
    print('d) Multiplicacion')
    print('e) Factorial')
    print('')
    print('f) RESET SELECCIONADAS')
    print('g) VOLVER ATRAS')


def validar_numeros_ingresados(prompt):
    """Validamos que se haya ingresado un numero

    Args:
        prompt (str): ingresamos el prompt para mostrar en el input

    Returns:
        float: devolvemos el valor numerico en flotante
    """
    while True:
        numero_ingresado = input(prompt)
        try:
            numero_ingresado_validado = float(numero_ingresado)
            return numero_ingresado_validado
        except ValueError:
            print("ERROR: Por favor ingrese un número.")


def verificar_operacion(lista: list, target:int)-> bool:
    """Verifica si la operación ya se seleccionó

    Args:
        lista (list): recibe la lista de operaciones
        target (str): recibe la operación

    Returns:
        bool: devuelve True o False si la operación ya está seleccionada
    """
    for i in range(len(lista)):
        if lista[i] == target:
            return True
    return False

# **********************************************************

num1 = "(no indicado)"
num2 = "(no indicado)"
operaciones = []

while True:
    match menu_calculadora(num1, num2, operaciones):
        case '1':
            num1 = validar_numeros_ingresados('\nIngrese 1er operando: ')

        case '2':
            num2 = validar_numeros_ingresados('\nIngrese 2do operando: ')

        case '3':
            menu_operaciones()
            operacion_a_realizar = input('Operación a realizar: ')
            while operacion_a_realizar not in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] or verificar_operacion(operaciones, operacion_a_realizar) == True:
                print(f'ERROR: OPCION {operacion_a_realizar} NO VALIDA')
                operacion_a_realizar = input('Operación a realizar: ')

            if operacion_a_realizar == 'f':
                operaciones = []
            elif operacion_a_realizar == 'g':
                continue
            else:
                operaciones.append(operacion_a_realizar)
            # pause_screen()

        case '4':
            if num1 == "(no indicado)" or num2 == "(no indicado)" or len(operaciones) == 0: 
                print(f'\nPrimero debes indicar los operandos y las operaciones')
                pause_screen()
                continue
            else:
                print(f'\n\tRESULTADOS')
                for operacion in operaciones:
                    if operacion == 'a':
                        print(f'El resultado de la suma es: {sumar(num1, num2)}')
                    if operacion == 'b':
                        print(f'El resultado de la resta es: {restar(num1, num2)}')
                    if operacion == 'c':
                        print(f'El resultado de la division es: {dividir(num1, num2)}')
                    if operacion == 'd':
                        print(f'El resultado de la multiplicacion es: {multiplicar(num1, num2)}')
                    if operacion == 'e':
                        print(f'El factorial de {num1} es: {factorial(num1)}')
                        print(f'El factorial de {num2} es: {factorial(num2)}')
            pause_screen()
            
        case '5':
            print(f'\n ¿Confirmar salida? (s/n)')
            if input() == 's':
                break
            continue

    clean_screen()


print(f'\n\tFIN DEL PROGRAMA')
