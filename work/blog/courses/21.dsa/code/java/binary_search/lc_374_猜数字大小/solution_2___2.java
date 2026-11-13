// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
package com.webfault.dsa; // 引入依赖

// 猜数字大小（方案2：迭代二分）
class Main { // 定义类型
  static int pick = 6; // 把 6; 写入 static int pick

  static int guess(int num) { // 定义函数/方法 guess
    if (num == pick) return 0; // 若 num 等于 pick，直接返回 0
    return num < pick ? 1 : -1; // 返回 num 小于 pick ? 1 : 减 1
  }

  static int guessNumber(int n) { // 定义函数/方法 guessNumber
    int low = 1, high = n; // 把 1, high 赋值为 元素个数 存入 low
    while (low <= high) { // 循环，直到不满足「low 不超过 high」
      int mid = low + (high - low) / 2; // 把 (low 加 high) 除以 2 存入 中点
      int res = guess(mid); // 把 guess(中点) 存入 结果
      if (res == 0) return mid; // 若 结果 等于 0，直接返回 中点
      if (res == 1) low = mid + 1; // 若 结果 等于 1) low 赋值为 中点 加 1;
      else high = mid - 1; // 否则
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {{10, 6}, {1, 1}, {10, 1}, {10, 10}, {2, 2}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      pick = c[1]; // 把 字符[1]; 写入 pick
      int got = guessNumber(c[0]); // 把 guessNumber(字符[0]) 存入 got
      if (got != c[1]) { // 若 got 不等于 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL guessNumber(n=" + c[0] + ", pick=" + c[1] + ")=" + got); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
