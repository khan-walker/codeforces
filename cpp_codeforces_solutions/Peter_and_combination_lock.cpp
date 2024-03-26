#include <iostream>
using namespace std;
int n,i,j,s,a[20];
int main(){
	for(cin>>n;i<n;i++)cin>>a[i];
	for(i=0;i<2<<15;i++){
		for(j=s=0;j<15;j++)s+=i&(1<<j)?+a[j]:-a[j];
		if(s%360==0)return cout<<"YES",0;
	}
	cout<<"NO";
}
