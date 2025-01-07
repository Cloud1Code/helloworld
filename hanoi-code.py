# This pseudocode solves the Hanoi destwers problem
# It moves n disks from the 'source' to  'dest' , using the 'aux'  as an auxiliary
def hanoi(n, source, dest, aux):
    if n == 1:
        # If there is only one disk, simply move it from the 'source'  to the 'dest' 
        print(f"Move disk 1 from", source, "to", dest)
    else:
        # Recursively move the top n-1 disks from the 'source'  to the 'aux' 
        hanoi(n - 1, source, aux, dest)
        # Move the remaining disk (the largest one) from the 'source'  to the 'dest' 
        print(f"Move disk", n,"from", source, "to",dest)
        # Recursively move the n-1 disks from the 'aux'  to the 'dest' 
        hanoi(n - 1, aux, dest, source)

# Main program
n = 3 #number of discs
source = 'A'
dest = 'C'
aux = 'B'
hanoi(n, source, dest, aux)