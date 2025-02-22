#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter the num: ";
    cin >> num;

    int i = 0;
    while (i<=num) {
        if(i%2 == 0) {
            cout << i << " is a even number" << endl;
        }
        i++;
    }

    return 0;
}

