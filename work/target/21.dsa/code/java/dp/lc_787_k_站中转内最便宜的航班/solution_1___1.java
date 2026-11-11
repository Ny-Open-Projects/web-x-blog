// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc787_solution { // 定义类型
  int findCheapestPrice(
      int n, int[][] flights, int src, int dst, int k) { // 定义函数/方法 findCheapestPrice
    int INF = 1 << 29; // 把 1 小于 小于 29 存入 INF
    int[] dist = new int[n]; // 把 new int[元素个数]; 写入 int[] dist
    Arrays.fill(dist, INF); // Arrays.fill(dist, INF);
    dist[src] = 0; // 把 0; 写入 dist[src]
    for (int iter = 0; iter < k + 1; iter++) { // 让 iter 从 0 开始计数，iter 小于 下标 k 加 1 就继续
      int[] prev = dist.clone(); // 把 dist.clone(); 写入 int[] prev
      for (int[] f : flights) { // for (int[] f : flights) {
        int frm = f[0], to = f[1], price = f[2]; // 把 f[0], to 赋值为 f[1], price 赋值为 f[2] 存入 frm
        if (prev[frm] != INF
            && prev[frm] + price < dist[to]) { // 若 前一个[frm] 不等于 INF 且 前一个[frm] 加 price 小于 dist[to]
          dist[to] = prev[frm] + price; // 把 前一个[frm] 加 price; 写入 dist[to]
        }
      }
    }
    return dist[dst] == INF ? -1 : dist[dst]; // 返回 dist[dst] 等于 INF ? 减 1 : dist[dst]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc787_solution s = new lc787_solution(); // 把 new lc787_solution(); 写入 lc787_solution s
    int[][][] flightsCases = { // 把 { 写入 int[][][] flightsCases
      {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}},
      {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}},
      {{0, 1, 100}} // {{0,1,100}}
    };
    int[][] params = { // 把 { 写入 int[][] params
      {4, 0, 3, 1},
      {4, 0, 1, 0},
      {3, 0, 2, 1} // {3, 0, 2, 1}
    };
    int[] wants = {700, 100, -1}; // 把 {700, 100, 减 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < wants.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants.长度 就继续
      int got =
          s.findCheapestPrice(
              params[i][0], flightsCases[i], params[i][1], params[i][2], params[i][3]);
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
