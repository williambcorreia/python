# Importação do módulos random e math
import random
import math

# Variáveis
n = random.random()
n10 = 10 * random.random()
ln = random.choice ([2,4,6,8,10,12])
f = random.choice (["Laranja","Banana","Mamão","Abacate"])

# Aplicações do módulo random
print ("A função random.random() gera um número aleatório entre 0 e 1, sendo o número desta vez: ", n)
print () # Linha em branco
print ("Ao multiplicarmos pelo valor limite desejado, por exemplo 10, temos o resultado de: ", n10)
print ("O valor arredondado é: ", math.ceil(n10))
print () # Linha em branco
print ("Tenho uma lista de números de 2 até 12, aumentando 2 em sequência. Para escolher entre um desses números, utilizamos a função random.choice([item,item,...]).")
print ("O número escolhido foi: ", ln) 
print () # Linha em branco
print ("A função random.choice também pode usar caracteres. Gosto destas frutas, mas só posso escolher uma: laranja, banana, mamão e abacate.")
print ("A fruta escolhida foi: ", f)
