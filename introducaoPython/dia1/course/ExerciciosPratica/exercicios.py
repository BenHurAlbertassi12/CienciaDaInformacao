#  Crie uma função que receba dois números e retorne o maior deles.


def maior(number1, number2):
    if number1 > number2:
        return number1
    return number2


# Calcule a média aritmética dos valores contidos em uma lista.

def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


# faça um programa que, dado um valor n qualquer, tal que n > 11
# imprima na tela um quadrado feito de * de lado e tamanho n

def draw_square(n):
    for row in range(n):
        print(n * '*')


# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Crie uma função que retorne dois valores em uma tupla contendo a
# quantidade de latas de tinta a serem compradas e o preço total
# a partir do tamanho de uma parede (em m²).

def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price


# Crie uma função que receba os três lado de um triângulo e
# informe qual o tipo de triângulo formado ou "não é triangulo",
# caso não seja possível formar um triângulo.

def type_of_triangle(side1, side2, side3):
    is_triangle = (
        side1 + side2 > side3 and
        side2 + side3 > side1 and
        side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"
