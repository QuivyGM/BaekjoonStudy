//errors: 
//  illegal instruction: strlen is deisgned for C-Styled strings but std::strings are designed for c++ -> instead should use .length or .size
//  timeout: one to one compare with neighbor takes too long -> compare with entire list? -> use insertionSort
//  need to remove duplicates -> use .erase(unique(list.begin(), list.end()), list.end()); (used for vectors and strings)

#include<iostream>
using namespace std;


// void sort(string list[], int N){
//     for(int i=0; i<N; i++)
//         for(int j=i; j<N; j++)
//             if (list[i].length() > list[j].length() || (list[i].length() == list[j].length() && list[i] > list[j]))
//                 swap(list[i], list[j]);
// }

void sortSingle(string list[], int N){
        for(int i=0; i<N; i++)
            if (list[i].length() > list[N].length() || (list[i].length() == list[N].length() && list[i] > list[N]))
                swap(list[i], list[N]);
}

int main(){
    int N;
    cin >> N;

    string *list = new string[N];
    for(int i=0; i<N; i++){
        cin >> list[i];  
        sortSingle(list, i);
    }
    //sort(list, N);

    //cout << "\n\n";
    for(int i=0; i<N; i++)
        cout << list[i] << endl;


    delete [] list;
}