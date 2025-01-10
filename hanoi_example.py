def hanoi(n, from_rod,to_rod,aux_rod):
    global steps
    if (n == 0):
        return
    else:
    hanoi(n-1,from_rod, aux_rod, to_rod)
    from_rod.remove("size-"+ str(i))
    to_rod.insert(0,"size-"+ str(i))
    print("A: ",A,"B: ",B,"C: ",C)
    steps = steps + 1
    hanoi(n-1,aux_rod,to_rod,from_rod)
      
n=3
A=[]
B=[]
C=[]
steps=1
for i in range(1, n+1):
    A.append("size-"+str(i))
print(A)
print(B)
hanoi(n,A,B,C)

