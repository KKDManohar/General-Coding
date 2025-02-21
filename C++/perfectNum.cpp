#include <iostream>
using namespace std;

int main() {
    int num;
    int sum = 0;
    cout << "Enter the num to check it is perfect or not: ";
    cin >> num;

    for(int i = 1;i<=num/2;i++){
        if(num%i==0){
            sum += i;
        } 
    }

    if(sum == num){
        cout << "The num is perfect num" << endl;
    }
    else{
        cout << "The num is not perfect num" << endl;
    }

    return 0;
}