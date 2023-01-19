

# Python >> 05. Laços de Repetição (while) >> Quantos uns

# Quantos uns

# Escreva uma função que recebe um número e devolve a quantidade de vezes que o algarismo 1 ocorre nesse número.
# Sua função deve se chamar quantos_uns


def quantos_uns(numero):

    contador_de_uns = 0

    while numero > 0:
        
        if numero % 10 == 1:
            contador_de_uns +=1

        numero = numero //10

    
    return contador_de_uns

resultado = quantos_uns(21)
print(resultado)