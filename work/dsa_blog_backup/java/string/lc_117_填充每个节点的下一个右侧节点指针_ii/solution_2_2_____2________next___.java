// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
// 引入依赖
import java.util.List; // 引入依赖

/** LeetCode 117. 填充每个节点的下一个右侧节点指针 II 方案2：使用已建立的 next 指针（O(1) 额外空间，逐层串接）。 */
class lc117_solution_2 { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    Node left, right, next; // Node 左边界, 右边界, 下一个;

    Node() { // Node() {
    }

    Node(int val) { // Node(int 值) {
      this.val = val; // 把 值; 写入 值
    }
  }

  static Node buildNode(Integer[] vals) { // 定义函数/方法 buildNode
    if (vals == null || vals.length == 0 || vals[0] == null)
      return null; // 若 vals 等于 null 或 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    Node root = new Node(vals[0]); // 把 new Node(vals[0]); 写入 Node root
    java.util.LinkedList<Node> q = new java.util.LinkedList<>();
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      Node node = q.poll(); // 把 节点.poll(); 写入 Node node
      if (i < vals.length && vals[i] != null) {
        node.left = new Node(vals[i]);
        q.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) {
        node.right = new Node(vals[i]);
        q.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  Node connect(Node root) { // 定义函数/方法 connect
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    Node leftmost = root; // 把 根节点; 写入 Node leftmost
    while (leftmost != null) { // 循环，直到不满足「leftmost 不等于 null」
      Node cur = leftmost; // 把 leftmost; 写入 Node cur
      Node nextStart = null; // 把 null; 写入 Node nextStart
      Node prev = null; // 把 null; 写入 Node prev
      while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
        Node[] kids = {cur.left, cur.right}; // 把 {当前值.左边界, 当前值.右边界}; 写入 Node[] kids
        for (Node ch : kids) { // for (Node 字符 : kids) {
          if (ch != null) { // 若 字符 不等于 null
            if (prev == null) { // 若 前一个 等于 null
              nextStart = ch; // 把 字符; 写入 nextStart
            } else { // 否则
              prev.next = ch; // 把 字符; 写入 下一个
            }
            prev = ch; // 把 字符; 写入 前一个
          }
        }
        cur = cur.next; // 把 当前值.下一个; 写入 当前值
      }
      leftmost = nextStart; // 把 nextStart; 写入 leftmost
    }
    return root; // 返回 根节点
  }

  static List<List<Integer>> collectLevels(Node root) { // 定义函数/方法 collectLevels
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    for (Node leftmost = root; leftmost != null; leftmost = leftmost.left) {
      List<Integer> level = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> level
      for (Node cur = leftmost; cur != null; cur = cur.next) {
        level.add(cur.val); // level 追加 当前值.值);
      }
      res.add(level); // 结果 追加 level);
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc117_solution_2 s = new lc117_solution_2(); // 把 new lc117_solution_2(); 写入 lc117_solution_2 s
    Node root = buildNode(new Integer[] {1, 2, 3, 4, 5, null, 7});
    s.connect(root); // 字符串.connect(根节点);
    List<List<Integer>> got =
        collectLevels(root); // 把 collectLevels(根节点); 写入 List<List<Integer>> got
    List<List<Integer>> want = List.of(List.of(1), List.of(2, 3), List.of(4, 5, 7));
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL connect=" + got + " want " + want); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    if (s.connect(null) != null) { // 若 字符串.connect(null) 不等于 null
      System.out.println("FAIL connect(null) != null"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    Node single = new Node(9); // 把 new Node(9); 写入 Node single
    s.connect(single); // 字符串.connect(single);
    if (!collectLevels(single)
        .equals(List.of(List.of(9)))) { // 若 取反 collectLevels(single).equals(List.of(List.of(9
      System.out.println("FAIL single"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
