// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int seqSearch(int[] arr, int target) { // 定义函数/方法 seqSearch
    for (int i = 0; i < arr.length; i++)
      if (arr[i] == target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] a = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};
    int[] t = {1, 3, 5};
    int[] ws = {0, 2, -1};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      int got = seqSearch(a[i], t[i]); // 把 seqSearch(数组[下标 i], 另一字符串[下标 i]) 存入 got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
