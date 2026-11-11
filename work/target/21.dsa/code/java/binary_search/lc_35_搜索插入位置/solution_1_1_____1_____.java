// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int searchInsert(int[] nums, int target) { // 定义函数/方法 searchInsert
    int left = 0, right = nums.length; // 把 0, 右边界 赋值为 数组.长度 存入 左边界
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      int mid = left + (right - left) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
      if (nums[mid] < target) left = mid + 1; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1;
      else right = mid; // 否则
    }
    return left; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.searchInsert(new int[] {1, 3, 5, 6}, 5) != 2) {
      ok = false;
      System.out.println("FAIL 5");
    }
    if (s.searchInsert(new int[] {1, 3, 5, 6}, 2) != 1) {
      ok = false;
      System.out.println("FAIL 2");
    }
    if (s.searchInsert(new int[] {1, 3, 5, 6}, 7) != 4) {
      ok = false;
      System.out.println("FAIL 7");
    }
    if (s.searchInsert(new int[] {1, 3, 5, 6}, 0) != 0) {
      ok = false;
      System.out.println("FAIL 0");
    }
    if (s.searchInsert(new int[] {}, 5) != 0) {
      ok = false;
      System.out.println("FAIL empty");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
