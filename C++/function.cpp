#include <iostream>
using namespace std;

int add(int a,int b){
    return a + b;
}

int main() {
    int num1,num2;

    cout << "enter the value of num1";
    cin >> num1;
    cout << "enter the value of num2";

    int sum = add(num1,num2);

    cout << "Sum: " << sum << endl;

    return 0;
}