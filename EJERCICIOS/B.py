def esprimo(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
Preg = []
k = 0

for i in range(2, n+1):
    if (n % i) == 0 and esprimo(i):
        Preg.append(int(n/i))
        k += 1
print(k)
for p in Preg:
    print("1 ", p)
