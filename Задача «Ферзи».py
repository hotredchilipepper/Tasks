a = []
b = []
z = 0
for i in range(8):
    x,y = [int(s) for s in input().split()]
    a.append(x)
    b.append(y)
    
for j in range(len(a)):
    for t in range(1 + j, len(a)):
        if a[j] == a[t] or b[j] == b[t] or abs(a[j]-a[t]) == abs(b[j]-b[t]):
            z +=1
            break
        
if z == 0:
    print('NO')
else:
    print('YES')
 
 # Задача состоит в том чтобы проверить могут ли стоять 8 ферзей на шахматной доске чтобы не били друг друга.