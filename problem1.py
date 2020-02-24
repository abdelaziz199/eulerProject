# mathematical problem
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


number_limit = int(input('enter the limit:'))
multiple_trois = int(input('enter the first multiple:'))
multiple_cinq = int(input('enter second multiple :'))
sum =0
cpt =1 
while cpt < number_limit:
    
    if cpt%multiple_three == 0 or cpt%multiple_five == 0:
        sum += cpt
        
    cpt += 1
        
print(sum)
