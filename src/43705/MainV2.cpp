/* 43705 */
#include <iostream>
using namespace std;

const int MOD = 1000000007;
// `OPP[a]` is `b` means the opposite side of face `a` is face `b`.
const int OPP[] = { 3, 4, 5, 0, 1, 2 };

/* Fast power for integer. */
long long pow(long long a, long long b, int mod) {
    long long res = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            res = (res * a) % mod;
        }
        a = (a * a) % mod;
        b >>= 1;
    }
    return res;
}

/* Multiplication for 6x6 2D matrices. */
void matrix_multiply(long long A[6][6], long long B[6][6], long long result[6][6]) {
    long long rst[6][6] = {};
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            rst[i][j] = 0;
            for (int k = 0; k < 6; ++k) {
                rst[i][j] = (rst[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            result[i][j] = rst[i][j];
        }
    }
}

/* Fast power for 6x6 2D matrix. */
void matrix_power(long long T[6][6], int exp, long long result[6][6]) {
    long long rst[6][6] = {};
    for (int i = 0; i < 6; ++i) {
        rst[i][i] = 1; // Identity matrix
    }
    while (exp > 0) {
        if (exp % 2 == 1) {
            matrix_multiply(rst, T, rst);
        }
        matrix_multiply(T, T, T);
        exp >>= 1;
    }
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            result[i][j] = rst[i][j];
        }
    }
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

    // `transitT` is the transposed long integer version of `transit`.
    long long transitT[6][6] = {};
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            if (transit[j][i]) {
                transitT[i][j] = 1;
            }
        }
    }

    // `transitT` power `n - 1`.
    long long transitTPowered[6][6];
    matrix_power(transitT, n - 1, transitTPowered);

    long long init[6] = { 1, 1, 1, 1, 1, 1 };
    long long final[6] = {};

    // Calculate `init` multiply by `transitTPowered`.
    for (int i = 0; i < 6; ++i) {
        final[i] = 0;
        for (int j = 0; j < 6; ++j) {
            final[i] = (final[i] + transitTPowered[i][j] * init[j]) % MOD;
        }
    }

    // Accumulate the result.
    long long rst = 0;
    for (int i = 0; i < 6; ++i) {
        rst = (rst + final[i]) % MOD;
    }

    // Multiply by `4^n` because the dice can be rotated by 90 degrees for 4 times.
    rst = (rst * pow(4, n, MOD)) % MOD;
    cout << rst << endl;

    return 0;
}
