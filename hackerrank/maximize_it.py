from itertools import product
K, M = map(int,input().split())
def Sq(n):
    return int(n)**2
List = []
for i in range(K):
    List.append(list(map(Sq,input().split()[1:])))
Max=0  
#print(List)
#print(product(*List))  
for T in product(*List):
    #print(T)
    Sum=sum(T)%M
    if Sum>Max:   #finding maximum sum out of all tuples
        Max=Sum
print(Max)
