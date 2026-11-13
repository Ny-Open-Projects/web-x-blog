// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package com.webfault.dsa; // 引入依赖

class notes108_me { // 定义类型
  int majorityElement(int[] arr) { // 定义函数/方法 majorityElement
    Integer candidate = null; // 把 null 存入 candidate
    int count = 0; // 把 0 存入 计数
    for (int num : arr) { // for (int num : 数组) {
      if (count == 0) candidate = num; // 若 计数 等于 0) candidate 赋值为 num;
      if (num == candidate) count++; // 若 num 等于 candidate) 计数 加一 ;
      else count--; // 否则
    }
    int cnt = 0; // 把 0 存入 计数
    for (int num : arr)
      if (num == candidate) cnt++; // 把 赋值为 candidate) 计数 加一 ; 写入 for (int num : arr) if (num
    if (cnt > arr.length / 2) return candidate; // 若 计数 超过 数组.长度 除以 2，直接返回 candidate
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    notes108_me s = new notes108_me(); // 把 new notes108_me(); 写入 notes108_me s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.majorityElement(new int[] {2, 2, 1, 1, 1, 1, 1}) != 1) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.majorityElement(new int[] {1, 2, 3}) != -1) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (s.majorityElement(new int[] {3, 3, 4}) != 3) {
      ok = false;
      System.out.println("FAIL3");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
