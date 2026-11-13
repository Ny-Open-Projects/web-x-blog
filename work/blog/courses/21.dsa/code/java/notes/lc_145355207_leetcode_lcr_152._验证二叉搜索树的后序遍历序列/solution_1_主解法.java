// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class BstS1 { // 定义类型
  static boolean verifyPostorder(int[] postorder) { // 定义函数/方法 verifyPostorder
    return helper(postorder); // 返回 helper(postorder)
  }

  static boolean helper(int[] seq) { // 定义函数/方法 helper
    if (seq.length <= 1) return true; // 若 seq.长度 不超过 1，直接返回 true
    int root = seq[seq.length - 1]; // 把 seq[seq.长度 减 1] 存入 根节点
    int i = 0; // 把 0 存入 下标 i
    while (i < seq.length - 1 && seq[i] < root)
      i++; // 循环，直到不满足「下标 i 小于 seq.长度 减 1 且 seq[下标 i] 小于 根节点) 下标 i 加一 ;」
    for (int j = i; j < seq.length - 1; j++)
      if (seq[j] <= root) return false; // 让 下标 j 从 下标 i 开始计数，下标 j 小于 seq.长度 减 1 就继续
    int[] left = Arrays.copyOfRange(seq, 0, i); // 把 Arrays.copyOfRange(seq, 0, 下标 i); 写入 int[] left
    int[] right =
        Arrays.copyOfRange(
            seq, i, seq.length - 1); // 把 Arrays.copyOfRange(seq, 下标 i, seq.长度 减 1); 写入 int[] right
    return helper(left) && helper(right); // 返回 helper(左边界) 且 helper(右边界)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean[] got = { // 把 { 写入 boolean[] got
      BstS1.verifyPostorder(new int[] {1, 6, 3, 2, 5}),
      BstS1.verifyPostorder(new int[] {1, 3, 2, 6, 5}),
      BstS1.verifyPostorder(new int[] {4, 8, 6, 12, 10, 9}),
    };
    boolean[] want = {false, true, true}; // 把 { false, true, true }; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
