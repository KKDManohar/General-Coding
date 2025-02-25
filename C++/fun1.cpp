#include <iostream>
using namespace std;


    int add (int a , int b){
        return a + b;
    }

    int main() {
        int a,b,sum;
        cout << "Enter the value of a";
        cin >> a;
        cout << "Enter the value of b";
        cin >> b;

        sum = add(a,b);
        cout << sum << endl;
        return 0;
    }