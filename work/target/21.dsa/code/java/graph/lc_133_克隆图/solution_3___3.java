// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc133_solution33 { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    List<Node> neighbors = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Node> neighbors

    Node(int v) {
      val = v;
    } // 把 值; } 写入 Node(int v) { val
  }

  public Node cloneGraph(Node node) { // 定义函数/方法 cloneGraph
    if (node == null) return null; // 若 节点 等于 null，直接返回 null
    Map<Node, Node> visited = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Node, Node> visited
    return dfs(node, visited); // 返回 dfs(节点, 已访问集合)
  }

  private Node dfs(Node n, Map<Node, Node> visited) { // 定义函数/方法 dfs
    if (visited.containsKey(n))
      return visited.get(n); // 若 已访问集合.containsKey(元素个数)，直接返回 已访问集合 查找 元素个数)
    Node clone = new Node(n.val); // 把 new Node(元素个数.值); 写入 Node clone
    visited.put(n, clone); // 已访问集合.put(元素个数, clone);
    for (Node ne : n.neighbors) { // for (Node ne : 元素个数.neighbors) {
      clone.neighbors.add(dfs(ne, visited)); // clone.neighbors 追加 dfs(ne, 已访问集合));
    }
    return clone; // 返回 clone
  }

  static Map<Integer, List<Integer>> signature(Node node) {
    Map<Integer, List<Integer>> sig =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, List<Integer>> sig
    Set<Integer> seen = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> seen
    sigDfs(node, sig, seen); // sigDfs(节点, sig, 已见集合);
    return sig; // 返回 sig
  }

  static void sigDfs(Node n, Map<Integer, List<Integer>> sig, Set<Integer> seen) { // 定义函数/方法 sigDfs
    if (seen.contains(n.val)) return; // 若 已见集合 是否包含 元素个数.值)) return;
    seen.add(n.val); // 已见集合 追加 元素个数.值);
    List<Integer> nb = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> nb
    for (Node x : n.neighbors) nb.add(x.val); // for (Node x : 元素个数.neighbors) nb 追加 x.值);
    Collections.sort(nb); // 排序
    sig.put(n.val, nb); // sig.put(元素个数.值, nb);
    for (Node x : n.neighbors)
      sigDfs(x, sig, seen); // for (Node x : 元素个数.neighbors) sigDfs(x, sig, 已见集合);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Node n1 = new Node(1), n2 = new Node(2), n3 = new Node(3), n4 = new Node(4);
    n1.neighbors = Arrays.asList(n2, n4); // 把 Arrays.asList(n2, n4); 写入 n1.neighbors
    n2.neighbors = Arrays.asList(n1, n3); // 把 Arrays.asList(n1, n3); 写入 n2.neighbors
    n3.neighbors = Arrays.asList(n2, n4); // 把 Arrays.asList(n2, n4); 写入 n3.neighbors
    n4.neighbors = Arrays.asList(n1, n3); // 把 Arrays.asList(n1, n3); 写入 n4.neighbors
    lc133_solution33 s = new lc133_solution33(); // 把 new lc133_solution33(); 写入 lc133_solution33 s
    Node c = s.cloneGraph(n1); // 把 字符串.cloneGraph(n1); 写入 Node c
    Map<Integer, List<Integer>> got =
        signature(c); // 把 signature(字符); 写入 Map<Integer, List<Integer>> got
    Map<Integer, List<Integer>> want =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, List<Integer>> want
    want.put(1, Arrays.asList(2, 4)); // want.put(1, Arrays.asList(2, 4));
    want.put(2, Arrays.asList(1, 3)); // want.put(2, Arrays.asList(1, 3));
    want.put(3, Arrays.asList(2, 4)); // want.put(3, Arrays.asList(2, 4));
    want.put(4, Arrays.asList(1, 3)); // want.put(4, Arrays.asList(1, 3));
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL got " + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
