// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc133651611 { // 定义类型
  static Map<Integer, List<Integer>> graph; // static Map 小于 Integer,List 小于 Integer 超过 超过 graph;

  static { // static {
    graph = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 graph
    graph.put(0, Arrays.asList(1, 2)); // graph.put(0,Arrays.asList(1,2));
    graph.put(1, Arrays.asList(2)); // graph.put(1,Arrays.asList(2));
    graph.put(2, Arrays.asList(0, 3)); // graph.put(2,Arrays.asList(0,3));
    graph.put(3, Arrays.asList(3)); // graph.put(3,Arrays.asList(3));
  }

  List<Integer> dfs(int start) { // 定义函数/方法 dfs
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    Set<Integer> visited = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> visited
    dfsRec(start, visited, res); // dfsRec(起点,已访问集合,结果);
    return res; // 返回 结果
  }

  void dfsRec(int n, Set<Integer> visited, List<Integer> res) { // 定义函数/方法 dfsRec
    res.add(n);
    visited.add(n); // 结果 追加 元素个数); 已访问集合 追加 元素个数);
    for (int c : graph.get(n)) if (!visited.contains(c)) dfsRec(c, visited, res);
  }

  List<Integer> bfs(int start) { // 定义函数/方法 bfs
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    Set<Integer> visited = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> visited
    Deque<Integer> q = new ArrayDeque<>();
    q.offer(start);
    visited.add(start);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int n = q.poll();
      res.add(n); // 把 节点.poll(); 结果 追加 元素个数) 存入 元素个数
      for (int c : graph.get(n))
        if (!visited.contains(c)) {
          visited.add(c);
          q.offer(c);
        }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc133651611 s = new Lc133651611(); // 把 new Lc133651611(); 写入 Lc133651611 s
    List<Integer> d = s.dfs(2); // 把 字符串.dfs(2); 写入 List<Integer> d
    List<Integer> b = s.bfs(2); // 把 字符串.bfs(2); 写入 List<Integer> b
    List<Integer> dw = Arrays.asList(2, 0, 1, 3); // 把 Arrays.asList(2,0,1,3); 写入 List<Integer> dw
    List<Integer> bw = Arrays.asList(2, 0, 3, 1); // 把 Arrays.asList(2,0,3,1); 写入 List<Integer> bw
    boolean ok = true; // 把 true; 写入 boolean ok
    if (d.size() != dw.size()) ok = false;
    else for (int i = 0; i < dw.size(); i++) if (!d.get(i).equals(dw.get(i))) ok = false;
    if (b.size() != bw.size()) ok = false;
    else for (int i = 0; i < bw.size(); i++) if (!b.get(i).equals(bw.get(i))) ok = false;
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
