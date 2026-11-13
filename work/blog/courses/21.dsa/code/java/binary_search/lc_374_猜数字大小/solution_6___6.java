// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
package com.webfault.dsa; // 引入依赖

// 猜数字大小（方案6：迭代二分，guess 先行判定大小）
class Main { // 定义类型
  static int pick = 6; // 把 6; 写入 static int pick

  static int guess(int num) { // 定义函数/方法 guess
    if (num > pick) return -1; // 若 num 超过 pick，直接返回 减 1
    else if (num < pick) return 1; // 否则，若 num 小于 pick) return 1;
    return 0; // 返回 0
  }

  static int guessNumber(int n) { // 定义函数/方法 guessNumber
    int left = 1, right = n; // 把 1, 右边界 赋值为 元素个数 存入 左边界
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      int mid = left + (right - left) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
      int g = guess(mid); // 把 guess(中点) 存入 g
      if (g == 0) return mid; // 若 g 等于 0，直接返回 中点
      else if (g == 1) left = mid + 1; // 否则，若 g 等于 1) 左边界 赋值为 中点 加 1;
      else right = mid - 1; // 否则
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
