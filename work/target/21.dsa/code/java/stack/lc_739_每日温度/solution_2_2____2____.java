// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
package com.webfault.dsa; // 引入依赖

import java.util.ArrayDeque; // 引入依赖
import java.util.Deque; // 引入依赖

class DailyTemperaturesSol2 { // 定义类型
  public int[] dailyTemperatures(int[] temperatures) { // 定义函数/方法 dailyTemperatures
    int n = temperatures.length; // 把 temperatures.长度 存入 元素个数
    int[] ans = new int[n]; // 把 new int[元素个数]; 写入 int[] ans
    Deque<Integer> stack = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> stack
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
        int prevIndex = stack.pop(); // 把 栈 弹出 ) 存入 prevIndex
        ans[prevIndex] = i - prevIndex; // 把 下标 i 减 prevIndex; 写入 ans[prevIndex]
      }
      stack.push(i); // 把 下标 i 压入栈/数组尾部
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    DailyTemperaturesSol2 s =
        new DailyTemperaturesSol2(); // 把 new DailyTemperaturesSol2(); 写入 DailyTemperaturesSol2 s
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{73, 74, 75, 71, 69, 72, 76, 73}, {1, 1, 4, 2, 1, 1, 0, 0}},
      {{30, 40, 50, 60}, {1, 1, 1, 0}},
      {{30, 60, 90}, {1, 1, 0}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got = s.dailyTemperatures(c[0]); // 把 字符串.dailyTemperatures(字符[0]); 写入 int[] got
      if (!eqArr(got, c[1])) { // 若 取反 eqArr(got, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL dailyTemperatures("
                + arrStr(c[0])
                + ")="
                + arrStr(got)
                + " want "
                + arrStr(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean eqArr(int[] a, int[] b) { // 定义函数/方法 eqArr
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (int i = 0; i < a.length; i++)
      if (a[i] != b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  static String arrStr(int[] a) { // 定义函数/方法 arrStr
    StringBuilder sb = new StringBuilder("["); // 把 new StringBuilder(「[」); 写入 StringBuilder sb
    for (int i = 0; i < a.length; i++) {
      if (i > 0) sb.append(",");
      sb.append(a[i]);
    } // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    sb.append("]"); // 把 「]」 追加到列表尾部
    return sb.toString(); // 返回 sb.toString()
  }
}
