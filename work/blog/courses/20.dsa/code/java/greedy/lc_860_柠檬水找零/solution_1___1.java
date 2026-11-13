// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  boolean lemonadeChange(int[] bills) { // 定义函数/方法 lemonadeChange
    int five = 0, ten = 0; // 把 0, ten 赋值为 0 存入 five
    for (int bill : bills) { // for (int bill : bills) {
      if (bill == 5) { // 若 bill 等于 5
        five++; // five 加一
      } else if (bill == 10) { // 否则，若 bill 等于 10
        if (five == 0) return false; // 若 five 等于 0，直接返回 false
        five--; // five 减一
        ten++; // ten 加一
      } else { // 否则
        if (ten > 0 && five > 0) { // 若 ten 超过 0 且 five 超过 0
          ten--; // ten 减一
          five--; // five 减一
        } else if (five >= 3) { // 否则，若 five 不低于 3
          five -= 3; // five累减 3
        } else { // 否则
          return false; // 返回 false
        }
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!s.lemonadeChange(new int[] {5, 5, 5, 10, 20})) {
      ok = false;
      System.out.println("FAIL case1");
    }
    if (s.lemonadeChange(new int[] {5, 5, 10, 10, 20})) {
      ok = false;
      System.out.println("FAIL case2");
    }
    if (!s.lemonadeChange(new int[] {5, 5, 5, 5, 5, 5, 20})) {
      ok = false;
      System.out.println("FAIL case3");
    }
    if (s.lemonadeChange(new int[] {10})) {
      ok = false;
      System.out.println("FAIL case4");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
