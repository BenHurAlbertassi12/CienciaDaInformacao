import random

random_number = random.randint(1, 10)
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))
    # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)
