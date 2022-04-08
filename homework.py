leng = 0
i = 0
big = 0

T = [4,5,6,7,8,9,10,5,3,4,8,9,4,5,6,7,1,2,3,5,4,7,8]
print(T)
limit = len(T)
L = []

T.append(0)
while(i < limit ):
    if abs(T[i+1]) - abs(T[i]) == 1 :
        leng += 1
    else:
        L.append(leng)
        leng = 0
    i += 1
T.pop(len(T)-1)

max = L[0];    
i = 0      
for i in range(0, len(L)):       
   if(L[i] > max):   
       max = L[i];  

pos = L.index(max)
M = L[0:pos]
N = L[0:pos+1]
sumM = sum(M) + len(M)
sumN = sum(N) + len(N)
Tinv = T[sumM:sumN]
Tinv2 = Tinv[::-1]

T[sumM:sumN] = Tinv2
print(T)
