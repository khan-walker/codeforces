#include<bits/stdc++.h>

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define sz(z) (int)(x).size()
#define rep(i, a, b) for (int i = (a); i < (b); i++)
#define rep1(a) for(int i = 0; i < (a); i++)
#define debug(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

const int MOD = 1e9 + 7;
const int MAXN = 100005;

void yes() {
	cout << "YES" << "\n";
	}
	
void no() {
	cout << "NO" << "\n";
}


void solve() 
{
	ll n;
	cin >> n;
	vector<ll> dp((int) 1e5 + 1, 0);
	rep(i, 0, n)
	{
		int x; 
		cin >> x;
		dp[x] ++;
		}
	for (ll i = 2; i <= (int)1e5; i++)
	{
		dp[i] = max(dp[i - 1], dp[i - 2] + dp[i] * i *1LL);
		
		}
		cout << dp[(int)1e5]<<endl;
	}
	
int main() 
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	solve();
	return (0-0);
	
	
	
	}
