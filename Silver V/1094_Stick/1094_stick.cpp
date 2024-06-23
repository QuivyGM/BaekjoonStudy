//error: when using recursion remember to provide return value for all options otherwise illegal instructions will occur

#include<iostream>
using namespace std;

int count=1;
int cut(int x, int stick){
    
    if(stick == x)      // 자른 길이가 x이랑 같다 -> 반환
        return count;
    else if(stick > x)  // 자른 길이가 x보다 작다 -> 막대 갯수 + 1
        stick/=2;
    else{               // 자른 길이가 x보다 크다 -> 막대 길이 / 2
        count++;
        x-=stick;
    }
    return cut(x, stick);
}

int main(){
    int X;
    cin >> X;

    cout << cut(X, 64);
}

// 32 16