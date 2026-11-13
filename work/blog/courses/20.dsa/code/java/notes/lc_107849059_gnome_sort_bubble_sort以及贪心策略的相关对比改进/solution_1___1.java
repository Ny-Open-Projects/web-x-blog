// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_1：Gnome Sort + Bubble Sort + 贪心找零
class Main { // 定义类型

  static int[] gnomeSort(int[] arr) { // 定义函数/方法 gnomeSort
    int i = 0; // 把 0 存入 下标 i
    while (i < arr.length) { // 循环，直到不满足「下标 i 小于 数组.长度」
      if (i == 0 || arr[i] >= arr[i - 1]) { // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]
        i += 1; // 下标 i累加 1
      } else { // 否则
        int t = arr[i - 1]; // 把 数组[下标 i 减 1] 存入 另一字符串
        arr[i - 1] = arr[i]; // 把 数组[下标 i]; 写入 arr[i - 1]
        arr[i] = t; // 把 另一字符串; 写入 arr[i]
        i -= 1; // 下标 i累减 1
      }
    }
    return arr; // 返回 数组
  }

  static int[] bubbleSort(int[] arr) { // 定义函数/方法 bubbleSort
    int[] a = arr.clone(); // 把 数组.clone(); 写入 int[] a
    boolean swapped = true; // 把 true; 写入 boolean swapped
    while (swapped) { // 循环，直到不满足「swapped」
      swapped = false; // 把 false; 写入 swapped
      for (int i = 0; i + 1 < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 加 1 小于 数组.长度 就继续
        if (a[i] > a[i + 1]) { // 若 数组[下标 i] 超过 数组[下标 i 加 1]
          int t = a[i]; // 把 数组[下标 i] 存入 另一字符串
          a[i] = a[i + 1]; // 把 数组[下标 i 加 1]; 写入 a[i]
          a[i + 1] = t; // 把 另一字符串; 写入 a[i + 1]
          swapped = true; // 把 true; 写入 swapped
        }
      }
    }
    return a; // 返回 数组
  }

  static int coinChange(int[] coins, int amount) { // 定义函数/方法 coinChange
    int[] cs = coins.clone(); // 把 硬币面额.clone(); 写入 int[] cs
    Arrays.sort(cs); // 排序
    int remaining = amount; // 把 目标金额 存入 remaining
    int count = 0; // 把 0 存入 计数
    for (int i = cs.length - 1; i >= 0; i--) { // 让 下标 i 从 cs.长度 减 1 开始计数，下标 i 不低于 0 就继续
      while (remaining >= cs[i]) { // 循环，直到不满足「remaining 不低于 cs[下标 i]」
        remaining -= cs[i]; // remaining累减 cs[下标 i]
        count += 1; // 计数累加 1
      }
    }
    return remaining == 0 ? count : -1; // 返回 remaining 等于 0 ? 计数 : 减 1
  }

  static boolean eqArr(int[] a, int[] b) { // 定义函数/方法 eqArr
    if (a.length != b.length) { // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] != b[i]) { // 若 数组[下标 i] 不等于 b[下标 i]
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }

  static String show(int[] a) { // 定义函数/方法 show
    return Arrays.toString(a); // 返回 Arrays.toString(数组)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] gnomeCases = { // 把 { 写入 int[][] gnomeCases
      {3, 2, 1}, {1, 1, 2, 0}, {} // {3, 2, 1}, {1, 1, 2, 0}, {}
    };
    int[][] gnomeWant = { // 把 { 写入 int[][] gnomeWant
      {1, 2, 3}, {0, 1, 1, 2}, {} // {1, 2, 3}, {0, 1, 1, 2}, {}
    };
    int[][] bubbleCases = { // 把 { 写入 int[][] bubbleCases
      {3, 2, 1}, {2, 2, 1}, {} // {3, 2, 1}, {2, 2, 1}, {}
    };
    int[][] bubbleWant = { // 把 { 写入 int[][] bubbleWant
      {1, 2, 3}, {1, 2, 2}, {} // {1, 2, 3}, {1, 2, 2}, {}
    };
    int[][] coinCoins = { // 把 { 写入 int[][] coinCoins
      {1, 5, 10, 25}, {2}, {1, 2, 5} // {1, 5, 10, 25}, {2}, {1, 2, 5}
    };
    int[] coinAmount = {63, 3, 11}; // 把 {63, 3, 11}; 写入 int[] coinAmount
    int[] coinWant = {6, -1, 3}; // 把 {6, 减 1, 3}; 写入 int[] coinWant

    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < gnomeCases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 gnomeCases.长度 就继续
      int[] got =
          gnomeSort(gnomeCases[i].clone()); // 把 gnomeSort(gnomeCases[下标 i].clone()); 写入 int[] got
      if (!eqArr(got, gnomeWant[i])) { // 若 取反 eqArr(got, gnomeWant[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL gnome_sort("
                + show(gnomeCases[i])
                + ")="
                + show(got) // 打印输出
                + " want "
                + show(gnomeWant[i])); // 加 「 want 」 加 show(gnomeWant[下标 i]));
      }
    }
    for (int i = 0; i < bubbleCases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 bubbleCases.长度 就继续
      int[] got = bubbleSort(bubbleCases[i]); // 把 bubbleSort(bubbleCases[下标 i]); 写入 int[] got
      if (!eqArr(got, bubbleWant[i])) { // 若 取反 eqArr(got, bubbleWant[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL bubble_sort("
                + show(bubbleCases[i])
                + ")="
                + show(got) // 打印输出
                + " want "
                + show(bubbleWant[i])); // 加 「 want 」 加 show(bubbleWant[下标 i]));
      }
    }
    for (int i = 0; i < coinAmount.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 coinAmount.长度 就继续
      int got =
          coinChange(
              coinCoins[i],
              coinAmount[i]); // 把 coinChange(coinCoins[下标 i], coinAmount[下标 i]) 存入 got
      if (got != coinWant[i]) { // 若 got 不等于 coinWant[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL coin_change("
                + show(coinCoins[i])
                + ", "
                + coinAmount[i] // 打印输出
                + ")="
                + got
                + " want "
                + coinWant[i]); // 把 「 加 got 加 」 want " 加 coinWant[下标 i]); 写入 + ")
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
