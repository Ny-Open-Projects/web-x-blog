// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc113548046_solution11 { // 定义类型
  int[] parent; // int[] parent;

  List<Integer> bfs(int[][] graph, int start) { // 定义函数/方法 bfs
    int n = graph.length; // 把 graph.长度 存入 元素个数
    String[] status = new String[n]; // 把 new String[元素个数]; 写入 String[] status
    for (int i = 0; i < n; i++) status[i] = "UNDISCOVERED"; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    parent = new int[n]; // 把 new int[元素个数]; 写入 parent
    for (int i = 0; i < n; i++) parent[i] = -1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    List<Integer> order =
        new ArrayList<Integer>(); // 把 new ArrayList 小于 Integer 超过 (); 写入 List<Integer> order
    ArrayDeque<Integer> q =
        new ArrayDeque<Integer>(); // 把 new ArrayDeque 小于 Integer 超过 (); 写入 ArrayDeque<Integer> q
    q.add(start); // 节点 追加 起点);
    status[start] = "DISCOVERED"; // 把 「DISCOVERED」; 写入 status[start]
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int v = q.poll(); // 把 节点.poll() 存入 值
      order.add(v); // order 追加 值);
      for (int u : graph[v]) { // for (int 节点 u : graph[值]) {
        if (status[u].equals("UNDISCOVERED")) { // 若 status[节点 u].equals(「UNDISCOVERED」
          status[u] = "DISCOVERED"; // 把 「DISCOVERED」; 写入 status[u]
          parent[u] = v; // 把 值; 写入 parent[u]
          q.add(u); // 节点 追加 节点 u);
        }
      }
      status[v] = "VISITED"; // 把 「VISITED」; 写入 status[v]
    }
    return order; // 返回 order
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc113548046_solution11 s =
        new lc113548046_solution11(); // 把 new lc113548046_solution11(); 写入 lc113548046_solution11 s
    int[][] graph = {{1, 2}, {0, 3, 4}, {0, 5}, {1}, {1}, {2}};
    List<Integer> order = s.bfs(graph, 0); // 把 字符串.bfs(graph, 0); 写入 List<Integer> order
    boolean ok = true; // 把 true; 写入 boolean ok
    List<Integer> want =
        Arrays.asList(0, 1, 2, 3, 4, 5); // 把 Arrays.asList(0, 1, 2, 3, 4, 5); 写入 List<Integer> want
    if (!order.equals(want)) {
      ok = false;
      System.out.println("FAIL order " + order);
    }
    int[] wantP = {-1, 0, 0, 1, 1, 2}; // 把 { 减 1, 0, 0, 1, 1, 2}; 写入 int[] wantP
    for (int i = 0; i < wantP.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wantP.长度 就继续
      if (s.parent[i] != wantP[i]) {
        ok = false;
        System.out.println("FAIL parent " + i);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
