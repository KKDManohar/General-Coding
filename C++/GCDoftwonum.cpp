#include <iostream>
using namespace std;

int main() {
    int num1;
    int num2;

    cout << "enter the numbers: ";

    cin >> num1;
    cin >> num2;
    
    if(num1 > num2) {
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }

    int GCD1 = 0;
    int i = 1;
    int j = 1; 
    while (i<=num1 && j<=num2) {
        if(num1%i == 0 && num2%j==0) {
            if(i <= j) {
                GCD1 = i;
            }
            else {
                GCD1 = GCD1;
            }
        }
        i++;
        j++;
    }


    cout << GCD1 << endl;

    return 0;
}