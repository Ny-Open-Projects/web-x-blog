// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc350_solution22 { // 定义类型
  static int[] intersect(int[] nums1, int[] nums2) { // 定义函数/方法 intersect
    Arrays.sort(nums1); // 排序
    Arrays.sort(nums2); // 排序
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    int i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
    while (i < nums1.length && j < nums2.length) { // 循环，直到不满足「下标 i 小于 数组1.长度 且 下标 j 小于 数组2.长度」
      if (nums1[i] < nums2[j]) i++; // 若 数组1[下标 i] 小于 数组2[下标 j]) 下标 i 加一 ;
      else if (nums1[i] > nums2[j]) j++; // 否则，若 数组1[下标 i] 超过 数组2[下标 j]) 下标 j 加一 ;
      else { // 否则
        res.add(nums1[i]); // 结果 追加 数组1[下标 i]);
        i++; // 下标 i 加一
        j++; // 下标 j 加一
      }
    }
    int[] out = new int[res.size()]; // 把 new int[结果.大小()]; 写入 int[] out
    for (int k = 0; k < res.size(); k++) out[k] = res.get(k); // 让 下标 k 从 0 开始计数，下标 k 小于 结果.大小() 就继续
    return out; // 返回 out
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] a = intersect(new int[] {1, 2, 2, 1}, new int[] {2, 2});
    if (!(a.length == 2 && a[0] == 2 && a[1] == 2)) // 若 取反 (数组.长度 等于 2 且 数组[0] 等于 2 且 数组[1] 等于 2
    throw new RuntimeException("FAILED a: " + Arrays.toString(a));
    int[] b = intersect(new int[] {4, 9, 5}, new int[] {9, 4, 9, 8, 4});
    if (!(b.length == 2 && b[0] == 4 && b[1] == 9)) // 若 取反 (b.长度 等于 2 且 b[0] 等于 4 且 b[1] 等于 9
    throw new RuntimeException("FAILED b: " + Arrays.toString(b));
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
