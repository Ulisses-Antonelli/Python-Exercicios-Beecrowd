a, b = 7, 4
for i in range(1, 10, 2):
    for j in range(a, b, -1):
        print(f"I={i} J={j}")
    a += 2
    b += 2
