// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_1_1_____1___.py (cmp_to_key: xy>yx => -1)
  static String largestNumber(int[] nums) { // 定义函数/方法 largestNumber
    String[] strs = new String[nums.length]; // 把 new String[数组.长度]; 写入 String[] strs
    for (int i = 0; i < nums.length; i++)
      strs[i] = String.valueOf(nums[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    Arrays.sort(
        strs,
        new Comparator<String>() { // 排序
          public int compare(String x, String y) { // 定义函数/方法 compare
            String xy = x + y; // 把 x 加 y 存入 xy
            String yx = y + x; // 把 y 加 x 存入 yx
            if (xy.compareTo(yx) > 0) return -1; // 若 xy.compareTo(yx) 超过 0，直接返回 减 1
            else if (xy.compareTo(yx) < 0) return 1; // 否则，若 xy.compareTo(yx) 小于 0) return 1;
            else return 0; // 否则
          }
        }); // });
    if (strs[0].equals("0")) return "0"; // 若 strs[0].equals(「0」)，直接返回 「0」
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (String s : strs) sb.append(s); // 把 字符串 追加到列表尾部
    return sb.toString(); // 返回 sb.toString()
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
