
def printdots(n):
    if n > 0:
        print("." * n)
        printdots(n-1)
    
printdots(5)

def startriangle(n):
    for i in range(n, 0, -1):
        print('*' * i)
        
startriangle(5)

def triangular (n):
    return sum (range(1, n+1))
        
    
print(triangular(6))