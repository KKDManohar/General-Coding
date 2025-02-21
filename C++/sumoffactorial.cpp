#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter the number: ";
    cin >> num;
    int result = 0;

    for(int i = 1; i <= num; i++) {
        int product = 1;
        for(int j = 1;j <= i;j++){
            product = product * j;
            cout << j << product << endl;
            cout << " " << endl;
        }
        cout << "product" << product << endl;
        cout << result << endl;
        result = result + product;

    }

    cout << result << endl;

    return 0;
}