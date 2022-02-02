import  math
def pereb(proper):
    global q
    i1=0
    for i in range(len(proper) -1,-1,-1):
        if proper[i]>proper[i-1] and i-1!=-1:
            i1=i-1
            break
    else:
        q=1
        return
    for i in range(len(proper) - 1, -1, -1):
        if proper[i1]<proper[i]:
            proper[i1],proper[i]=proper[i],proper[i1]
            break
    proper[i1+1:]=sorted(proper[i1+1:])
n,g=map(int,input().split())
q=0
k=[]
c=0
l=0
for i in range(n):
    k.append(i+1)
while q!=1:
    for i in range(len(k)-1):
        for j in range(i+1,len(k)):
            if abs((i+1)-(j+1))==abs(k[i]-k[j]):
                c+=1
                break
        if c>0:
            break
    if c==0 :
        l+=1
        if l==g:
            break
    c=0
    pereb(k)
for i in range(len(k)-1):
    print('Q'+chr(i+97)+str(k[i]),end=' ')
print('Q'+chr(n+96)+str(k[-1]))
#Перед вами стоит шахматная доска размера n×n.Назовем расстановку n ферзей на этой доске правильной, если никакие два ферзя не бьют друг друга.
#Очевидно, что правильных расстановок может быть несколько.
#Упорядочим правильные расстановки в лексикографическом порядке, где старшим разрядом будет столбец "a а младшим столбец "h".
#Например, расстановка (Qa1, Qb5, Qc8, Qd6, Qe3, Qf7, Qg2, Qh4) будет меньше расстановки (Qa1, Qb6, Qc8, Qd3, Qe7, Qf4, Qg2, Qh5).
#Выведите k-ю по счету правильную расстановку ферзей на заданной доске в формате шахматной нотации. Нумерация перестановок начинается единицы.