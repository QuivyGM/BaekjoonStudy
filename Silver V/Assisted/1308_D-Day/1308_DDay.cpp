/*
error:  error in withdrawing information and adjusting date for calculations - fixed
        1000y setting was excluded - included

ex:
2008 12 27
2009 1 22
26

1999 1 1
2001 1 1
731

*/

#include<iostream>
using namespace std;

void printDate(int C_Date[], int D_Date[]){
    for(int i=0; i<3; i++)
        cout << C_Date[i] << " ";
    cout << endl;
    for(int i=0; i<3; i++)
        cout << D_Date[i] << " ";
    cout << endl;
}

int main(){
    int C_Date[3], D_Date[3], days=0;
    int month[12]={ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    for(int i=0; i<3; i++){
        cin >> C_Date[i];
    }
    for(int i=0; i<3; i++)
        cin >> D_Date[i];

    if (D_Date[0] - C_Date[0] > 1000 || 
                                        (D_Date[0] - C_Date[0] == 1000 && 
                                                            ( C_Date[1] < D_Date[1] || (C_Date[1] == D_Date[1] && C_Date[2] <= D_Date[2]) ) ) ) {
        cout << "gg";
    } else {
        // 일 계산
        if( C_Date[1] == D_Date[1] && C_Date[2] <= D_Date[2] )                                // 같은 달이 아니면
            days += D_Date[2] - C_Date[2];
        else{
            days += ( month[C_Date[1]-1] - C_Date[2] ) + D_Date[2];
            C_Date[1]++;
        }
        if(C_Date[1]>12)
            C_Date[1]=1, C_Date[0]++;
            
        // cout << "일 계산: " << days << endl;
        // printDate( C_Date, D_Date);


        // 월 계산
        if( C_Date[1] > D_Date[1] ){            // 미래 < 현재
            for(int i=C_Date[1]-1; i<12; i++)
                days += month[i];
            for(int i=0; i<D_Date[1]; i++)
                days += month[i];
        }
        else{                                   // 현재 < 미래
            for(int i=C_Date[1]-1; i<D_Date[1]-1; i++){
                days += month[i];
                //cout << i+1 << ": " << month[i]<< endl;
            }
        }

        // cout << "월 계산: " << days << endl;
        // printDate( C_Date, D_Date);

        // 년 계산 - 년 마다 365일 더하기, 윤년있으면 +1
        days += 365 * (D_Date[0]-C_Date[0]);
        // 윤년 계산기
        for(int i=C_Date[0]; i<D_Date[0]; i++)
            if( i%4==0 && ( i%100 != 0 || i%400 == 0 ) )    // 4로 나눠진다. 그러나 100으로 나눠지지 않으면서 400으로 나눠지면
                days++;
            
        if( (D_Date[0]%4==0 && ( D_Date[0]%100 != 0 || D_Date[0]%400 == 0 ) ) && D_Date[1]>=2 )
            days++;
        if( (C_Date[0]%4==0 && ( C_Date[0]%100 != 0 || C_Date[0]%400 == 0 ) ) && (C_Date[1]-1)<= 2 )
            days++;

        // cout << "년 계산: " << days << endl;
        // printDate( C_Date, D_Date);
        
        cout << "D-" << days;
    }
}