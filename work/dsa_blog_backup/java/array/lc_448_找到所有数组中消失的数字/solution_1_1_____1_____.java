package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc448_solution1 { // 定义类型
  // 找到所有数组中消失的数字
  // 忠实翻译 Python ref_findDisappearedNumbers: 用集合标记后按顺序收集 1..n 中缺失者
  static List<Integer> findDisappearedNumbers(int[] nums) { // 定义函数/方法 findDisappearedNumbers
    Set<Integer> s = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> s
    for (int v : nums) s.add(v); // for (int 值 : 数组) 字符串 追加 值);
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    for (int i = 1; i <= nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 数组.长度 就继续
      if (!s.contains(i)) res.add(i); // 若 取反 字符串 是否包含 下标 i)) 结果 追加 下标 i);
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] inputs = {
      {4, 3, 2, 7, 8, 2, 3, 1}, {1, 1}
    }; // 把 {{4, 3, 2, 7, 8, 2, 3, 1}, {1, 1}}; 写入 int[][] inputs
    int[][] wants = {{5, 6}, {2}}; // 把 {{5, 6}, {2}}; 写入 int[][] wants
    for (int i = 0; i < inputs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 inputs.长度 就继续
      List<Integer> got =
          findDisappearedNumbers(
              inputs[i]); // 把 findDisappearedNumbers(inputs[下标 i]); 写入 List<Integer> got
      int[] ga = new int[got.size()]; // 把 new int[got.大小()]; 写入 int[] ga
      for (int k = 0; k < ga.length; k++) ga[k] = got.get(k); // 让 下标 k 从 0 开始计数，下标 k 小于 ga.长度 就继续
      if (!Arrays.equals(ga, wants[i])) { // 若 取反 Arrays.equals(ga, wants[下标 i]
        System.out.println(
            "FAIL: findDisappearedNumbers("
                + Arrays.toString(inputs[i])
                + ")="
                + got
                + " want "
                + Arrays.toString(wants[i])); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
