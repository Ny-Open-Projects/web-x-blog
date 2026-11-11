// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
package com.webfault.dsa; // 引入依赖

class lc541_solution111 { // 定义类型
  String reverseStr(String s, int k) { // 定义函数/方法 reverseStr
    char[] arr = s.toCharArray(); // 把 字符串.toCharArray(); 写入 char[] arr
    int n = arr.length; // 把 数组.长度 存入 元素个数
    for (int i = 0; i < n; i += 2 * k) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      int left = i; // 把 下标 i 存入 左边界
      int right = Math.min(i + k - 1, n - 1); // 把 Math.取较小值 下标 i 加 下标 k 减 1, 元素个数 减 1) 存入 右边界
      while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
        char temp = arr[left]; // 把 数组[左边界]; 写入 char temp
        arr[left] = arr[right]; // 把 数组[右边界]; 写入 arr[left]
        arr[right] = temp; // 把 临时变量; 写入 arr[right]
        left++; // 左边界 加一
        right--; // 右边界 减一
      }
    }
    return new String(arr); // 返回 new String(数组)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc541_solution111 s =
        new lc541_solution111(); // 把 new lc541_solution111(); 写入 lc541_solution111 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!s.reverseStr("abc", 1).equals("abc")) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (!s.reverseStr("abcdefg", 2).equals("bacdfeg")) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (!s.reverseStr("abcd", 2).equals("bacd")) {
      ok = false;
      System.out.println("FAIL3");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
