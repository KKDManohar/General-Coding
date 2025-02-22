#include <iostream>
using namespace std;

int main() {
    int num;
    int factorial = 1;
    cout << "Enter the number: ";
    cin >> num;

    int i = 1;
    while (i <= num) {
        factorial *= i;
        i++;
    }

    cout << factorial << endl;

    return 0;
}