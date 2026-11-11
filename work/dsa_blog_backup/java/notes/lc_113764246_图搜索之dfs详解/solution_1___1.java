// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc113764246_solution11 { // 定义类型
  static int[] dTime, fTime, parent; // static int[] dTime, fTime, parent;
  static String[] status; // static String[] status;
  static Map<String, String> edges; // static Map 小于 String, String 超过 边集;
  static int clock; // static int clock;
  static List<List<Integer>> graph; // static List 小于 List 小于 Integer 超过 超过 graph;

  static void visit(int v) { // 定义函数/方法 visit
    clock++; // clock 加一
    dTime[v] = clock; // 把 clock; 写入 dTime[v]
    status[v] = "DISCOVERED"; // 把 「DISCOVERED」; 写入 status[v]
    for (int u : graph.get(v)) { // for (int 节点 u : graph 查找 值)) {
      if (status[u].equals("UNDISCOVERED")) { // 若 status[节点 u].equals(「UNDISCOVERED」
        edges.put(v + "-" + u, "TREE"); // 边集.put(值 加 「 减 」 加 节点 u, 「 减 」);
        parent[u] = v; // 把 值; 写入 parent[u]
        visit(u); // visit(节点 u);
      } else if (status[u].equals("DISCOVERED")) { // 否则，若 status[节点 u].equals(「DISCOVERED」
        edges.put(v + "-" + u, "BACKWARD"); // 边集.put(值 加 「 减 」 加 节点 u, 「 减 」);
      } else { // 否则
        edges.put(v + "-" + u, dTime[v] < dTime[u] ? "FORWARD" : "CROSS");
      }
    }
    clock++; // clock 加一
    fTime[v] = clock; // 把 clock; 写入 fTime[v]
    status[v] = "VISITED"; // 把 「VISITED」; 写入 status[v]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    graph =
        Arrays.asList(
            Arrays.asList(1, 5),
            Arrays.asList(2),
            Arrays.asList(),
            Arrays.asList(4),
            Arrays.asList(5, 6),
            Arrays.asList(1, 6),
            Arrays.asList()); // Arrays.asList());
    int n = graph.size(); // 把 graph.大小() 存入 元素个数
    dTime = new int[n]; // 把 new int[元素个数]; 写入 dTime
    fTime = new int[n]; // 把 new int[元素个数]; 写入 fTime
    parent = new int[n]; // 把 new int[元素个数]; 写入 parent
    status = new String[n]; // 把 new String[元素个数]; 写入 status
    edges = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 边集
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      status[i] = "UNDISCOVERED"; // 把 「UNDISCOVERED」; 写入 status[i]
      parent[i] = -1; // 把 减 1; 写入 parent[i]
    }
    clock = 0; // 把 0; 写入 clock
    visit(0); // visit(0);
    int[] expD = {1, 2, 3, 0, 0, 6, 7}; // 把 {1, 2, 3, 0, 0, 6, 7}; 写入 int[] expD
    int[] expF = {10, 5, 4, 0, 0, 9, 8}; // 把 {10, 5, 4, 0, 0, 9, 8}; 写入 int[] expF
    int[] expP = {-1, 0, 1, -1, -1, 0, 5}; // 把 { 减 1, 0, 1, 减 1, 减 1, 0, 5}; 写入 int[] expP
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (dTime[i] != expD[i] || fTime[i] != expF[i] || parent[i] != expP[i]) {
        System.out.println(
            "FAIL node " + i + " d=" + dTime[i] + " f=" + fTime[i] + " p=" + parent[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    if (!"TREE".equals(edges.get("0-1"))) {
      System.out.println("FAIL 0-1");
      throw new RuntimeException("FAILED");
    }
    if (!"TREE".equals(edges.get("1-2"))) {
      System.out.println("FAIL 1-2");
      throw new RuntimeException("FAILED");
    }
    if (!"TREE".equals(edges.get("0-5"))) {
      System.out.println("FAIL 0-5");
      throw new RuntimeException("FAILED");
    }
    if (!"CROSS".equals(edges.get("5-1"))) {
      System.out.println("FAIL 5-1 " + edges.get("5-1"));
      throw new RuntimeException("FAILED");
    }
    if (!"TREE".equals(edges.get("5-6"))) {
      System.out.println("FAIL 5-6");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
