nome_completo = "Yan Sena";
idade_aluno = 19;
bairro_aluno = "Liberdade";
maioridade = False;

#Aula ainda não chegou aos if's apenaas testando. 

if idade_aluno >= 18:
    maioridade = True;
else: 
    maioridade = False;


print("Olá, " + nome_completo + " bem vindo ao curso de python intermediario");

if maioridade == True:
    print("Você é maior de idade.");
else:
    print("Você é menor de idade.");
    