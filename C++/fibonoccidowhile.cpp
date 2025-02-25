#include <iostream>
using namespace std;

int main() {
    int num;
    int start_item = 0;
    int next_item = 1;

    cout << "Enter the number: ";
    cin >> num;

    int i = 0;

    do {
        cout << start_item << " ";
        int temp = next_item;
        next_item = start_item + next_item;
        start_item = temp;
        i++;
    } while (i <= num);

    return 0;
}