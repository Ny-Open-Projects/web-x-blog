// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144830623
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  static int longestConsecutive(int[] nums) { // 定义函数/方法 longestConsecutive
    Set<Integer> set = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> set
    for (int v : nums) set.add(v); // for (int 值 : 数组) set 追加 值);
    int best = 0; // 把 0 存入 当前最优
    for (int num : set) { // for (int num : set) {
      if (!set.contains(num - 1)) { // 若 取反 set 是否包含 num 减 1
        int cur = num, streak = 1; // 把 num, streak 赋值为 1 存入 当前值
        while (set.contains(cur + 1)) {
          cur++;
          streak++;
        } // 循环，直到不满足「set 是否包含 当前值 加 1)) { 当前值 加一 ; streak 加一 ; }」
        if (streak > best) best = streak; // 若 streak 超过 当前最优) 当前最优 赋值为 streak;
      }
    }
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{100, 4, 200, 1, 3, 2}, {0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, {1, 0, 1, 2}};
    int[] wants = {4, 9, 3}; // 把 {4, 9, 3}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int got = longestConsecutive(ins[i]); // 把 longestConsecutive(ins[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        System.out.println(
            "FAIL in=" + Arrays.toString(ins[i]) + " want=" + wants[i] + " got=" + got); // 打印输出
        ok = false; // 把 false; 写入 ok
      }
    }
    if (!ok) {
      System.out.println("RESULT: FAIL");
      System.exit(1);
    } // 若 取反 ok) { System.out.输出(「RESULT: FAIL」); System.exit(1); }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
