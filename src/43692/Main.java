/**
 * 43692
 */
import java.util.*;

public class Main {
    static String origin;
    static String target;
    static int length;
    static final int[] DELTA = {-3, -2, -1, 1, 2, 3};

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        origin = scanner.nextLine();
        target = scanner.nextLine();
        length = origin.length();

        System.out.println(search(new HashSet<>(Collections.singletonList(origin)), 1));
    }

    static int search(HashSet<String> curSitus, int curSteps) {
        HashSet<String> nextSitus = new HashSet<>();
        for (String cur : curSitus) {
            int emptyIndex = cur.indexOf('*');
            for (int d : DELTA) {
                int newIndex = emptyIndex + d;
                if (newIndex >= 0 && newIndex < length) {
                    String next = swap(cur, emptyIndex, newIndex);
                    if (next.equals(target))
                        return curSteps;
                    nextSitus.add(next);
                }
            }
        }
        return search(nextSitus, curSteps + 1);
    }

    static String swap(String str, int i, int j) {
        char[] arr = str.toCharArray();
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return new String(arr);
    }
}
