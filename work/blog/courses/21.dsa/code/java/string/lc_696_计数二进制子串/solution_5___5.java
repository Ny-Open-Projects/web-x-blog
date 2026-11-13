// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
package com.webfault.dsa; // 引入依赖

class lc695_solution5 { // 定义类型
  static int countBinarySubstrings3(String s) { // 定义函数/方法 countBinarySubstrings3
    int prev = 0, cur = 1, ans = 0; // 上一组、当前组、答案
    for (int i = 1; i < s.length(); i++) { // 从下标 1 扫描到末尾
      if (s.charAt(i) == s.charAt(i - 1)) { // 同组
        cur++;
      } else { // 换组
        ans += Math.min(prev, cur); // 结算上一对相邻组
        prev = cur;
        cur = 1;
      }
    }
    return ans + Math.min(prev, cur); // 结算最后一对
  }

  public static void main(String[] args) { // 程序入口：跑内嵌自测用例
    String[][] cases = {{"00110011", "6"}, {"10101", "4"}, {"0", "0"}, {"111000", "3"}};
    boolean ok = true;
    for (String[] c : cases) {
      int got = countBinarySubstrings3(c[0]);
      if (got != Integer.parseInt(c[1])) {
        ok = false;
        System.out.println("FAIL " + c[0] + "=" + got + " want " + c[1]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED");
    System.out.println("PASS");
  }
}
