#include <iostream>
using namespace std;

int main() {

    int num;
    bool isPrime = true;

    cout << "Enter the number :";
    cin >> num;

    if (num <= 1) {
        isPrime = false;
    }
    else {
        for(int i = 2;i<num/2;i++){
            if(num % i == 0) {
                isPrime = false;
            }
        }
    }

    if(isPrime) {
        cout << "the number is prime" << endl;
    }
    else {
        cout << "the number is not prime" << endl;
    }

}