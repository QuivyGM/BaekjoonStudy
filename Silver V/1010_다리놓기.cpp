#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    // create 
    int** river = new int*[T];
    for (int i = 0; i < T; i++) {
        river[i] = new int[T];
    }
}
