#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int num;
    int temp;
    int ArmstrongNum;
    cout << "Enter the num to check the Armstrong num: ";
    cin >> num;
    int originalnum = num;
    for(int i = 0;num != 0;i++){
        temp = 0;
        temp = num % 10;
        ArmstrongNum += pow(temp,3);
        num = num / 10;
    }

    if(ArmstrongNum == originalnum) {
        cout << "The num is Armstring num" << ArmstrongNum << endl;
    }
    else {
        cout << "The num is not Armstring num"<< ArmstrongNum << endl;
    }

    return 0;
}
