// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
package com.webfault.dsa; // 引入依赖

class Lc1685 { // 定义类型
  static int[] getSumAbsoluteDifferences(int[] nums) { // 定义函数/方法 getSumAbsoluteDifferences
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int leftSum = 0; // 把 0 存入 leftSum
    int rightSum = 0; // 把 0 存入 rightSum
    for (int v : nums) rightSum += v; // 把 值; 写入 for (int v : nums) rightSum +
    int[] result = new int[n]; // 把 new int[元素个数]; 写入 int[] result
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      rightSum -= nums[i]; // rightSum累减 数组[下标 i]
      result[i] = i * nums[i] - leftSum + rightSum - (n - i - 1) * nums[i];
      leftSum += nums[i]; // leftSum累加 数组[下标 i]
    }
    return result; // 返回 结果
  }

  static boolean eq(int[] a, int[] b) { // 定义函数/方法 eq
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (int i = 0; i < a.length; i++)
      if (a[i] != b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {3, 2, 3}},
      {{1, 2, 3, 4}, {6, 4, 4, 6}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          getSumAbsoluteDifferences(c[0]); // 把 getSumAbsoluteDifferences(字符[0]); 写入 int[] got
      if (!eq(got, c[1])) {
        ok = false;
        System.out.println(
            "FAIL getSumAbsoluteDifferences("
                + java.util.Arrays.toString(c[0])
                + ")="
                + java.util.Arrays.toString(got)
                + " want "
                + java.util.Arrays.toString(c[1]));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
