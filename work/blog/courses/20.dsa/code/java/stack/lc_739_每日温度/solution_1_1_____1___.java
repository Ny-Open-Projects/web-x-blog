// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
package com.webfault.dsa; // 引入依赖

class DailyTemperaturesSol1 { // 定义类型
  public int[] dailyTemperatures(int[] temperatures) { // 定义函数/方法 dailyTemperatures
    int length = temperatures.length; // 把 temperatures.长度 存入 长度
    int[] ans = new int[length]; // 把 new int[长度]; 写入 int[] ans
    int[] next = new int[101]; // 把 new int[101]; 写入 int[] next
    for (int i = 0; i < 101; i++) next[i] = Integer.MAX_VALUE; // 让 下标 i 从 0 开始计数，下标 i 小于 101 就继续
    for (int i = length - 1; i >= 0; i--) { // 让 下标 i 从 长度 减 1 开始计数，下标 i 不低于 0 就继续
      int warmerIndex = Integer.MAX_VALUE; // 把 Integer.MAX_VALUE 存入 warmerIndex
      int t = temperatures[i]; // 把 temperatures[下标 i] 存入 另一字符串
      for (int temp = t + 1; temp < 101; temp++) { // 让 临时变量 从 另一字符串 加 1 开始计数，临时变量 小于 101 就继续
        if (next[temp] < warmerIndex) { // 若 下一个[临时变量] 小于 warmerIndex
          warmerIndex = next[temp]; // 把 下一个[临时变量]; 写入 warmerIndex
        }
      }
      if (warmerIndex < Integer.MAX_VALUE) { // 若 warmerIndex 小于 Integer.MAX_VALUE
        ans[i] = warmerIndex - i; // 把 warmerIndex 减 下标 i; 写入 ans[i]
      }
      next[t] = i; // 把 下标 i; 写入 next[t]
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    DailyTemperaturesSol1 s =
        new DailyTemperaturesSol1(); // 把 new DailyTemperaturesSol1(); 写入 DailyTemperaturesSol1 s
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
