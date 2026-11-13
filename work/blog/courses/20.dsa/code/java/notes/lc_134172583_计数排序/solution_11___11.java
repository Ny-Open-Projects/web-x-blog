// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_11___11.py (count_sort optimized: string-join build)
  static int[] countSort(int[] lst) { // 定义函数/方法 countSort
    int length = lst.length; // 把 lst.长度 存入 长度
    if (length < 2) return lst; // 若 长度 小于 2，直接返回 lst
    int maxVal = lst[0], minVal = lst[0]; // 把 lst[0], minVal 赋值为 lst[0] 存入 maxVal
    for (int v : lst) {
      if (v > maxVal) maxVal = v;
      if (v < minVal) minVal = v;
    }
    int[] countList =
        new int[maxVal - minVal + 1]; // 把 new int[maxVal 减 minVal 加 1]; 写入 int[] countList
    for (int num : lst)
      countList[num - minVal] += 1; // 把 1; 写入 for (int num : lst) countList[num - minVal] +
    StringBuilder strResult =
        new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder strResult
    for (int j = 0;
        j < maxVal - minVal + 1;
        j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 maxVal 减 minVal 加 1 就继续
      if (countList[j] == 0) continue; // 若 countList[下标 j] 等于 0) continue;
      for (int c = 0; c < countList[j]; c++) { // 让 字符 从 0 开始计数，字符 小于 countList[下标 j] 就继续
        strResult.append(j + minVal).append(','); // 把 下标 j 加 minVal 追加到列表尾部
      }
    }
    String s = strResult.toString(); // 把 strResult.toString() 存入 字符串
    if (s.endsWith(","))
      s = s.substring(0, s.length() - 1); // 若 字符串.endsWith(「,」)) 字符串 赋值为 字符串 截取 0, 字符串.长度() 减 1);
    if (s.isEmpty()) return new int[0]; // 若 字符串.isEmpty()，直接返回 new int[0]
    String[] parts = s.split(","); // 把 字符串.split(「,」); 写入 String[] parts
    int[] result = new int[parts.length]; // 把 new int[parts.长度]; 写入 int[] result
    for (int i = 0; i < parts.length; i++)
      result[i] = Integer.parseInt(parts[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 parts.长度 就继续
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {3, 1, 2},
      {5, -3, 0, 5, -1},
      {1, 2, 3},
      {},
      {7},
      {1},
      {
        102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106,
        109, 102
      },
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3},
      {-3, -1, 0, 5, 5},
      {1, 2, 3},
      {},
      {7},
      {1},
      {
        101, 101, 102, 102, 102, 102, 102, 102, 102, 103, 103, 104, 104, 106, 107, 107, 108, 108,
        109, 109
      },
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int[] got = countSort(cases[ci]); // 把 countSort(cases[ci]); 写入 int[] got
      if (!Arrays.equals(got, wants[ci])) { // 若 取反 Arrays.equals(got, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL countSort("
                + Arrays.toString(cases[ci])
                + ")="
                + Arrays.toString(got)
                + " want="
                + Arrays.toString(wants[ci])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
