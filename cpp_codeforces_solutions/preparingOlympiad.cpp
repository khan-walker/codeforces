#include<iostream>
using namespace std;
int n,l,r,x,j,c[20];
int f(int s,int a,int b,int i)
{
    return(i==n)?s>=l&&s<=r&&b-a>=x:f(s+c[i],min(a,c[i]),max(b,c[i]),i+1)+f(s,a,b,i+1);
    
}
main()
{cin>>n>>l>>r>>x;
while(cin>>c[j++]);
cout<<f(0,1e9,0,0);
}
