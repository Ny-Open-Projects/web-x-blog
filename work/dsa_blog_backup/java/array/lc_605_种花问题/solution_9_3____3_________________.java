// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
package com.webfault.dsa; // 引入依赖

class lc605_solution933 { // 定义类型
  // canPlaceFlowers 忠实翻译 python ref solution_9_3____3_________________.py（贪心种植）
  public boolean canPlaceFlowers(int[] flowerbed, int n) { // 定义函数/方法 canPlaceFlowers
    int cnt = 0; // 把 0 存入 计数
    int m = flowerbed.length; // 把 flowerbed.长度 存入 映射表
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      if (flowerbed[i] == 0
          && (i == 0 || flowerbed[i - 1] == 0)
          && (i == m - 1 || flowerbed[i + 1] == 0)) {
        flowerbed[i] = 1; // 把 1; 写入 flowerbed[i]
        cnt++; // 计数 加一
        if (cnt >= n) { // 若 计数 不低于 元素个数
          return true; // 返回 true
        }
      }
    }
    return cnt >= n; // 返回 计数 不低于 元素个数
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc605_solution933 s =
        new lc605_solution933(); // 把 new lc605_solution933(); 写入 lc605_solution933 s
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new int[] {1, 0, 0, 0, 1}, 1, true},
      {new int[] {1, 0, 0, 0, 1}, 2, false},
      {new int[] {0}, 1, true},
      {new int[] {0}, 0, true},
      {new int[] {0, 0, 0, 0, 0}, 3, true},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      boolean got = s.canPlaceFlowers((int[]) c[0], (Integer) c[1]);
      boolean want = (Boolean) c[2]; // 把 (Boolean) 字符[2]; 写入 boolean want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL got " + got + " want " + want); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
