#Calculando tabela de frequências
lista = ['SP', 'SP', 'RJ', 'MG', 'CE', 'PE', 'SE', 'AC', 'AC', 'BA', 'AM', 'PE', 'PE', 'PE', 'SP', 'SE', 'BA', 'AM', 'RJ', 'MG', 'CE']
print('Tabela de Frequências')
freqAbsoluta = {x:lista.count(x) for x in set(lista)}
print('Cálculo da coluna FA: ', freqAbsoluta)

#Tamanho do total da tabela de frequências
tamanho = len(lista)
print('Cálculo do tamanho: ', tamanho)

#Colocando frequência absoluta em lista - FA: NÚMERO DE OCORRÊNCIAS DO VALOR NA TABELA
FA = list(freqAbsoluta.values())
print('Coluna da FA: ', FA)

#Calculando frequência relativa - FR: CADA FA DIVIDIVO PELO TAMANHO DOS ITENS DA TABELA
FR = []
for x in FA:
	result = 0
	result = (x / tamanho)
	FR.append(result)
print('Coluna de FR: ', FR)

#Calculando porcentagem
porcentagem = []
for x in FR:
	contador = 0
	contador = (x * 100)
	porcentagem.append(contador)
print('Coluna da porcentagem: ', porcentagem)