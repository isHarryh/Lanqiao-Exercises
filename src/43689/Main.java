/**
 * 43689
 */
import java.util.*;

public class Main {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        final int N = scanner.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++)
            nums[i] = scanner.nextInt();

        int gcd = gcd(nums);
        if (gcd != 1) {
            System.out.println("INF");
        } else {
            int veryBig = 1 << 16;
            int canNot = 0;
            boolean[] dp = new boolean[veryBig];
            dp[0] = true;

            for (int i = 1; i < veryBig; i++) {
                canNot += 1;
                for (int n : nums) {
                    if (i >= n && dp[i - n]) {
                        dp[i] = true;
                        canNot -= 1;
                        break;
                    }
                }
            }

            System.out.println(canNot);
        }
    }

    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    static int gcd(int[] nums) {
        int result = nums[0];
        for (int i = 1; i < nums.length; i++)
            result = gcd(result, nums[i]);
        return result;
    }
}
