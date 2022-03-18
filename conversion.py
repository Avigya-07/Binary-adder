def changeToBinary(n): #Creating a function to convert decimal into binary
    binary=""
    while n!=0:
        m=n%2
        n=int(n/2)
        binary=str(m)+binary     
    l=8-len(binary)    
    for i in range(l):
        binary="0"+binary
    return binary




