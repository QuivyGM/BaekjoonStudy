// code runtime is ( O(n^2) ) because of the nested loop in the insertionSort function

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void insertionSort(vector<string>& list) {     // function to sort list, list is passed by reference
    for (int i = 1; i < list.size(); i++) {     // loop as long as there are elements in the list
        string key = list[i];                   // key is the current element of the list
        int j = i - 1;

        // Move elements of list[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && (list[j].length() > key.length() ||            // if the length of the current element is greater than the key
              (list[j].length() == key.length() && list[j] > key))) {   // or if the length is the same but the current element is greater than the key
            list[j + 1] = list[j];                                      // move the current element to the next position
            j = j - 1;                                                  // move to the previous element
        }
        list[j + 1] = key;                                              // insert the key in the correct position
    }
}

int main() {
    int N;
    cin >> N;

    vector<string> list(N);             // create string vector of size N
    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    insertionSort(list);
    list.erase(unique(list.begin(), list.end()), list.end());
    // .erase(a, b) : removes elements from a to b
    // .unique(a, b) : rearranges elements in a to b so that all the unique elements are at the beginning

    // Output the sorted list
    for (const string& word : list) {       // loop as long as there are elements in the list
        cout << word << endl;
    }

    return 0;
}