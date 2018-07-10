N,K=int(raw_input()),int(raw_input())
a=[]
c=0
for i in range(N):
	x=int(input())
	a.insert(i,x)
for j in range(K):
	c=c+a[j]
print (c)
