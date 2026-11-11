package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// LeetCode 66. 加一。忠实翻译 Python 参考实现 ref_plusOne。
class lc66_solution1 { // 定义类型
  int[] plusOne(int[] digits) { // 定义函数/方法 plusOne
    int[] d =
        Arrays.copyOf(digits, digits.length); // 把 Arrays.copyOf(digits, digits.长度); 写入 int[] d
    for (int i = d.length - 1; i >= 0; i--) { // 让 下标 i 从 d.长度 减 1 开始计数，下标 i 不低于 0 就继续
      if (d[i] == 9) { // 若 d[下标 i] 等于 9
        d[i] = 0; // 把 0; 写入 d[i]
      } else { // 否则
        d[i]++; // d[下标 i] 加一 ;
        return d; // 返回 d
      }
    }
    int[] res = new int[digits.length + 1]; // 把 new int[digits.长度 加 1]; 写入 int[] res
    res[0] = 1; // 把 1; 写入 res[0]
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_66_加一"]
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {1, 2, 4}},
      {{4, 3, 2, 1}, {4, 3, 2, 2}},
      {{9, 9, 9}, {1, 0, 0, 0}},
    };
    lc66_solution1 s = new lc66_solution1(); // 把 new lc66_solution1(); 写入 lc66_solution1 s
    boolean allOK = true; // 把 true; 写入 boolean allOK
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got = s.plusOne(c[0]); // 把 字符串.plusOne(字符[0]); 写入 int[] got
      int[] want = c[1]; // 把 字符[1]; 写入 int[] want
      if (!Arrays.equals(got, want)) { // 若 取反 Arrays.equals(got, want
        allOK = false; // 把 false; 写入 allOK
        System.out.println(
            "FAIL plusOne("
                + Arrays.toString(c[0])
                + ") = "
                + Arrays.toString(got)
                + ", want "
                + Arrays.toString(want)); // 打印输出
      }
    }
    if (!allOK) { // 若 取反 allOK
      throw new RuntimeException(
          "some cases FAILED"); // throw new RuntimeException(「some cases FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
