# on listons les nombres inferieurs a 10 , 
# on prend 3 ou 5 ,on cherche les multiples de 3 ou bien 5   , dans le cas de 10   3= 3,6,9  . 5=5
# on fait la somme = 3+6+9+5=23


# le probleme on cherche la somme des multiples de 3 ou 5 en dessous de 1000



number_limit = int(input('entrer le nombre limite :'))
multiple_trois = int(input('entrer le premier multiple :'))
multiple_cinq = int(input('entrer le deuxieme multiple :'))
somme =0
cpt =1 
while cpt < number_limit:
    
    if cpt%multiple_trois == 0 or cpt%multiple_cinq == 0:
        somme += cpt
        
    cpt += 1
        
print(somme)