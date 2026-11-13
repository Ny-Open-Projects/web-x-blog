// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc116_solution_2_1_____1_____ { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    Node left, right, next; // Node 左边界, 右边界, 下一个;

    Node(int v) {
      val = v;
    } // 把 值; } 写入 Node(int v) { val
  }

  public Node connect(Node root) { // 定义函数/方法 connect
    if (root == null) return root; // 若 根节点 等于 null，直接返回 根节点
    Deque<Node> Q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Node> Q
    Q.add(root); // Q 追加 根节点);
    while (!Q.isEmpty()) { // 循环，直到不满足「取反 Q.isEmpty(」
      int size = Q.size(); // 把 Q.大小() 存入 大小
      for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
        Node node = Q.poll(); // 把 Q.poll(); 写入 Node node
        if (i < size - 1) { // 若 下标 i 小于 大小 减 1
          node.next = Q.peek(); // 把 Q.peek(); 写入 下一个
        }
        if (node.left != null) Q.add(node.left); // 若 节点.左边界 不等于 null) Q 追加 节点.左边界);
        if (node.right != null) Q.add(node.right); // 若 节点.右边界 不等于 null) Q 追加 节点.右边界);
      }
    }
    return root; // 返回 根节点
  }

  static Node build(Integer[] a) { // 定义函数/方法 build
    if (a.length == 0 || a[0] == null) return null; // 若 数组.长度 等于 0 或 数组[0] 等于 null，直接返回 null
    Node root = new Node(a[0]); // 把 new Node(数组[0]); 写入 Node root
    Deque<Node> queue = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Node> queue
    queue.add(root); // 队列 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!queue.isEmpty() && i < a.length) { // 循环，直到不满足「取反 队列.isEmpty() 且 下标 i 小于 数组.长度」
      Node node = queue.poll(); // 把 队列.poll(); 写入 Node node
      if (i < a.length && a[i] != null) {
        node.left = new Node(a[i]);
        queue.add(node.left);
      }
      i++; // 下标 i 加一
      if (i < a.length && a[i] != null) {
        node.right = new Node(a[i]);
        queue.add(node.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  static List<List<Integer>> levelChains(Node root) { // 定义函数/方法 levelChains
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    Node cur = root; // 把 根节点; 写入 Node cur
    while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
      List<Integer> vals = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> vals
      Node node = cur; // 把 当前值; 写入 Node node
      while (node != null) { // 循环，直到不满足「节点 不等于 null」
        vals.add(node.val); // vals 追加 节点.值);
        node = node.next; // 把 节点.下一个; 写入 节点
      }
      res.add(vals); // 结果 追加 vals);
      cur = cur.left; // 把 当前值.左边界; 写入 当前值
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc116_solution_2_1_____1_____ s = new lc116_solution_2_1_____1_____();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {
        new Integer[] {1, 2, 3, 4, 5, 6, 7},
        Arrays.asList(Arrays.asList(1), Arrays.asList(2, 3), Arrays.asList(4, 5, 6, 7))
      },
      {new Integer[] {1}, Arrays.asList(Arrays.asList(1))},
      {null, Arrays.asList()},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      Node root = c[0] == null ? null : build((Integer[]) c[0]);
      s.connect(root); // 字符串.connect(根节点);
      List<List<Integer>> got = levelChains(root); // 把 levelChains(根节点); 写入 List<List<Integer>> got
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<List<Integer>> want = (List<List<Integer>>) c[1];
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL connect=" + got + " want " + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
