/**
 * 43686
 */
import java.util.*;

public class Main {
    static int n;
    static int[] xNums;
    static int[] yNums;
    static final int[][] DELTA = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        xNums = new int[n];
        yNums = new int[n];

        for (int i = 0; i < n; i++)
            xNums[i] = scanner.nextInt();
        for (int i = 0; i < n; i++)
            yNums[i] = scanner.nextInt();

        List<int[]> path = search(new int[]{0, 0}, new ArrayList<>(), new int[n], new int[n]);
        printNormPath(path);
    }

    static List<int[]> search(int[] nextXY, List<int[]> curPath, int[] curXNums, int[] curYNums) {
        int cx = nextXY[0], cy = nextXY[1];
        curPath.add(nextXY);
        curXNums[cx]++;
        curYNums[cy]++;

        if (curXNums[cx] <= xNums[cx] && curYNums[cy] <= yNums[cy]) {
            if (cx == n - 1 && cy == n - 1 && Arrays.equals(curXNums, xNums) && Arrays.equals(curYNums, yNums))
                return curPath;
            for (int[] delta : DELTA) {
                int nx = cx + delta[0], ny = cy + delta[1];
                if (!curPath.stream().anyMatch(p -> p[0] == nx && p[1] == ny) && nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    List<int[]> rst = search(new int[]{nx, ny}, curPath, curXNums, curYNums);
                    if (rst != null)
                        return rst;
                }
            }
        }

        curXNums[cx]--;
        curYNums[cy]--;
        curPath.remove(curPath.size() - 1);
        return null;
    }

    static void printNormPath(List<int[]> path) {
        for (int[] point : path) {
            System.out.print(n * point[1] + point[0] + " ");
        }
    }
}
