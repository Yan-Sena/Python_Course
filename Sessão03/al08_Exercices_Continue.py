#Faça um codigo que mostre números impares entre 0 e 100 usando o continue e o While cYS

contador = 0

while contador < 100:
    contador += 1;
    
    if (contador % 2) == 0:
        continue    
    
    print(contador)
        
