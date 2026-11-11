package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖
import java.util.Map; // 引入依赖

// LeetCode 169. 多数元素。忠实翻译 Python 参考实现 ref_majorityElement：
// Counter(nums).most_common(1)[0][0]
class lc169_solution1 { // 定义类型
  int majorityElement(int[] nums) { // 定义函数/方法 majorityElement
    Map<Integer, Integer> cnt =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> cnt
    for (int v : nums) { // for (int 值 : 数组) {
      cnt.put(v, cnt.getOrDefault(v, 0) + 1); // 计数.put(值, 计数.getOrDefault(值, 0) 加 1);
    }
    int best = 0, bestCnt = -1; // 把 0, bestCnt 赋值为 减 1 存入 当前最优
    for (Map.Entry<Integer, Integer> e :
        cnt.entrySet()) { // for (Map.Entry 小于 Integer, Integer 超过 e : 计数.entrySet()) {
      if (e.getValue() > bestCnt) { // 若 e.getValue() 超过 bestCnt
        best = e.getKey(); // 把 e.getKey(); 写入 当前最优
        bestCnt = e.getValue(); // 把 e.getValue(); 写入 bestCnt
      }
    }
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_169_多数元素"]
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new int[] {3, 2, 3}, 3},
      {new int[] {2, 2, 1, 1, 1, 2, 2}, 2},
      {new int[] {1}, 1},
    };
    lc169_solution1 s = new lc169_solution1(); // 把 new lc169_solution1(); 写入 lc169_solution1 s
    boolean allOK = true; // 把 true; 写入 boolean allOK
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int got = s.majorityElement((int[]) c[0]); // 把 字符串.majorityElement((int[]) 字符[0]) 存入 got
      int want = (Integer) c[1]; // 把 (Integer) 字符[1] 存入 want
      if (got != want) { // 若 got 不等于 want
        allOK = false; // 把 false; 写入 allOK
        System.out.println("FAIL majorityElement = " + got + ", want " + want); // 打印输出
      }
    }
    if (!allOK) { // 若 取反 allOK
      throw new RuntimeException(
          "some cases FAILED"); // throw new RuntimeException(「some cases FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
