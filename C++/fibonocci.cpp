#include <iostream>
using namespace std;

int main() {
    int start_item = 0 , present_item = 1, next_item;
    int num;
    cout << "Enter the final num: ";
    cin >> num;
    int i = 0;
    
    while (i <= num) {

        cout << start_item << " " ;

        next_item = start_item + present_item;
        start_item = present_item;
        present_item = next_item;

        i++;
    }

    return 0;
}