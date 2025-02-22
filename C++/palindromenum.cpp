#include <iostream>
using namespace std;

int main() {
    int num;
    int reverseNum;
    cout << "Enter the number: ";
    cin >> num;
    int originalNum = num;

    while (num > 0) {
        int temp = num % 10;
        reverseNum = reverseNum * 10 + temp;
        num  = num / 10;
    }

    if(originalNum == reverseNum) {
        cout << reverseNum << "the given num is palindrome" << endl;
    }
    else {
        cout << reverseNum << "the given num is not palindrome" << endl;
    }
}