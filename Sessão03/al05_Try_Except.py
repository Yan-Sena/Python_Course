Idade = input("Digite sua idade: ");    

while True:
    try:
        Idade = int(Idade);    
        break
    except ValueError:
        print("Erro: Idade deve ser um numero inteiro, animal.")
        Idade = input("Digite sua idade: ");
