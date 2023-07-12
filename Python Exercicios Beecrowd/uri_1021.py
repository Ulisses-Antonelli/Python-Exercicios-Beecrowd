
N = float(input('Digite as notas: '))

ced = [100, 50, 20, 10, 5, 2]
moed = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

if 0 <= N <= 1000000.00:

    print('NOTAS:')
    for qtd in ced:
        notas = int(N / qtd)
        N = N - (notas * qtd)
        print(f'{int(notas)} nota(s) de R$ {qtd:.2f}')

    print('MOEDAS:')
    for qtd in moed:
        N = round(N, 2)
        moedas = int(N / qtd)
        N = N - (moedas * qtd)
        print(f'{int(moedas)} moeda(s) de R$ {qtd:.2f}')

'''
N = float(input().replace(',', '.'))

if 0 <= N <= 1000000.00:

    ced_100 = N // 100
    N = N - (ced_100 * 100)

    ced_50 = N // 50
    N = N - (ced_50 * 50)

    ced_20 = N // 20
    N = N - (ced_20 * 20)

    ced_10 = N // 10
    N = N - (ced_10 * 10)

    ced_5 = N // 5
    N = N - (ced_5 * 5)

    ced_2 = N // 2
    N = N - (ced_2 * 2)

    moeda_1 = N // 1
    N = N - (moeda_1 * 1)

    moeda_05 = N // 0.5
    N = N - (moeda_05 * 0.5)

    moeda_025 = N // 0.25
    N = N - (moeda_025 * 0.25)

    moeda_010 = N // 0.10
    N = N - (moeda_010 * 0.10)

    moeda_005 = N // 0.05
    N = N - (moeda_005 * 0.05)

    moeda_001 = N // 0.01
    N = N - (moeda_001 * 0.01)

    print('NOTAS:')
    print(f'{int(ced_100)} nota(s) de R$ 100.00')
    print(f'{int(ced_50)} nota(s) de R$ 50.00')
    print(f'{int(ced_20)} nota(s) de R$ 20.00')
    print(f'{int(ced_10)} nota(s) de R$ 10.00')
    print(f'{int(ced_5)} nota(s) de R$ 5.00')
    print(f'{int(ced_2)} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{int(moeda_1)} moeda(s) de R$ 1.00')
    print(f'{int(moeda_05)} moeda(s) de R$ 0.50')
    print(f'{int(moeda_025)} moeda(s) de R$ 0.25')
    print(f'{int(moeda_010)} moeda(s) de R$ 0.10')
    print(f'{int(moeda_005)} moeda(s) de R$ 0.05')
    print(f'{int(moeda_001)} moeda(s) de R$ 0.01')
    
    '''
