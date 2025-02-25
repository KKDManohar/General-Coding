#include <iostream>
using namespace std;

void greet(string name){
    cout << "my name is " << name << endl; 
}

int main() {
    string name = " ";
    cout << "Enter your name: ";
    cin >> name;

    greet(name);

    return 0;
}