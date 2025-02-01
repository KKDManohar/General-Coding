#include <iostream>
#include <array>
using namespace std;

int main() {
   // int numbers[5] = {10,20,30,40,50};
    std::array<int,5>  numbers = {10,20,30,40,50};

    for(int i = 0;i < numbers.size();i++){
        cout << "Elements in an array" << i << numbers[i] << endl;
    }

    return 0;
}