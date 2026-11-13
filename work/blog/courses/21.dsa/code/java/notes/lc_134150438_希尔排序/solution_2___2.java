// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ShellS2 { // 定义类型
  static int[] shellSort(int[] lst) { // 定义函数/方法 shellSort
    int length = lst.length; // 把 lst.长度 存入 长度
    int gap = length / 2; // 把 长度 除以 2 存入 gap
    while (gap > 0) { // 循环，直到不满足「gap 超过 0」
      for (int i = gap; i < length; i++) { // 让 下标 i 从 gap 开始计数，下标 i 小于 长度 就继续
        int tmp = lst[i]; // 把 lst[下标 i] 存入 临时变量
        int p = i; // 把 下标 i 存入 节点
        while (p - gap >= 0
            && lst[p - gap] > tmp) { // 循环，直到不满足「节点 减 gap 不低于 0 且 lst[节点 减 gap] 超过 临时变量」
          lst[p] = lst[p - gap]; // 把 lst[节点 减 gap]; 写入 lst[p]
          p -= gap; // 节点累减 gap
        }
        lst[p] = tmp; // 把 临时变量; 写入 lst[p]
      }
      gap /= 2; // 把 2; 写入 gap /
    }
    return lst; // 返回 lst
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{9, 12, 1, 3, -1, 22, 22, 31, 1, 0}, {-1, 0, 1, 1, 3, 9, 12, 22, 22, 31}},
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{1}, {1}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          ShellS2.shellSort(c[0].clone()); // 把 ShellS2.shellSort(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) { // 若 取反 Arrays.equals(got, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(got)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
