a,m,n=map(int,input().split())
A=[1];B=[1]
for i in range(1,a+1):
    A+=[sum(A[max(i-m,0):])]
    B+=[sum(B[max(i-n+1,0):])]
print((A[-1]-B[-1])%(10**9+7))