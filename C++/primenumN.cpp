//printing of all prime numbers form 1 to 100

#include <iostream>
using namespace std;

int main() {
    int num;
    int count;
    bool isPrime;
    cout << "Enter the first N numbers: ";
    cin >> num;

    for(int i = 1; i <= num; i++) {
        count = 0;
        if(i <= 1){
            isPrime = false;
            continue;
        }
        else {
            for(int j = 1;j <= i;j++){
                if(i%j == 0) {
                    count++;
                }
            }
        }
        if (count == 2) {
            cout << i << " ";
        }
    }

    return 0;
}