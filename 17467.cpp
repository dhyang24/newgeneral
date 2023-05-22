#pragma GCC optimize("O3")
#pragma GCC target ("avx2")
#pragma GCC optimize ("lzcnt,popcnt,bmi2,bmi,abm,fma")
#include <iostream>
alignas(32)int st[8]{1,1,1,1,1,1,1,1};
using namespace std;
int main(void){
    int n,p;
    cin >> n >> p;
    int no = n-n%8;
    for(int i=1; i<=no; i+=8)for(int k=0; k<8; k++)st[k] = (long long)st[k]*(i+k)%p;
    int ans = 1;
    for(int i=no+1; i<=n; i++)ans = (long long)ans*i%p;
    for(int i=0; i<8; i++)ans = (long long)ans*st[i]%p;
    cout << ans << '\n';
}