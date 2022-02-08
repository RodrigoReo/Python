import math
linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
MaiorAB = (a+b+abs(a-b))/2
if MaiorAB < c:
    print(c,'eh o maior')
elif a > b:
    print(a,'eh o maior')
else :
    print(b,'eh o maior')