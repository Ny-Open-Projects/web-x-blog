// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
package com.webfault.dsa; // 引入依赖

class lc674_solution111 { // 定义类型
  int findLengthOfLCIS(int[] nums) { // 定义函数/方法 findLengthOfLCIS
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int ans = 1, cur = 1; // 把 1, 当前值 赋值为 1 存入 答案
    for (int i = 1; i < nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[i - 1]) { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
        cur++; // 当前值 加一
        if (cur > ans) ans = cur; // 若 当前值 超过 答案) 答案 赋值为 当前值;
      } else { // 否则
        cur = 1; // 把 1; 写入 当前值
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc674_solution111 s =
        new lc674_solution111(); // 把 new lc674_solution111(); 写入 lc674_solution111 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.findLengthOfLCIS(new int[] {1, 3, 5, 4, 7}) != 3) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.findLengthOfLCIS(new int[] {2, 2, 2, 2, 2}) != 1) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (s.findLengthOfLCIS(new int[] {1, 3, 5, 7}) != 4) {
      ok = false;
      System.out.println("FAIL3");
    }
    if (s.findLengthOfLCIS(new int[] {}) != 0) {
      ok = false;
      System.out.println("FAIL4");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
