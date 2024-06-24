#include<iostream>
using namespace std;

int main(){
    
    int N=1;
    cin >> N;

    for(int i=1; ; i++){
        if(N<=i){                           // N
            if(i%2==1)
                N = i-N+1;                  // N = i - N + 1;
            cout << N << "/" << i-N+1;      // (N만큼 큰수) / (i 에서 N을 뺀 수 + 1)
            break;
        }
        else
            N-=i;
    }    
}