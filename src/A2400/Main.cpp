/* Sudoku Solver */
#include <iostream>

struct Matrix {
    int data[9][9];
};

struct SearchResult {
    bool success;
    Matrix matrix;

    SearchResult(bool success, Matrix matrix) {
        this->success = success;
        this->matrix = matrix;
    }
};

SearchResult search(Matrix matrix, int start_row) {
    int x, y;
    bool hasEmpty = false;
    for (y = start_row; y < 9; y++) {
        for (x = 0; x < 9; x++) {
            if (matrix.data[y][x] == 0)
                hasEmpty = true;
            if (hasEmpty)
                break;
        }
        if (hasEmpty)
            break;
    }
    if (!hasEmpty)
        return SearchResult(true, matrix);

    bool occupied[9] = { false };
    for (int r = 0; r < 9; r++)
        if (matrix.data[r][x] != 0)
            occupied[matrix.data[r][x] - 1] = true;
    for (int c = 0; c < 9; c++)
        if (matrix.data[y][c] != 0)
            occupied[matrix.data[y][c] - 1] = true;

    int regionX = x / 3;
    int regionY = y / 3;
    for (int dy = 0; dy < 3; dy++)
        for (int dx = 0; dx < 3; dx++)
            if (matrix.data[regionY * 3 + dy][regionX * 3 + dx] != 0)
                occupied[matrix.data[regionY * 3 + dy][regionX * 3 + dx] - 1] = true;

    for (int i = 0; i < 9; i++) {
        if (!occupied[i]) {
            matrix.data[y][x] = i + 1;
            SearchResult result = search(matrix, y);
            if (result.success) {
                return result;
            }
            else {
                matrix.data[y][x] = 0;
            }
        }
    }

    return SearchResult(false, matrix);
}

int main() {
    Matrix origin = Matrix();
    for (int r = 0; r < 9; r++)
        for (int c = 0; c < 9; c++)
            scanf_s("%d", &origin.data[r][c]);

    SearchResult result = search(origin, 0);
    for (int r = 0; r < 9; r++)
        for (int c = 0; c < 9; c++)
            if (c != 8)
                printf("%d ", result.matrix.data[r][c]);
            else
                printf("%d\n", result.matrix.data[r][c]);

    return 0;
}
