# Variáveis
a = "Abacaxi"
s = "Pizza"
x = len(s)
l = "a,b,c,d,e,f,g,h"

# Valores
print ("O valor atribuído para a variável A é: ", a)
print ("O valor atribuído para a variável S é: ", s)
print ("O valor atribuído para a variável L é: ", l)
print () # Linha em branco

# Função len()
print ("Para ver o tamanho da string, utilizamos a função len(). Len é a abreviação de Length, que significa comprimento.")
print ("O valor da variável S é Pizza, e seu comprimento é: ", x)
print () # Linha em branco

# Função print com índice
print ("Para acessar caracteres individuais, utilize print(var[p]). Sendo p a posição do caractere, da esquerda para direita começando em 0.")
print ("O caractere na posição 0 da variável S é: ", s[0])
print ("O caractere na posição 3 da variável S é: ", s[3])
print () # Linha em branco
print ("Demonstração da função print(var[p]) na variável S com as 5 posições: ")
print (s[0])
print (s[1])
print (s[2])
print (s[3])
print (s[4])
print ()

# Função print com slicing
print ("Slicing ou fatiamento permite retornar pedaços da string. O número limite deve ser uma unidade maior, pois o limite sempre será subtraído por 1.")
print ("A função print(s[:]) retorna a string inteira. Resultado: ", s[:])
print ("A função print(s[1:3]) retorna os caracteres da posição 1 e 2. Resultado: ", s[1:3])
print ("A função print(s[:4]) retorna todos os caracteres até a posição 3. Resultado: ", s[:4])
print ("A função print(s[1:]) retorna todos os caracteres a partir da posição 1. Resultado: ", s[1:])
print () # Linha em branco
print ("Quando utilizamos um índice negativo, as posições são contadas da direita para a esquerda.")
print ("A função print(s[-1]) retorna o último caractere da string. Resultado: ", s[-1])
print ("A função print(s[-2]) retorna o penúltimo caractere da string. Resultado: ", s[-2])
print () # Linha em branco

# Função print com concatenação
print ("Concatenação é o processo de 'juntar' duas ou mais strings, formando uma nova. O sinal de concatenação é +.")
print ("A função print(s + ' portuguesa') concatena a string da variável com a palavra portuguesa. Resultado: ", s + " portuguesa")
print ()

# Função print com repetição
print ("Repetição é o processo de repetir uma sequência de caracteres determinado número de vezes. O sinal de repetição é *.")
print ("A função print(s * 6) repete a string na variável 6 vezes. Resultado: ", s * 6)
print ("A função print((s + ' ') * 6) repete a string na variável 6 vezes com espaços. Resultado: ", (s + " ") * 6)
print ()

# Teste
print ("Qual comando permite retornar os 3 primeiros caracteres da string Linux?")
print ("Resposta: print(s[0:3])")
print ()

# Métodos em strings
print ("Os métodos podem ser aplicados a strings, existindo vários deles com funções diferentes.")
print ("O método var.find('substring') encontra a posição de uma substring. A posição de 'iz' na variável S é: ", s.find("iz"))
print ("O método var.replace('item','item') substitui uma substring por outra. Ao substituir 'zza' por 'nhão' na variável S, o resultado é: ", s.replace("zza","nhão"))
print ("O método var.upper() deixa a string inteira em letras maiúsculas. Exemplo na variável S: ", s.upper())
print ("O método var.lower() deixa a string inteira em letras minúsculas. Exemplo na variável S: ", s.lower())
print ("O método var.isalpha() diz se a string é composta apenas por letras do alfabeto. A variável S é alfabética? ", s.isalpha())
print ("O método var.isalnum diz se a string é composta por letras ou números. A variável S é alfanumérica? ", s.isalnum())
print ("O método var.lstrip('substring') retorna uma cópia da string removendo caracteres à esquerda. Se utilizado sem um argumento nos parênteses, elimina espaços em branco. Utilizando o parâmetro 'P' na variável S, o resultado é: ", s.lstrip("P"))
print ("O método var.rstrip('substring') tem a mesma função do lstrip, mas à direita. Utilizando o parâmetro 'a' na variável S, o resultado é: ", s.rstrip("a"))
print ("A função var.strip() remove espaços em ambas as direções.")
print ("A função var.capitalize() retorna a string com o primeiro caractere maiúsculo.")
print ("A função var.split() retorna uma lista de itens delimitada pelo caractere especificado. Utilizando o método l.split(','), o resultado é: ", l.split(","))
