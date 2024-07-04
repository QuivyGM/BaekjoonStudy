#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;

    //정보를 저장할 변수
    int *board[5];
    for(int i=0; i<5; i++)
        board[i] = new int[N];
    // 학생 점수를 저장할 곳
    
    int **score = new int*[N];
    for(int i=0; i<N; i++)
        score[i] = new int[N];

    // wrong user case
    // int **score = new int[N];
    // for(int i=0; i<N; i++)
    //     int *score[i] = new int[N];

    //[][] 학년, 학생
    for(int i=0; i<N; i++)
        for(int j=0; j<5; j++)
            cin >> board[j][i];
    
    //학년별로 시행
    for(int i=0; i<5; i++){     //학년별로 시행
        for(int j=0; j<N; j++){     //모든 학생 새힝
            for(int a=j; a<N; a++)
                if(board[i][j]==board[i][a]){
                    score[j][a]=1;
                    score[a][j]=1;
                }
        }
    }
    
    // use max_element to simplify calculating the max amount in the array 
    int president[2]={0, 0};
    int temp=0;
    for(int i=0; i<N; i++){
        temp=0;
        for(int j=0; j<N; j++)
            temp +=score[i][j];
        if(temp > president[1]){
            president[0]=i;
            president[1]=temp;
        }
    }
    cout << president[0];
}