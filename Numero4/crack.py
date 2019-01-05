import sys

e = int(sys.argv[1])
n = int(sys.argv[2])

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

f = factors(n)
f.remove(1)
f.remove(n)

p, q = list(f)
d = modinv(e, (p - 1) * (q - 1))

print 'p = %d, q = %d, d = %d' % (p, q, d)
