#include<bits/stdc++.h>
using namespace std;
long long n,m,a;
int main()
{
for(cin>>n; cin>>n>>m; cout<<a<<' ')
{
vector<int>v1(m),v2(m);
for(;n--;++v1[--a])
cin>>a;
for(int&c:v2)
cin>>c;
for(a=0;m--;)
for(;v1[m]--;)
a+=v2[min(m,++n)];
}
return 0;
}

