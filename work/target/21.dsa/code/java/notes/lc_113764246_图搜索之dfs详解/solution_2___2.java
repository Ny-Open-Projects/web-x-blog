// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc113764246_solution22 { // 定义类型
  static List<Integer> topoSortDfs(List<List<Integer>> graph) { // 定义函数/方法 topoSortDfs
    int n = graph.size(); // 把 graph.大小() 存入 元素个数
    String[] status = new String[n]; // 把 new String[元素个数]; 写入 String[] status
    for (int i = 0; i < n; i++) status[i] = "UNDISCOVERED"; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    List<Integer> stack = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> stack
    class Vis { // 定义类型
      void visit(int v) { // 定义函数/方法 visit
        status[v] = "DISCOVERED"; // 把 「DISCOVERED」; 写入 status[v]
        for (int u : graph.get(v)) { // for (int 节点 u : graph 查找 值)) {
          if (status[u].equals("UNDISCOVERED"))
            visit(u); // 若 status[节点 u].equals(「UNDISCOVERED」)) visit(节点 u);
        }
        status[v] = "VISITED"; // 把 「VISITED」; 写入 status[v]
        stack.add(v); // 栈 追加 值);
      }
    }
    Vis vis = new Vis(); // 把 new Vis(); 写入 Vis vis
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (status[i].equals("UNDISCOVERED"))
        vis.visit(i); // 若 status[下标 i].equals(「UNDISCOVERED」)) vis.visit(下标 i);
    }
    Collections.reverse(stack); // 反转
    return stack; // 返回 栈
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<Integer>> graph =
        Arrays.asList(
            Arrays.asList(2),
            Arrays.asList(2),
            Arrays.asList(3),
            Arrays.asList(4),
            Arrays.asList(5),
            Arrays.asList()); // Arrays.asList());
    List<Integer> topo = topoSortDfs(graph); // 把 topoSortDfs(graph); 写入 List<Integer> topo
    List<Integer> expect =
        Arrays.asList(
            1, 0, 2, 3, 4, 5); // 把 Arrays.asList(1, 0, 2, 3, 4, 5); 写入 List<Integer> expect
    if (!topo.equals(expect)) { // 若 取反 topo.equals(expect
      System.out.println("FAIL " + topo); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
