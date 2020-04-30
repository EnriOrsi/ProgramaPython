
#Nome: Enri Bernardi Carvalho Orsi | TIA: 32008661 | Sala: 01N

# -*- coding: utf-8 -*-
import time
cont = 0
listaPeso = []
listaAltura = []
listaIdade = []
qtdSenior = 0
qtdJovem = 0
qtdSobPeso = 0
saltura = 0

for cont in range(30):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: (em metros) "))
    peso = float(input("Digite seu peso: (em Kg) "))
    listaIdade.append(idade)
    listaAltura.append(altura)
    listaPeso.append(peso)

for cont in range(30):
    if listaIdade[cont] >= 50:
        qtdSenior += 1

for cont in range(30):
    if listaIdade[cont] >= 10 and listaIdade[cont] <= 20:
        saltura = saltura + listaAltura[cont]
        qtdJovem += 1
mAlturaJovem = saltura/qtdJovem

for cont in range(30):
    if listaPeso[cont] > 40:
        qtdSobPeso += 1

pctgPessoasSobPeso = (qtdSobPeso*100)/30

print("A quantidade de pessoas que tem 50 anos ou mais é: ", qtdSenior)
print("A média das alturas das pessoas com idade entre 10 e 20 anos é: %.2f"%mAlturaJovem)
print("A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas é: %.2f"%pctgPessoasSobPeso)
