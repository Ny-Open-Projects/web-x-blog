// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_3_3_____3___-____.py (cmp sort via quickSort)
  static String largestNumber(int[] nums) { // 定义函数/方法 largestNumber
    String[] strs = new String[nums.length]; // 把 new String[数组.长度]; 写入 String[] strs
    for (int i = 0; i < nums.length; i++)
      strs[i] = String.valueOf(nums[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    quickSort(strs, 0, strs.length - 1); // quickSort(strs, 0, strs.长度 减 1);
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (String s : strs) sb.append(s); // 把 字符串 追加到列表尾部
    String res = sb.toString(); // 把 sb.toString() 存入 结果
    if (strs[strs.length - 1].equals("0")) return "0"; // 若 strs[strs.长度 减 1].equals(「0」)，直接返回 「0」
    return res; // 返回 结果
  }

  static void quickSort(String[] strs, int l, int r) { // 定义函数/方法 quickSort
    if (l >= r) return; // 若 左指针 不低于 右指针) return;
    int i = l, j = r; // 把 左指针, 下标 j 赋值为 右指针 存入 下标 i
    String pivot = strs[l + (r - l) / 2]; // 把 strs[(左指针 加 右指针) 除以 2] 存入 pivot
    while (i <= j) { // 循环，直到不满足「下标 i 不超过 下标 j」
      while ((strs[i] + pivot).compareTo(pivot + strs[i]) > 0) i++;
      while ((strs[j] + pivot).compareTo(pivot + strs[j]) < 0) j--;
      if (i <= j) { // 若 下标 i 不超过 下标 j
        String tmp = strs[i]; // 把 strs[下标 i] 存入 临时变量
        strs[i] = strs[j]; // 把 strs[下标 j]; 写入 strs[i]
        strs[j] = tmp; // 把 临时变量; 写入 strs[j]
        i++; // 下标 i 加一
        j--; // 下标 j 减一
      }
    }
    if (l < j) quickSort(strs, l, j); // 若 左指针 小于 下标 j) quickSort(strs, 左指针, 下标 j);
    if (r > i) quickSort(strs, i, r); // 若 右指针 超过 下标 i) quickSort(strs, 下标 i, 右指针);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {10, 2},
      {3, 30, 34, 5, 9},
      {0, 0},
      {1},
    };
    String[] wants = {
      "210", "9534330", "0", "1"
    }; // 把 {「210」, 「210」, 「210」, 「210」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      String got = largestNumber(cases[ci]); // 把 largestNumber(cases[ci]) 存入 got
      if (!got.equals(wants[ci])) { // 若 取反 got.equals(wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL largestNumber("
                + Arrays.toString(cases[ci])
                + ")=\""
                + got
                + "\" want \""
                + wants[ci]
                + "\""); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
