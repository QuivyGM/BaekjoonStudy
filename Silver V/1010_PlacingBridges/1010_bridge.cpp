//errors:
//      (1)theoretically count *=(a/b)is possible but would need both a, b and count to be double to be able to account for the division prospects
//              ex: 7/2 would incorrectly save as 3 leading to error in all later calculations
//      solution: int -> double -> long double      +       start dividing with smaller numbers             
//      (2) if numbers are too big then overflow occurs breaking calculation
//      solution: multiplilcation and division simultaneously

#include<iostream>
using namespace std;

long long countBridges(int a, int b){
    // return = a 가 더 작다면 b에서 a개 의 장소를 선택
    // 조함 공식: N! / (N-r)! / R!
    // a > b 일수도 있을때
    // if(a>b) swap(a, b);

    //식 단순화 n.C.r = n.C.n=r
    if( b-a < a ) a = b-a;

    // If a or b is 0, the combination is 1
    if (a == 0 || b == 0) return 1;

    // calculation
    long long count=1;

    // problem: division starting with larges number causes overflow/data loss
    // for( ; a>0; a--, b--){
    //     count *= b;
    //     count /= a;
    //     //cout << endl << count << "// " << a << " " << b;      //for debugging
    // }

    for (int i = 1; i <= a; ++i, --b) {
        count = count * b / i;
        // cout << "Current count: " << count << ", i: " << i << ", b: " << b << endl; // 디버깅 출력
    }

    //cout << endl;
    return static_cast<long long>(count);
}

int main(){
    int T, a, b;
    cin >> T;

    // 만약 입력 값을 모두 저장하고 싶을때
    // int** river = new int*[T];      // declares river as pointer to an array of T int pointers
    // for (int i = 0; i < T; i++) {   // allocates a row of T ints for each river[i], forming a T x T int matrix
    //     river[i] = new int[2];
    // }
    long long* result = new long long[T];       // T sized array for result

    for(int i=0; i<T; i++){
        cin >> a >> b;  // input T times
        result[i]=countBridges(a, b);
    }

    for(int i=0; i<T; i++){
        cout << result[i] << endl;
    }

    delete[] result;
}