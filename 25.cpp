#include <iostream>

using namespace std;

int main() {
    long x, y, c, z = 1, t = 1;
    cin >> x >> y;
    while (z != x) {
        z *= 7, z %= 20201227;
        c++;
    }
    while (c--) {
        t *= y, t %= 20201227;
    }
    cout << t << endl;
}
