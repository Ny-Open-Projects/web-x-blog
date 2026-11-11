// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class lc134082074_solution33 { // 定义类型
  // insertionSort 忠实翻译 python ref solution_3___3.py（tmp 风格 + i != j 优化，就地排序并返回 nums）
  public static int[] insertionSort(int[] nums) { // public static int[] insertionSort(int[] 数组) {
    int length = nums.length; // 把 数组.长度 存入 长度
    for (int i = 1; i < length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
      int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
      int j = i; // 把 下标 i 存入 下标 j
      while (j > 0) { // 循环，直到不满足「下标 j 超过 0」
        if (nums[j - 1] > tmp) { // 若 数组[下标 j 减 1] 超过 临时变量
          nums[j] = nums[j - 1]; // 把 数组[下标 j 减 1]; 写入 nums[j]
        } else { // 否则
          break; // 跳出循环
        }
        j--; // 下标 j 减一
      }
      if (i != j) { // 若 下标 i 不等于 下标 j
        nums[j] = tmp; // 把 临时变量; 写入 nums[j]
      }
    }
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new int[] {1, 2, 3}, new int[] {1, 2, 3}},
      {new int[] {5, 4, 3, 2, 1}, new int[] {1, 2, 3, 4, 5}},
      {new int[] {}, new int[] {}},
      {new int[] {1}, new int[] {1}},
      {new int[] {3, 1, 2, 1, 3}, new int[] {1, 1, 2, 3, 3}},
      {new int[] {2, -1, 0}, new int[] {-1, 0, 2}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int[] in = (int[]) c[0]; // 把 (int[]) 字符[0]; 写入 int[] in
      int[] want = (int[]) c[1]; // 把 (int[]) 字符[1]; 写入 int[] want
      int[] got = insertionSort(in); // 把 insertionSort(in); 写入 int[] got
      if (!Arrays.equals(got, want)
          || !Arrays.equals(
              in, want)) { // 若 取反 Arrays.equals(got, want) 或 取反 Arrays.equals(in, want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL got " + Arrays.toString(got) + " want " + Arrays.toString(want)); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
