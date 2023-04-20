""" word = input('Ingresa la palabra clave')

while True:
    if word == 'chupacabras':
        break
    word = input('Ingresa la palabra clave')

print('Has dejado el bucle con éxito') """


""" word = input('Ingresa una palabra')
word = word.upper()

for letter in word:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter) """


""" word = input('Ingresa una palabra')
word = word.upper()

word_without_vowels = ''
for letter in word:
    if letter in ['A','E','I','O','U']:
        continue
    word_without_vowels += letter
print(word_without_vowels)  """


""" bloques = int(input('Ingresa el número de bloques: '))

altura = 0
capa = 1
while capa <= bloques:
    altura = altura + 1
    blocks = blocks - capa
    capa = capa + 1

print(altura) """


""" c0 = int(input('Introduce un número: '))

pasos = 0
#print(c0)
while True:
    if c0 <= 1:
        break
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
    elif c0 % 2 != 0:
        c0 = c0 * 3 + 1
        print(c0)
    pasos = pasos + 1
print(pasos) """


""" for x in range(1,11):
    if x % 2 != 0:
        print(x) """

""" x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x = x + 1 """


correo = input('Introduce una dirección de correo electrónico: ')

nombre = ''
for letter in correo:
    if letter == '@':
        break
    nombre = nombre + letter

print(nombre)