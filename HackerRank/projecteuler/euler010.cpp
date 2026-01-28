// https://www.hackerrank.com/contests/projecteuler/challenges/euler010/
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MAXN = 2e6 + 10;

bitset<MAXN> primes;
ll ft[MAXN];

void update(int i, int n) {
  while (i < MAXN) {
    ft[i] += n;
    i += i & (-i);
  }
}

ll search(int i) {
  ll cont = 0;
  while (i) {
    cont += ft[i];
    i -= i & (-i);
  }
  return cont;
}

int main() {
  primes.set();
  primes.reset(0);
  primes.reset(1);
  for (int i = 2; i < MAXN; ++i) {
    if (primes.test(i)) {
      update(i, i);
    }
    for (int j = i * 2; j < MAXN; j += i) {
      primes.reset(j);
    }
  }
  int T, N;
  cin >> T;
  while (T--) {
    cin >> N;
    cout << search(N) << "\n";
  }
}
