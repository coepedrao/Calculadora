print ('Digite um número: ')
num = int(input())

print ('Escolha um operador: ')
operador = input()

print ('Digite outro número: ')
num2 = int(input())

if operador == '+' :
    resultado = num + num2
    print ('Calculando.... ') 
    print (90 * '=')
    print ('O resultado final foi' , resultado)

elif operador == '-' :
    resultado = num - num2
    print ('Calculando.... ') 
    print (90 * '=')
    print ('O resultado final foi' , resultado)

elif operador == '*' :
    resultado = num * num2
    print ('Calculando.... ') 
    print (90 * '=')
    print ('O resultado final foi' , resultado)

elif operador == '/' :
    resultado = num / num2
    print ('Calculando.... ') 
    print (90 * '=')
    print ('O resultado final foi' , resultado)

else:
    print ('Operador inválido! ')
