/*
주어진 단어 쪼개기 -> 쪼개는 기준: 가장 빠른 알파벳 구하기 - 1번 쪼개기: 최소 단어 두개 놔두기, 2번 쪼개기: 최소 단어 한개 나누기

error:  strlen != position
            -> entirety of word must be taken into account  ->  word.substr() & word[newpivot]>=word[i]
        string initialization needs to be done! 
            -> when want to empty string used ="" instead of {} or NUll
*/

#include<iostream>
using namespace std;
int split(string &word, int start, int end, int round=0){

    int newpivot=start;
    string temp1, temp2;
    if(round==0){           //find new pivot and swap to end
        temp2=word.substr(start, end);
        for(int i=start; i<=end; i++){
            //cout << i << ": " << word[newpivot] << " " << word[i] << endl;
            if(word[newpivot]>=word[i]){
                temp1="";
                for(int j=i; j>=start; j--)
                    temp1+=word[j];
                //cout << "comparing: " << temp1 << " " << temp2 << endl;
                if(temp2>temp1){
                    newpivot=i;
                    temp2=temp1;
                }
            }
        }
        end=newpivot;
    }

    //swap to end
    while (start<=end){
        swap(word[start], word[end]);
        start++, end--;
    }
    return newpivot+1;
}

int main(){
    string word={};
    int pivot=0;

    cin >> word;

    //cout << "word 1:" << endl;
    pivot = split(word, pivot, word.length()-3);
    //cout << "word 2:" << endl;
    pivot = split(word, pivot, word.length()-2);
    //cout << "word 3:" << endl;
    pivot = split(word, pivot, word.length()-1, 1);    

    cout << word;
    return 0;
}