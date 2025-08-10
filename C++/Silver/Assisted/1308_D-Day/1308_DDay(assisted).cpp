/*
error:  error in withdrawing information and adjusting date for calculations - fixed
        1000y setting was excluded - included
            conditiions weren't properly met -> fixed
        skip year doesn't properly count when considering the d year and c year

ex:
1.
2008 12 27
2009 1 22

Expected : D-26

2.
2000 01 01
3001 01 01

Expected : gg

3.
2013 2 28
2013 3 1

Received : D-1

4.
2013 12 31
2014 01 01

Expected : D-1

5.
399 3 3
1399 3 3

Expected : gg

6.
1 1 1
1001 1 1

Expected : gg

7.
2008 12 27
3008 6 5

Expected : D-365037

8.
399 3 1
1399 2 28

Expected : D-365242

9.
1999 1 1
2001 1 1
Expected : 731

*/

#include <iostream>
using namespace std;

bool isLeapYear(int year) { // 윤년 확인 함수
    return (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
}

int daysInMonth(int month, int year) {  //월에 있는 일수 계산기
    int daysPerMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (month == 2 && isLeapYear(year)) return 29;  //윤년이면 +1일
    return daysPerMonth[month - 1];
}

int calculateDays(int start[], int end[]) {     //일수 계산기
    int days = 0;
    while (!(start[0] == end[0] && start[1] == end[1] && start[2] == end[2])) {
        days++;
        start[2]++;
        if (start[2] > daysInMonth(start[1], start[0])) {
            start[2] = 1;
            start[1]++;
            if (start[1] > 12) {
                start[1] = 1;
                start[0]++;
            }
        }
    }
    return days;
}

int main() {
    int C_Date[3], D_Date[3];
    cin >> C_Date[0] >> C_Date[1] >> C_Date[2];
    cin >> D_Date[0] >> D_Date[1] >> D_Date[2];

    if (D_Date[0] - C_Date[0] > 1000 || 
                                        (D_Date[0] - C_Date[0] == 1000 && 
                                                            ( C_Date[1] < D_Date[1] || (C_Date[1] == D_Date[1] && C_Date[2] <= D_Date[2]) ) ) ) {
        cout << "gg";
    } else {
        int days = calculateDays(C_Date, D_Date);
        cout << "D-" << days;
    }

    return 0;
}