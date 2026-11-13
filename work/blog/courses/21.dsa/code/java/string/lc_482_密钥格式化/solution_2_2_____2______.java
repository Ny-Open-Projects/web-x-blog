// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public String licenseKeyFormatting(String s, int k) { // 定义函数/方法 licenseKeyFormatting
    s = s.replace("-", "").toUpperCase(); // 把 字符串.replace(「 减 」, 「 减 」).toUpperCase(); 写入 字符串
    StringBuilder result = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder result
    for (int i = s.length() - 1; i >= 0; i--) { // 让 下标 i 从 字符串.长度() 减 1 开始计数，下标 i 不低于 0 就继续
      result.append(s.charAt(i)); // 把 字符串 取字符 下标 i 追加到列表尾部
      if ((result.length() - 1) % k == k - 1 && i > 0) result.append("-");
    }
    return result.reverse().toString(); // 返回 结果.reverse().toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] ss = {"abc", "5F3Z-2we-9w"}; // 把 {「abc」, 「abc」}; 写入 String[] ss
    int[] ks = {1, 4}; // 把 {1, 4}; 写入 int[] ks
    String[] wants = {"A-B-C", "5F-3Z2-WE9W"}; // 把 {「A 减 B 减 C」, 「A 减 B 减 C」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ss.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ss.长度 就继续
      String got =
          s.licenseKeyFormatting(
              ss[i], ks[i]); // 把 字符串.licenseKeyFormatting(ss[下标 i], ks[下标 i]) 存入 got
      if (!got.equals(wants[i])) {
        ok = false;
        System.out.println("FAIL " + ss[i] + "," + ks[i] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
