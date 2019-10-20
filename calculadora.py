print('************************ Python Calculator ************************')

print('Selecione o número da operação desejada: ')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')
selecione = int(input('Digite sua opção (1/2/3/4)'))

a = int(input('\nDigite o primeiro número: '))
b = int(input('\nDigite o segundo número: '))

soma = lambda a, b: a + b

subtrai = lambda a, b: a - b

multiplica = lambda a, b: a * b

divide = lambda a, b: a / b

if (selecione == 1):
	print('\n')
	print(a, '+', b, '=', soma(a.b))
	print('\n')
elif (selecione == 2):
	print('\n')
	print(a, '-', b, '=', subtrai(a.b))
	print('\n')
elif (selecione == 3):
	print('\n')
	print(a, '*', b, '=', multiplica(a.b))
	print('\n')
elif (selecione == 4):
	print('\n')
	print(a, '/', b, '=', divide(a.b))
	print('\n')
else:
	print('Opção inválida!')