#include <iostream>
using namespace std;

int main() {
    int num;

    cout << "Enter the num: ";
    cin >> num;
    double sum = 0.0;

    int i = 1;
    while(i<=num) {
        sum +=  (double) (1.0/i);
        i++;
        //cout << sum << endl;
    }

    cout << sum << endl;
    return 0;
}