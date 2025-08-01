#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    int R = 1, C = 1;
    char grid[41][41] = {0, };
    char alphabet[27] = {0, };

    bool RECTANGLE[27] = {true};

    while (true) {

        // set grid size
        scanf("%d %d", &R, &C);

        // end loop
        if(R+C == 0)
            break;

        // reset grid
        for (int i = 0; i < 41; i++)
            for (int j = 0; j < 41; j++)
                grid[i][j] = 0;
        for (int i = 0; i < 26; i++){
            alphabet[i] = 0;
            RECTANGLE[i] = true;
        }

        // set grid
        for (int DOWN = 0; DOWN < R; DOWN++) {
            scanf("%s", grid[DOWN]);
            for (int RIGHT = 0; RIGHT < C; RIGHT++) {
                if (grid[DOWN][RIGHT] != '.') {
                    alphabet[grid[DOWN][RIGHT] - 'a']++;
                }
            }
        }
        
        // print start
        printf("Uncovered: ");

        // search grid
        // 1. begin with alphabet
        for(int alph_search = 0; alph_search < 26; alph_search++){

            // 2. if alphabet_counter > 0 = number is valid
            if (alphabet[alph_search] > 0){
                char target = 'a' + alph_search;

                // 3. check(1) - check rectangle --------------------------------------
                int down_start = R, down_max = -1;
                int right_start = C, right_max = -1;

                // 3-1. find alphabet grid
                for (int down = 0; down < R; down++) {
                    for (int right = 0; right < C; right++) {
                        if (grid[down][right] == target) {
                            if (down < down_start) down_start = down;
                            if (down > down_max)   down_max = down;
                            if (right < right_start) right_start = right;
                            if (right > right_max)   right_max = right;
                        }
                    }
                }

                // 3-2. Check grid
                // 3-2-1. enough to fill rect?
                if ( (down_max-down_start+1)*(right_max-right_start+1) == alphabet[alph_search] ){
                    // if enough to fill grid then check if grid is filled with no exceptions
                    for (int i = down_start; i <= down_max; i++) {
                        for (int j = right_start; j <= right_max; j++) {
                            // if different letter then skip
                            if (grid[i][j] != target) {
                                // update state
                                RECTANGLE[alph_search] = false;
                                // exit loop
                                i = down_max + 1;
                                break;
                            }
                        }
                    }
                }
                else{
                    RECTANGLE[alph_search] = false;
                }

                // 4. check(2) - check overlap --------------------------------------
                if (RECTANGLE[alph_search]) {
                    for (int i = down_start; i <= down_max; i++) {
                        for (int j = right_start; j <= right_max; j++) {
                            if (grid[i][j] != '.' && grid[i][j] != target) {
                                RECTANGLE[alph_search] = false;
                                i = down_max + 1;
                                break;
                            }
                        }
                    }
                }


                // 5. print result
                if (RECTANGLE[alph_search]){
                    printf("%c", 'a' + alph_search);
                }
            }
        }
        printf("\n");
    }
    return 0;
}
