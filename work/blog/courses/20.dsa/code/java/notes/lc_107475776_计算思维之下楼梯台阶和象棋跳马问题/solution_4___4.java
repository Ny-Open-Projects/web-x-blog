// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

// 象棋跳马问题（方案4）：使用平行数组 dx/dy 描述四种马步
class Main { // 定义类型
  static int horseJumpCount(int gx, int gy) { // 定义函数/方法 horseJumpCount
    int[] dx = {1, 2, 2, 1}; // 把 {1, 2, 2, 1}; 写入 int[] dx
    int[] dy = {2, 1, -1, -2}; // 把 {2, 1, 减 1, 减 2}; 写入 int[] dy
    int[] count = {0}; // 把 {0}; 写入 int[] count
    jump(0, 0, gx, gy, dx, dy, count); // jump(0, 0, gx, gy, dx, dy, 计数);
    return count[0]; // 返回 计数[0]
  }

  static void jump(int x, int y, int gx, int gy, int[] dx, int[] dy, int[] count) { // 定义函数/方法 jump
    if (x == gx && y == gy) { // 若 x 等于 gx 且 y 等于 gy
      count[0]++; // 计数[0] 加一 ;
      return; // return;
    }
    for (int k = 0; k < 4; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
      int x1 = x + dx[k], y1 = y + dy[k]; // 把 x 加 dx[下标 k], y1 赋值为 y 加 dy[下标 k] 存入 x1
      if (x1 < 0 || x1 > 8 || y1 < 0 || y1 > 4) { // 若 x1 小于 0 或 x1 超过 8 或 y1 小于 0 或 y1 超过 4
        continue; // 跳过本轮，进入下一次
      }
      jump(x1, y1, gx, gy, dx, dy, count); // jump(x1, y1, gx, gy, dx, dy, 计数);
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
