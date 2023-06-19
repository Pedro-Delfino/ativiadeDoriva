vetorPossibilidade = [True, False]

quant = int(input('Digite se a quantidade de variáveis é 2 ou 3: '))
formula = input('Digite a Fórmula: ')

linhas = 0
verdade = 0
mentira = 0
lista1 = []
lista2 = []

if quant == 2:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            if eval(formula):
                lista1.append(True)
                resultadoF = True
                verdade += 1
            else:
                lista1.append(False)
                resultadoF = False
                mentira += 1
            
            print(f'A={a} \t B={b} \t H={resultadoF}')
            linhas += 1
            
    print(f'Total de linhas com resultado VERDADEIRO: {verdade}')
    print(f'Total de linhas com resultado FALSO: {mentira}')
    print(f'Total de linhas da tabela: {linhas}')
    
    if mentira == 0:
        print('Essa fórmula é TAUTOLOGICA.')
    elif verdade == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')

if quant == 3:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                if eval(formula):
                    lista1.append(False)
                    resultadoF = True
                    verdade += 1
                else:
                    lista1.append(False)
                    resultadoF = False
                    mentira += 1
                print(f'A={a} \t B={b} \t C={c} H={resultadoF}')
                linhas += 1

    print(f'Total de linhas com resultado VERDADEIRO: {verdade}')
    print(f'Total de linhas com resultado FALSO: {mentira}')
    print(f'Total de linhas da tabela: {linhas}')
                
    if mentira == 0:
        print('Essa fórmula é TAUTOLOGICA.')
    elif verdade == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')
    
linhas = 0 
verdade = 0
mentira = 0

formula = input('Digite uma fórmula: ')

if quant == 2:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            if eval(formula):
                lista2.append(True)
                resultadoF = True
                verdade += 1
            else:
                lista2.append(False)
                resultadoF = False
                mentira += 1
                
            print(f'A={a} \t B={b} \t C={c} H={resultadoF}')
            linhas += 1
            
    print(f'Total de linhas com resultado VERDADEIRO: {verdade}')
    print(f'Total de linhas com resultado FALSO: {mentira}')
    print(f'Total de linhas da tabela: {linhas}')
    
    if mentira == 0:
        print('Essa fórmula é TAUTOLOGICA.')
    elif verdade == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')
        
if quant == 3:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                if eval(formula):
                    lista2.append(True)
                    resultadoF = True
                    verdade += 1
                else:
                    lista2.append(False)
                    resultadoF = False
                    mentira += 1
                
                print(f'A={a} \t B={b} \t C={c} H={resultadoF}')
                linhas += 1
                
    print(f'Total de linhas com resultado VERDADEIRO: {verdade}')
    print(f'Total de linhas com resultado FALSO: {mentira}')
    print(f'Total de linhas da tabela: {linhas}')
        
    if mentira == 0:
        print('Essa fórmula é TAUTOLOGICA.')
    elif verdade == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')
            
if lista1 == lista2:
    print('As fórmulas são EQUIVALENTES.')
else:
    print('As fórmulas são DIFERENTES.')