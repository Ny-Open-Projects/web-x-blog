// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public int compareVersion(String version1, String version2) { // 定义函数/方法 compareVersion
    String[] v1 = version1.split("\\."); // 把 version1.split(「\.」); 写入 String[] v1
    String[] v2 = version2.split("\\."); // 把 version2.split(「\.」); 写入 String[] v2
    int len1 = v1.length, len2 = v2.length; // 把 v1.长度, len2 赋值为 v2.长度 存入 len1
    int maxLen = Math.max(len1, len2); // 把 Math.取较大值 len1, len2) 存入 maxLen
    for (int i = 0; i < maxLen; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 maxLen 就继续
      int num1 =
          i < len1
              ? Integer.parseInt(v1[i])
              : 0; // 把 下标 i 小于 len1 ? Integer.转整数(v1[下标 i]) : 0 存入 num1
      int num2 =
          i < len2
              ? Integer.parseInt(v2[i])
              : 0; // 把 下标 i 小于 len2 ? Integer.转整数(v2[下标 i]) : 0 存入 num2
      if (num1 < num2) return -1; // 若 num1 小于 num2，直接返回 减 1
      else if (num1 > num2) return 1; // 否则，若 num1 超过 num2) return 1;
    }
    return 0; // 返回 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[][] ins = {{"1.01", "1.001"}, {"1.0", "1.0.0"}, {"0.1", "1.1"}};
    int[] wants = {0, 0, -1}; // 把 {0,0, 减 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int got =
          s.compareVersion(
              ins[i][0], ins[i][1]); // 把 字符串.compareVersion(ins[下标 i][0], ins[下标 i][1]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL " + ins[i][0] + "," + ins[i][1] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
