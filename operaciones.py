def sumar(num1, num2):
    """realizar suma

    Args:
        num1 (float): operando 1
        num2 (float): operando 2

    Returns:
        float: suma
    """
    return num1 + num2


def restar(num1, num2):
    """realizar resta

    Args:
        num1 (float): operando 1
        num2 (float): operando 2

    Returns:
        float: resta
    """
    return num1 - num2


def multiplicar(num1, num2):
    """realizar multiplicacion

    Args:
        num1 (operando): operando 1
        num2 (operando): operando 2

    Returns:
        float: multiplicacion
    """
    return num1 * num2


def dividir(num1, num2):
    """realizar division

    Args:
        num1 (float): operando 1
        num2 (float): operando 2

    Returns:
        float: division
    """
    if num1 == 0 or num2 == 0:
        return 'No se puede dividir por 0'
    return num1 / num2


def factorial(numero):
    """factorizar un numero

    Args:
        numero (float): numero que se va a realizar el factorial

    Returns:
        float: factorial
    """
    if numero >= 0:
        fact = 1
        for i in range(1, int(numero) + 1):
            fact *= i
        return float(fact)
    else:
        return 1.0