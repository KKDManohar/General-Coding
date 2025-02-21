#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter the number: ";
    cin >> num;
    int sum = 0;

    while(num > 0){
        int temp = num % 10;
        sum += temp;
        num = num / 10;
    }

    cout << sum << endl;

    return 0;
}