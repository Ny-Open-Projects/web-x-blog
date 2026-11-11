// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc455 { // 定义类型
  int findContentChildren(int[] g, int[] s) { // 定义函数/方法 findContentChildren
    Arrays.sort(g);
    Arrays.sort(s); // 排序
    int child = 0, cookie = 0; // 把 0, cookie 赋值为 0 存入 子节点
    while (child < g.length && cookie < s.length) { // 循环，直到不满足「子节点 小于 g.长度 且 cookie 小于 字符串.长度」
      if (s[cookie] >= g[child]) child++; // 若 字符串[cookie] 不低于 g[子节点]) 子节点 加一 ;
      cookie++; // cookie 加一
    }
    return child; // 返回 子节点
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc455 s = new Lc455(); // 把 new Lc455(); 写入 Lc455 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.findContentChildren(new int[] {1, 2, 3}, new int[] {1, 1}) != 1) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.findContentChildren(new int[] {1, 2}, new int[] {1, 2, 3}) != 2) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
