// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
package com.webfault.dsa; // 引入依赖

class lc605_solution633 { // 定义类型
  // canPlaceFlowers 忠实翻译 python ref solution_6_3____3_________________.py（l/r 双指针）
  public boolean canPlaceFlowers(int[] flowerbed, int n) { // 定义函数/方法 canPlaceFlowers
    int l = -1; // 把 减 1 存入 左指针
    int r = 0; // 把 0 存入 右指针
    while (r <= flowerbed.length) { // 循环，直到不满足「右指针 不超过 flowerbed.长度」
      int rv =
          (r == flowerbed.length)
              ? 0
              : flowerbed[r]; // 把 (右指针 等于 flowerbed.长度) ? 0 : flowerbed[右指针] 存入 rv
      r++; // 右指针 加一
      if (rv == 1) { // 若 rv 等于 1
        l = r; // 把 右指针; 写入 左指针
      }
      if (r - l == 3) { // 若 右指针 减 左指针 等于 3
        n--; // 元素个数 减一
        l += 2; // 左指针累加 2
      }
    }
    return n <= 0; // 返回 元素个数 不超过 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc605_solution633 s =
        new lc605_solution633(); // 把 new lc605_solution633(); 写入 lc605_solution633 s
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
