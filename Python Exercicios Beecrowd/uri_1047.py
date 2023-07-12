
h_i, m_i, h_f, m_f = map(int, input().split())

m_i += h_i * 60
m_f += h_f * 60
m_t = abs(m_i - m_f)

h = m_t // 60
m = m_t % 60

if h_i == h_f:
    h += 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))






