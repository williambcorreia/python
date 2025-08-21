nota1 = 6.00
nota2 = 7.00
media = (nota1 + nota2) / 2

if media >= 7.00:
    print ("O aluno foi aprovado!")
    print ("Parabéns!")
    print () #Linha em branco
else:
    if media >= 5.00:
        print ("O aluno está na recuperação.")
        print ("Que aproveite a segunda chance.")
    else:
        print("O aluno foi reprovado.")
        print ("Estude mais!")

print() #Linha em branco
print ("A média do aluno foi: %f" % media)
