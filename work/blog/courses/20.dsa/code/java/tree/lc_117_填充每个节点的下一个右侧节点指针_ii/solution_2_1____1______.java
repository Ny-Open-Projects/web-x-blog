// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc117_solution_2_1____1______ { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    Node left, right, next; // Node 左边界, 右边界, 下一个;

    Node() {} // Node() {}

    Node(int v) {
      val = v;
    } // 把 值; } 写入 Node(int v) { val
  }

  static Node connect(Node root) { // 定义函数/方法 connect
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    Node head = root; // 把 根节点; 写入 Node head
    while (head != null) { // 循环，直到不满足「头节点 不等于 null」
      Node dummy = new Node(); // 把 new Node(); 写入 Node dummy
      Node tail = dummy; // 把 哨兵节点; 写入 Node tail
      Node cur = head; // 把 头节点; 写入 Node cur
      while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
        if (cur.left != null) {
          tail.next = cur.left;
          tail = tail.next;
        }
        if (cur.right != null) {
          tail.next = cur.right;
          tail = tail.next;
        }
        cur = cur.next; // 把 当前值.下一个; 写入 当前值
      }
      head = dummy.next; // 把 哨兵节点.下一个; 写入 头节点
    }
    return root; // 返回 根节点
  }

  static Node build(Integer[] vals) { // 定义函数/方法 build
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    Node root = new Node(vals[0]); // 把 new Node(vals[0]); 写入 Node root
    Deque<Node> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Node> q
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (i < vals.length && !q.isEmpty()) { // 循环，直到不满足「下标 i 小于 vals.长度 且 取反 节点.isEmpty(」
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

  static List<List<Integer>> chains(Node root) { // 定义函数/方法 chains
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    Node levelStart = root; // 把 根节点; 写入 Node levelStart
    while (levelStart != null) { // 循环，直到不满足「levelStart 不等于 null」
      List<Integer> vals = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> vals
      Node node = levelStart; // 把 levelStart; 写入 Node node
      while (node != null) {
        vals.add(node.val);
        node = node.next;
      } // 循环，直到不满足「节点 不等于 null) { vals 追加 节点.值); 节点 赋值为 节点.下一个; }」
      res.add(vals); // 结果 追加 vals);
      Node cur = levelStart; // 把 levelStart; 写入 Node cur
      levelStart = null; // 把 null; 写入 levelStart
      while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
        if (cur.left != null) {
          levelStart = cur.left;
          break;
        } // 若 当前值.左边界 不等于 null) { levelStart 赋值为 当前值.左边界; break; }
        if (cur.right != null) {
          levelStart = cur.right;
          break;
        } // 若 当前值.右边界 不等于 null) { levelStart 赋值为 当前值.右边界; break; }
        cur = cur.next; // 把 当前值.下一个; 写入 当前值
      }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {
        new Integer[] {1, 2, 3, 4, 5, null, 7},
        Arrays.asList(Arrays.asList(1), Arrays.asList(2, 3), Arrays.asList(4, 5, 7))
      },
      {null, Arrays.asList()},
      {new Integer[] {1}, Arrays.asList(Arrays.asList(1))},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      Node root = c[0] == null ? null : build((Integer[]) c[0]);
      connect(root); // connect(根节点);
      List<List<Integer>> got = chains(root); // 把 chains(根节点); 写入 List<List<Integer>> got
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
