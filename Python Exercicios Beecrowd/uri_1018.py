

s = int(input())

if 0 < s < 1000000:
    print(f'{s}')
    n = s // 100
    s = s - (n * 100)
    print(f'{n} nota(s) de R$ 100,00')
    n = s // 50
    s = s - (n * 50)
    print(f'{n} nota(s) de R$ 50,00')
    n = s // 20
    s = s - (n * 20)
    print(f'{n} nota(s) de R$ 20,00')
    n = s // 10
    s = s - (n * 10)
    print(f'{n} nota(s) de R$ 10,00')
    n = s // 5
    s = s - (n * 5)
    print(f'{n} nota(s) de R$ 5,00')
    n = s // 2
    s = s - (n * 2)
    print(f'{n} nota(s) de R$ 2,00')
    n = s // 1
    s = s - (n * 1)
    print(f'{n} nota(s) de R$ 1,00')









