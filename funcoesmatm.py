# Importação do módulo math
import math

# Variáveis
w = 3.5
x = 81
y = -5
z = 6
teste = math.log10(math.sqrt(math.pow(2,7) - 2 ** 2 * 7))

# Valores
print ("O valor de Pi é: ", math.pi)
print () # Linha em branco
print ("o valor de W é: ", w)
print ("O valor de X é: ", x)
print ("O valor de Y é: ", y)
print ("O valor de Z é: ", z)
print () # Linha em branco

# Aplicações do módulo math
print ("O valor da raiz quadrada de X é: ", math.sqrt(x))
print ("O valor absoluto de Y é: ", math.fabs(y))              
print ("O valor fatorial de Z é: ", math.factorial(z))
print ("O valor de Z, num logaritmo de base 10 é: ", math.log10(z))
print ("O valor de Y elevado a Z é: ", math.pow(y,z))
print ("O valor de W arredondado para cima é: ", math.ceil(w))
print ("O valor de W arredondado para baixo é: ", math.floor(w))
print () # Linha em branco

# Questão
print ("Qual o valor retornado pela seguinte expressão?")
print () # Linha em branco
print ("math.log10(math.sqrt(math.pow(2,7)-2**2*7))")
print () # Linha em branco
print ("Resultado: ", teste)
