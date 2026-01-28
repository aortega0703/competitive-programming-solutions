#include <bits/stdc++.h>

using namespace std;

vector<int> pals;
bool isPal(string n) {
  for (int i = 0; i < n.size() / 2; ++i) {
    if (n[i] != n[n.size() - i - 1])
      return false;
  }
  return true;
}

void maxPal() {
  for (int i = 999; i >= 100; --i) {
    for (int j = 999; j >= 100; --j) {
      if (isPal(to_string(i * j))) {
        pals.push_back(i * j);
      }
    }
  }
}

int binaryS(int n) {
  int l = 0;
  int r = pals.size() - 1;
  while (l < r) {
    if (pals[(l + r) / 2] < n) {
      l = (l + r) / 2 + 1;
    } else {
      r = (l + r) / 2 - 1;
    }
  }
  if (pals[l] >= n)
    return pals[l - 1];
  return pals[l];
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t, n;
  maxPal();
  sort(pals.begin(), pals.end());
  cin >> t;
  while (t--) {
    cin >> n;
    cout << binaryS(n) << "\n";
  }
}
