characters_file = open("meus-personagens-favoritos.txt", mode='w')

characters_file.write('Luffy\n')
characters_file.write('Zoro\n')
characters_file.write('Nami\n')
characters_file.write('Chopper\n')

print('Robin', file=characters_file)

more_characters = ['Sanji\n', 'Sogeking\n']

characters_file.writelines(more_characters)

characters_file.close()

# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    print(line)
    # não esqueça que a quebra de linha também é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo
