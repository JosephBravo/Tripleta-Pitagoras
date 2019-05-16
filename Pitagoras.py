print ("Existe solo una tripleta de Pitagoras para la cual a + b + c = 1000")
print ("Cual es el producto de abc")


def Pitagoras(a, b, c):
    if not (a < b and b < c):
        return False
    return a ** 2 + b ** 2 == c ** 2

universo = [x for x in range(1, 1000)]

for a in universo:
    for b in range(a, 1000 - a):
        for c in range(b, 1000 - b):
            if a + b + c == 1000:
                if Pitagoras(a, b, c):
                    print ("a es:",a, "  b es:",b, "  c es:",c, "a+b+c=1000")
                    print("El producto de abc es:",(a * b * c))
