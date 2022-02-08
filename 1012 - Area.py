a,b,c = [float(x) for x in input().split()]
pi = 3.14159
triangulo = (a*c)/2
   print("TRIANGULO:",'{:.3f}'.format(triangulo))
circulo = pi * (c**2)
   print("CIRCULO:", '{:.3f}'.format(circulo))
trapezio = ((a+b)*c)/2
   print("TRAPEZIO:", '{:.3f}'.format(trapezio))
quadrado = b**2
   print("QUADRADO:",'{:.3f}'.format(quadrado))
#retangulo = a*b
   print("RETANGULO:", '{:.3f}'.format(retangulo))