// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package com.webfault.dsa; // 引入依赖

class notes108_bs { // 定义类型
  int binarySearch(int[] arr, int target) { // 定义函数/方法 binarySearch
    int left = 0, right = arr.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      int mid = left + (right - left) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
      if (arr[mid] == target) return mid; // 若 数组[中点] 等于 目标值，直接返回 中点
      if (arr[mid] < target) left = mid + 1; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1;
      else right = mid - 1; // 否则
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    notes108_bs s = new notes108_bs(); // 把 new notes108_bs(); 写入 notes108_bs s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.binarySearch(new int[] {1, 3, 5, 7, 9}, 5) != 2) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.binarySearch(new int[] {1, 3, 5, 7, 9}, 4) != -1) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (s.binarySearch(new int[] {}, 5) != -1) {
      ok = false;
      System.out.println("FAIL3");
    }
    if (s.binarySearch(new int[] {1, 3, 5, 7, 9}, 1) != 0) {
      ok = false;
      System.out.println("FAIL4");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
