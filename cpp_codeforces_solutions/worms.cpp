#include <iostream>
#include <bits/stdc++.h>
typedef long long ll;
typedef long double ld;
using namespace std;

void solve()
{
	ll n;
	cin >> n;
	vector<ll>v(n);
	ll ind = 1, sum = 0;
	for (ll i = 0; i < n; i++){
		ll a;
		cin >> a; 
		sum += a;
		ind += a;
		v[i] = sum;
		}
		ll q;
		cin >> q;
		while (q--)
		{
			ll a;
			cin >> a;
			ll num = upper_bound(v.begin(), v.end(), a) - v.begin();
			if (v[num - 1] != a) num++;
			cout << num << "\n";
			}
	}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll t;
	t = 1;
	while (t--)
	{
		solve();
	}
	return 0;
}
	
