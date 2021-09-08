from os import path, pipe, umask
import re
from typing import Match
import math


try:
    entrada = open(r"C:\Users\lucianoq\OneDrive\DesafioTopaz\input.txt")
except:
    print("MUDAR A LOCALIZAÇÃO DO ARQUIVO INPUT")

#determinar ttask e umax 
for i,line in enumerate(entrada):
    line.strip()
    if(i==0):
        try:
            ttask = int(line)
        except:
            print("Valor de ttask deve ser numerico")
    elif(i==1):
        try:
            umax = int(line)
            break
        except:
            print("Valor de Umax no arquivo input deve ser numerico")
#definir quantos usuarios irao entrar
ticks = []
for line in entrada:
    ticks.append(int(line))

#definir quando os usuarios irao sair
remover = []
for i,usuario in enumerate(ticks):
    remover.append(i+ttask + 1)

#separar os usuarios pelo tamanho de ttask
t=[]
for i,element in enumerate(ticks):
    
    t.append(ticks[i:ttask + i])


agruparTotal = []
somar = 0
soma = 0

#Primeiro for consegue o numero de usuarios dos 3 primeiros ticks
for i in range(3):
    
    if i == 0:
        agruparTotal.append(t[0][i])
        soma += t[0][i]
    else:
        soma += t[0][i]
        agruparTotal.append(soma)

#com os usuarios agrupados por ttask, são somados para descobrir quantos usuarios havera em cada tick
for i,listTick in enumerate(t):
           
    for  lista in listTick:
            somar += lista
    agruparTotal.append(somar)
    somar = 0        

servidor=[]

#determinar o numero de servidores usando uumax


resultado = 0
for i,tick in enumerate(agruparTotal):

    resultado = (tick / umax)
    servidor.append(math.ceil(resultado))

resultado = 0
output = []
  
ler = open(r"C:\Users\lucianoq\OneDrive\DesafioTopaz\output.txt","w")

for i,servidores in enumerate(servidor):
    ler.write("{} servidores para {} usuarios\n".format(servidores,agruparTotal[i]))

#numero de usuarios que entraram por tick
ler.write("numero de usuarios que entraram:{}\n".format(ticks))
#posição de quando devera remover os usuarios
ler.write("posição de quando devera remover os usuarios:{}\n".format(remover))    
#numero de servidores criados
ler.write("numero de servidores criados por tick:{}\n".format(servidor))
#numero de usuarios totais por tick
ler.write("numero de usuarios totais por tick:{}\n".format(agruparTotal))


    





        
   






   
