
user_word = input("Ingresa una palabra: ")


user_word = user_word.upper()


word_without_vowels = ""

# Iterar sobre cada letra en la palabra
for letter in user_word:
    # Si la letra es una vocal, continuar con la siguiente iteración
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    # Concatenar las letras no consumidas a la variable word_without_vowels
    word_without_vowels += letter

# Imprimir la variable word_without_vowels
print(word_without_vowels)
