def prefixo ():
    texto1 = input('Digite alguma coisa: ')
    texto2 = input('Digite outra coisa: ')
    
    for letra_texto1 in texto1:
        for letra_texto2 in texto2:
            if letra_texto1 == letra_texto2:
                return True
            else:
                return False
    
print(prefixo())