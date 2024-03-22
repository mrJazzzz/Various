import math

# ispitati je li trocifren broj ABC ima svojstvo (ABn)^2-C^2=ABCn
"""
a = int(input("Unesi trocifren broj: "))
b = (a // 10)**2-(a % 10)**2
if b == a:
    print("Dobaar")
else:
    print("Nema svojstvo")
"""

# neka kod izbaci binaran broj napisan u drugom komplementu za zadat broj bitova
# dakle unosim binarnu predstavu
"""
n = int(input("Unesi broj bitova: "))
br = (input("Unesi binarnu predstavu: "))
if len(br) == n:
    rez = -(2**n - int(br, 2))
else:
    rez = int(br, 2)

print(rez)
"""

# konvertuj unetu temperaturu (degF, K, degR) u celzijuse
"""
temp = input("Unesi temperaturu : ")
c = temp[-1]
tempvr = float(temp[0:-1])
if c == 'F':
    tempvr -= 32
    tempvr *= 5/9
elif c == 'K':
    tempvr -= 273.15
else:
    tempvr -= 491.67
    tempvr *= 5/9

print("{0} --> {1:.2f} degC" .format(temp, tempvr))
"""

# skalarni i vektorski proizvod dva vektora
"""
p = input("p: ").split(", ")
q = input("q: ").split(", ")
v = []
for i in range(0, len(p)):
    s += (float(p[i]) * float(q[i]))
    v.append(float(p[(i+1) % 3]) * float(q[(i+2) % 3]) - float(p[(i+2) % 3]) * float(q[(i+1) % 3]))
print("p: {0}\nq: {1}\ns: {2}\nv: {3}".format(p, q, s, v))
"""

#najduzi striktno rastuci podniz
"""
niz = input("niz: ").split()
max_duz = tr_duz = 1
max_ind = tr_ind = 0

for i in range(1, len(niz)):
        if float(niz[i]) > float(niz[i-1]):
            tr_duz += 1
        else:
            if tr_duz > max_duz:
                max_duz = tr_duz
                max_ind = tr_ind
            tr_duz = 1
            tr_ind = i
if tr_duz > max_duz:
    max_duz = tr_duz
    max_ind = tr_ind

podniz = []
for i in range(max_ind, max_ind+max_duz):
    podniz.append(float(niz[i]))

print("podniz: {}".format(podniz))
"""

#tabeliranje polinoma
"""
deg = int(input("Stepen polinoma: "))
koef = []
for i in range(0, deg+1):
    a = int(input())
    koef.append(a)
Pol = ""

for i in range(0, deg+1):
    if koef[i] == 0:
        continue
    if koef[i] > 0 & i > 0:
        Pol += " + "
    if koef[i] < 0:
        Pol += " - "
    if (abs(koef[i]) != 1 & i != deg) | i == deg:
        Pol += str(abs(koef[i]))
    if i < deg:
        Pol += "x"
        if i < deg-1:
            Pol += "^"+str(deg-i)
print(Pol)
xmin = float(input("minimum: "))
xmax = float(input("maksimum: "))
dx = float(input("korak: "))

x = xmin
while x < xmax:
    P = 0
    for i in range(0, deg+1):
        P += koef[i]*x**(deg-i)
    print("P({0}) = {1}".format(x, P))
    x += dx
"""

n = []
for i in range(2):
    p = (input()).split(", ")
    n.append(p)

q = input()

r = (input()).split(", ")

s = input()

print(n,q,r,s, sep = "  ")















