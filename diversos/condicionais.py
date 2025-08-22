n1 = 6.0
n2 = 7.0
media = (n1 + n2) /  2

if media >= 7.00:
    print ("Aluno aprovado!")
    print () #Linha em branco
else:
    if media >= 5.00:
        print ("Aluno de recuperação.")
        print () #Linha em branco
    else:
        print ("Aluno reprovado.")
        print () #Linha em branco

print ("Média do aluno: %f" % media)
