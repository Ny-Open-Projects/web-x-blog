// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int[] two_sum_brute(int[] nums, int target) { // 定义函数/方法 two_sum_brute
    for (int i = 0; i < nums.length; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    for (int j = i + 1; j < nums.length; j++) // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 数组.长度 就继续
      if (nums[i] + nums[j] == target)
          return new int[] {i, j}; // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值，直接返回 new int[]{下标 i, 下标 j}
    return new int[] {}; // 返回 new int[]{}
  }

  int[] two_sum_hash(int[] nums, int target) { // 定义函数/方法 two_sum_hash
    java.util.Map<Integer, Integer> seen = new java.util.HashMap<>();
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (seen.containsKey(target - nums[i])) return new int[] {seen.get(target - nums[i]), i};
      seen.put(nums[i], i); // 已见集合.put(数组[下标 i], 下标 i);
    }
    return new int[] {}; // 返回 new int[]{}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!java.util.Arrays.equals(s.two_sum_brute(new int[] {2, 7, 11, 15}, 9), new int[] {0, 1})) {
      ok = false;
      System.out.println("FAIL two_sum_brute");
    }
    if (!java.util.Arrays.equals(s.two_sum_hash(new int[] {2, 7, 11, 15}, 9), new int[] {0, 1})) {
      ok = false;
      System.out.println("FAIL two_sum_hash");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
