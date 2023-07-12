A, B = map(int, input().split())
for i in range(11):
    C = A * i
    if C == B:
        print('Sao Multiplos')
        if C != B:
            print('Nao sao Multiplos')
            if A == B:
                print('Sao Multiplos')


