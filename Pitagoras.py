
print ("Existe solo una tripleta de Pitagoras para la cual a + b + c = 1000")
print ("Cual es el producto de abc")

for a in range(1, 1000):  #Empezamos la secuencia donde a esta entre 1 - 1000
    for b in range(a, 1000):  # sabemos que b es mayor que a (a<b<c)
        c = 1000 - a - b    #Restamos a y b a 1000 para encontrar c
        if c > 5: # sabemos que c es mayor que a (a<b<c)
            if a ** 2 + b ** 2 == c ** 2:   #Validamos que cumpla el teorema de pitagoras
                pitagoras = a*b*c

                print ("a es:",a, "  b es:",b, "  c es:",c, "a+b+c=1000")
                print ("El producto de abc es:", pitagoras)
