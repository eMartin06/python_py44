import random

lista=[]


for _ in range(5):
    szam=random.randint(1,10)
    if szam%2 ==0:
        lista.append(szam)
    
összeg=0
    
for szam in lista:
    összeg+=szam
    
print(lista)
print(összeg)