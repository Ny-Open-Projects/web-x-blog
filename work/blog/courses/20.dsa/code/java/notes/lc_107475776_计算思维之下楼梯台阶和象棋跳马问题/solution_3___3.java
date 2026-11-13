// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

// 象棋跳马问题：从 (0,0) 跳到 (8,4)，只允许向右的四种马步（方案3 枚举）
class Main { // 定义类型
  static final int[] DX = {1, 2, 2, 1}; // 把 {1, 2, 2, 1}; 写入 static final int[] DX
  static final int[] DY = {2, 1, -1, -2}; // 把 {2, 1, 减 1, 减 2}; 写入 static final int[] DY

  static int horseJumpCount(int gx, int gy) { // 定义函数/方法 horseJumpCount
    int[] count = {0}; // 把 {0}; 写入 int[] count
    dfs(0, 0, gx, gy, count); // dfs(0, 0, gx, gy, 计数);
    return count[0]; // 返回 计数[0]
  }

  static void dfs(int x, int y, int gx, int gy, int[] count) { // 定义函数/方法 dfs
    if (x == gx && y == gy) { // 若 x 等于 gx 且 y 等于 gy
      count[0]++; // 计数[0] 加一 ;
      return; // return;
    }
    for (int k = 0; k < 4; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
      int nx = x + DX[k], ny = y + DY[k]; // 把 x 加 DX[下标 k], ny 赋值为 y 加 DY[下标 k] 存入 nx
      if (0 <= nx && nx <= 8 && 0 <= ny && ny <= 4) { // 若 0 不超过 nx 且 nx 不超过 8 且 0 不超过 ny 且 ny 不超过 4
        dfs(nx, ny, gx, gy, count); // dfs(nx, ny, gx, gy, 计数);
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int normal = horseJumpCount(8, 4); // (0,0)->(8,4)
    int boundary = horseJumpCount(0, 0); // 起点即终点，只有 1 种方案
    boolean ok = true; // 把 true; 写入 boolean ok
    if (normal != 37) { // 若 normal 不等于 37
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL horseJumpCount(8,4)=" + normal + " want 37"); // 打印输出
    }
    if (boundary != 1) { // 若 boundary 不等于 1
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL horseJumpCount(0,0)=" + boundary + " want 1"); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
