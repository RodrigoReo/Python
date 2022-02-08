linha1 = input().split()
t = int(linha1[0])
linha2 = input().split()
vm = int(linha2[0])
d  = vm *t
ql = d/12
print('{:.3f}'.format(ql))