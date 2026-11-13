// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
package com.webfault.dsa; // 引入依赖

import java.util.HashSet; // 引入依赖
import java.util.Set; // 引入依赖

// 只出现一次的数字：基于集合的解法（方案2）。
// 出现则移除，未出现则加入，最后集合里剩下的即为答案。忠实翻译自 Python 参考实现。
class solution222Set { // 定义类型
  static int singleNumber(int[] nums) { // 定义函数/方法 singleNumber
    Set<Integer> set = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> set
    for (int num : nums) { // for (int num : 数组) {
      if (set.contains(num)) { // 若 set 是否包含 num
        set.remove(num); // set 弹出 num);
      } else { // 否则
        set.add(num); // set 追加 num);
      }
    }
    return set.iterator().next(); // 返回 set.iterator().下一个()
  }

  static boolean selfCheck() { // 定义函数/方法 selfCheck
    // (args, expected) 取自 _tools/correctness_check.py 的 lc_136_只出现一次的数字 cases
    int[][] cases = { // 把 { 写入 int[][] cases
      {2, 2, 1},
      {4, 1, 2, 1, 2},
      {1},
    };
    int[] wants = {1, 4, 1}; // 把 {1, 4, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int got = singleNumber(cases[k]); // 把 singleNumber(cases[下标 k]) 存入 got
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case" + (k + 1) + ": got " + got + " want " + wants[k]); // 打印输出
      }
    }
    return ok; // 返回 ok
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!selfCheck()) { // 若 取反 selfCheck(
      System.out.println("FAIL"); // 打印输出
      System.exit(1); // System.exit(1);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
