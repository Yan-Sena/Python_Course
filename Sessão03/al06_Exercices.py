Nu = input("Digite um numero inteiro: ")

#Verificando se o numero é valido.
while True:
    try:
        Nu = int(Nu);    
        break
    except ValueError:
        print("Erro: O Número deve ser um numero inteiro.")
        Nu = input("Digite UM NUMERO INTEIRO: ")
        
#Testando se é par ou impar.  
if (Nu % 2) == 0:
    print(f"O número {Nu} é um numero PAR")
else:
    print(f"O número {Nu} é um numero IMPAR")
    
    
