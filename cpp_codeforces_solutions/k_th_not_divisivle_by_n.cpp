#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int have = n-1;
        int mul = k/have;
        int rem = k%have;
        int res = (n*mul) + rem;
        if(rem==0) res--;
        cout<<res<<endl;
    }
}
