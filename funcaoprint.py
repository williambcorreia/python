# Variáveis
a = "pizza"
b = 30

# Valores
print ("O valor da variável A é: ", a)
print ("O valor da variável B é: ", b)
print () # Linha em branco

# Função print
print ("A função print(var) faz com que o conteúdo de uma variável seja impresso na tela. print(a) = ", a)
print () # Linha em branco

# Tabela de tipos de conversão
print ("Para nos orientarmos na instrução a seguir precisamos saber os tipos de conversão. Os tipos são: ")
print () # Linha em branco
print ("d = Decimal inteiro")
print ("f = Decimal ponto-flutuante")
print ("o = Octal")
print ("x = Hexadecimal (min.)")
print ("X = Hexadecimal (mai.)")
print ("c = Um caractere")
print ("s = String.")
print () # Linha em branco

# Formatação de strings
print ("Os objetos possuem um operador de formatação (%), onde formato % valores, em que formato é uma string e as especificações de conversão em formato são substituídas com zero ou mais elementos de valores.")
print ("Quero dizer 'Gosto de pizza', mas não preciso repetir essa palavra todas as vezes se possuo a string em uma variável. Para formatar com a variável A, usamos print('Gosto de %s' % a).")
print ("A letra s que foi utilizada indica o tipo de dados, que neste caso, é uma string.")
print ("Quero utilizar o valor da variável B em uma frase. O que fazer? ('string %d string') % b).")
print ("Resultado: Ela custa %d reais." % b)
print () # Linha em branco
print ("Podemos também substituir mais de um valor, abrindo parênteses no final para utilizar as variáveis, seguindo a ordem da esquerda para a direita. Exemplo:")
print ("print ('A %s custa %d reais' % (a,b)). Resultado: ")
print ("A %s custa %d reais." % (a,b))
print () # Linha em branco

# Método str.format
print ("O método str.format realiza uma operação de formatação de string. A string em que o método é chamado pode conter texto literal ou campos de substituição delimitados por chaves. Esses campos podem conter um índice de posição.")
print ("Se a variável A se encontra na posição 0, então todos os campos com índice de posição 0 serão substituídos pelo valor da string, com a lista de variáveis operando nos índices sempre da esquerda para a direita. Exemplo: ")
print ("Código: print('Gosto de {0}, mas {1} reais está caro para uma {0}'.format(a,b))")
print ("Resultado: Gosto de {0}, mas {1} reais está  caro para uma {0}!".format(a,b))
