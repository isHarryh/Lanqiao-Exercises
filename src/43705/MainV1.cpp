/* 43705 */
#include <iostream>
using namespace std;

const int MOD = 1000000007;
// `OPP[a]` is `b` means the opposite side of face `a` is face `b`.
const int OPP[] = { 3, 4, 5, 0, 1, 2 };

/* Fast power for integer. */
long long pow(long long a, long long b, int mod) {
    long long rst = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            rst = (rst * a) % mod;
        }
        a = (a * a) % mod;
        b >>= 1;
    }
    return rst;
}

int main() {
    int n, m;
    cin >> n >> m;

    int conflict[36][2] = {};
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        // Note that point 1~6 are mapped to 0~5
        conflict[i][0] = a - 1;
        conflict[i][1] = b - 1;
    }

    // `transit[a][b]` is `true` when up-face `a` can be transit to up-face `b`.
    bool transit[6][6] = {};
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            transit[i][j] = true;
        }
    }
    for (int i = 0; i < m; ++i) {
        int a = conflict[i][0];
        int b = conflict[i][1];
        transit[a][OPP[b]] = false;
        transit[b][OPP[a]] = false;
    }

    // `dp[i]` represents the number of ways to form up-face `i` on top.
    long long dp[6] = { 1, 1, 1, 1, 1, 1 };
    long long new_dp[6] = {};

    for (int _ = 1; _ < n; ++_) {
        for (int i = 0; i < 6; ++i) {
            new_dp[i] = 0;
            for (int j = 0; j < 6; ++j) {
                if (transit[j][i]) {
                    new_dp[i] = (new_dp[i] + dp[j]) % MOD;
                }
            }
        }
        for (int i = 0; i < 6; ++i) {
            dp[i] = new_dp[i];
        }
    }

    // Accumulate the result.
    long long rst = 0;
    for (int i = 0; i < 6; ++i) {
        rst = (rst + dp[i]) % MOD;
    }

    // Multiply by `4^n` because the dice can be rotated by 90 degrees for 4 times.
    rst = (rst * pow(4, n, MOD)) % MOD;
    cout << rst << endl;

    return 0;
}
