# This solves the Tower of Hanoi  problem
# It moves n disks from the 'source' to  'dest' , using the 'aux'  as an auxiliary
def hanoi(i, source, dest, aux):
    global steps
    if (i == 0):
        return
    # Move the remaining disk (the largest one) from the 'source'  to the 'dest' 
    hanoi(i-1, source, aux, dest)
    #move current disk from source to dest
    source.remove("size" + str(i))
    dest.insert(0, "size" + str(i)) #insert *ON TOP* of other discs
    #show rod states
    print(steps, "A:", a, "B:", b, "C:", c)
    steps = steps + 1
    # Recursively move the top n-1 disks from the 'source'  to the 'aux' 
    hanoi(i - 1, aux, dest, source)


# Main program
n = 6 #number of discs
#rods A, B, C
a = []
b = []
c = []
steps = 1
for i in range(1, n+1):
    a.append("size" + str(i))
print("Source = ", a)
hanoi(n, a, c, b)
print("Dest = ", c)
#n=if only one disc move to destination.
#n-1=move (n-1)from source to auxilaryy keeping dest as holding position.
#n-1=move (n-1)from aux to destination by keeping source as holding position.