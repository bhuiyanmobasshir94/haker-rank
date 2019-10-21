#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
  int n;
    cin >> n;

    int arr[n][n];

    long long int d1=0; //First Diagonal
    long long int d2=0; //Second Diagonal

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            if (i == j) d1 += arr[i][j];
            if (i == n - j - 1) d2 += arr[i][j];
        }
    }

    cout << abs(d1 - d2) << endl; //Absolute difference of the sums across the diagonals
   
    return 0;
}
