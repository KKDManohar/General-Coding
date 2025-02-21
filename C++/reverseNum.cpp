#include <iostream>
using namespace std;

int main() {
    int num;
    int reverseNum;

    cout << "Enter the num: ";
    cin >> num;

    while(num > 0) {
        int temp = num % 10;
        reverseNum = reverseNum * 10 + temp;
        num = num / 10;
    }

    cout << reverseNum << endl;

    return 0;
}