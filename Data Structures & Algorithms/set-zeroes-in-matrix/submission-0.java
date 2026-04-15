class Solution {
    public void setZeroes(int[][] matrix) {
        boolean isFirstRowZero = false;
        boolean isFirstColZero = false;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0) isFirstRowZero = true;
                    else matrix[i][0] = 0;
                    if (j == 0) isFirstColZero = true;
                    else matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < matrix.length; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 0; j < matrix[0].length; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int i = 1; i < matrix[0].length; i++) {
            if (matrix[0][i] == 0) {
                for (int j = 0; j < matrix.length; j++) {
                    matrix[j][i] = 0;
                }
            }
        }

        if (isFirstRowZero) {
            for (int i =0; i < matrix[0].length; i++) matrix[0][i] = 0;
        }

        if (isFirstColZero) {
            for (int i = 0; i < matrix.length; i++) matrix[i][0] = 0;
        }
    }
}