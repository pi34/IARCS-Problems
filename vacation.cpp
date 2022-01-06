
// This is the successful solution to this problem: https://www.codechef.com/ZCOPRAC/problems/ZCO22001.

#include <iostream>

using namespace std;

int main () {

    int n, m;
    cin >> n >> m;

    int matrix[n][m];
    int sum[n][m];

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix[i][j];
            if (i == 0 && j == 0) {
                sum[i][j] = matrix[i][j];
            } else if (i == 0) {
                sum[i][j] = matrix[i][j] + sum[i][j-1];
            } else if (j == 0) {
                sum[i][j] = matrix[i][j] + sum[i-1][j];
            } else {
                sum[i][j] = matrix[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
            };
        };
    };

    int q;
    cin >> q;

    for (int i = 0; i < q; ++i) {

        int a, b, c, d;
        cin >> a >> b >> c >> d; 

        int prod = (c-a+1) * (d-b+1);

        a = a - 1;
        b = b - 1;
        c = c - 1;
        d = d - 1;

        int sumFin = 0;

        if (a == 0 && b == 0) {
            sumFin = sum[c][d];
        } else if (a == 0) {
            sumFin = sum[c][d] - sum[c][b-1];
        } else if (b == 0) {
            sumFin = sum[c][d] - sum[a-1][d];
        } else {
            sumFin = sum[c][d] - sum[c][b-1] - sum[a-1][d] + sum[a-1][b-1];
        };
        
        if (prod == sumFin) {
            cout << 1;
        } else {
            cout << 0;
        };
        
    };

}
