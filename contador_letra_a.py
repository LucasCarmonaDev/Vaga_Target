def contador_letra_a(s):
    return s.lower().count('a')

# Solicita uma string ao usuário
texto = input("Digite um texto para verificar a quantidade de letras 'a': ")

# Conta e exibe a quantidade de letras 'a'
quantidade_a = contador_letra_a(texto)
print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
