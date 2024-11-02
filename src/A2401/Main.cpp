/* Counting Valid Sequences */
#include <iostream>
const int MAX = 24;

struct String {
    char data[MAX] = { '\0' };
};

int isValidMask(String str, int mask, int globalMinRemoval) {
    bool hasPaired = false;
    int totalRemoval = 0;
    int parenStartCount = 0;
    int squareStartCount = 0;
    for (int i = 0; i < MAX; i++) {
        if ((mask & (1 << i)) == 0) {
            totalRemoval += str.data[i] != '\0';
            if (globalMinRemoval != -1 && globalMinRemoval < totalRemoval)
                break;
            else
                continue;
        }
        switch (str.data[i]) {
        case '\0':
            return -1;
        case '(':
            parenStartCount++;
            break;
        case ')':
            if (parenStartCount == 0)
                return -1;
            hasPaired = true;
            parenStartCount--;
            break;
        case '[':
            if (parenStartCount > 0)
                return -1;
            squareStartCount++;
            break;
        case ']':
            if (parenStartCount > 0 || squareStartCount == 0)
                return -1;
            hasPaired = true;
            squareStartCount--;
            break;
        }
    }
    if (hasPaired == true && parenStartCount == 0 && squareStartCount == 0)
        return totalRemoval;
    return -1;
}

int main() {
    String origin = String();
    scanf("%s", &origin.data);

    int ways = 0;
    int minRemoval = -1;
    for (int mask = 1; mask < (1 << 24) - 1; mask++) {
        int result = isValidMask(origin, mask, minRemoval);
        if (result != -1) {
            if (ways == 0 || minRemoval > result) {
                ways = 1;
                minRemoval = result;
            }
            else if (minRemoval == result) {
                ways++;
            }
        }
    }

    if (ways == 0)
        printf("none 0");
    else
        printf("%d %d", minRemoval, ways);
    return 0;
}
