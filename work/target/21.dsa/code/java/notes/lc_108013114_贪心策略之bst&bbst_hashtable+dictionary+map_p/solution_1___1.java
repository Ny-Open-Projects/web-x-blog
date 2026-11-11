// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc108013114_solution11 { // 定义类型
  static class BST { // static class BST {
    class Node { // 定义类型
      int val; // int 值;
      Node left, right; // Node 左边界, 右边界;

      Node(int v) {
        val = v;
      } // 把 值; } 写入 Node(int v) { val
    }

    Node root; // Node 根节点;

    void insert(int val) { // 定义函数/方法 insert
      if (root == null) {
        root = new Node(val);
        return;
      } // 若 根节点 等于 null) { 根节点 赋值为 new Node(值); return; }
      Node cur = root; // 把 根节点; 写入 Node cur
      while (true) { // 循环，直到不满足「true」
        if (val < cur.val) { // 若 值 小于 当前值.值
          if (cur.left == null) {
            cur.left = new Node(val);
            break;
          } // 若 当前值.左边界 等于 null) { 当前值.左边界 赋值为 new Node(值); break; }
          cur = cur.left; // 把 当前值.左边界; 写入 当前值
        } else if (val > cur.val) { // 否则，若 值 超过 当前值.值
          if (cur.right == null) {
            cur.right = new Node(val);
            break;
          } // 若 当前值.右边界 等于 null) { 当前值.右边界 赋值为 new Node(值); break; }
          cur = cur.right; // 把 当前值.右边界; 写入 当前值
        } else break; // 否则
      }
    }

    boolean search(int val) { // 定义函数/方法 search
      Node cur = root; // 把 根节点; 写入 Node cur
      while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
        if (val == cur.val) return true; // 若 值 等于 当前值.值，直接返回 true
        cur = (val < cur.val) ? cur.left : cur.right; // 把 (值 小于 当前值.值) ? 当前值.左边界 : 当前值.右边界; 写入 当前值
      }
      return false; // 返回 false
    }
  }

  static int kruskalMst(int[][] edges) { // 定义函数/方法 kruskalMst
    Map<Integer, Integer> parent =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> parent
    class UF { // 定义类型
      int find(int x) { // 定义函数/方法 find
        parent.putIfAbsent(x, x); // parent.putIfAbsent(x, x);
        while (parent.get(x) != x) { // 循环，直到不满足「parent 查找 x) 不等于 x」
          int p = parent.get(x); // 把 parent 查找 x) 存入 节点
          parent.put(x, parent.get(p)); // parent.put(x, parent 查找 节点));
          x = p; // 把 节点; 写入 x
        }
        return x; // 返回 x
      }

      boolean union(int a, int b) { // 定义函数/方法 union
        int ra = find(a), rb = find(b); // 把 find(数组), rb 赋值为 find(b) 存入 ra
        if (ra == rb) return false; // 若 ra 等于 rb，直接返回 false
        parent.put(ra, rb); // parent.put(ra, rb);
        return true; // 返回 true
      }
    }
    UF uf = new UF(); // 把 new UF(); 写入 UF uf
    Arrays.sort(edges, Comparator.comparingInt(e -> e[2])); // 排序
    int total = 0; // 把 0 存入 总和
    for (int[] e : edges) { // for (int[] e : 边集) {
      if (uf.union(e[0], e[1])) total += e[2]; // 若 uf.union(e[0], e[1])) 总和 累加 e[2];
    }
    return total; // 返回 总和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    BST bst = new BST(); // 把 new BST(); 写入 BST bst
    for (int v : new int[] {5, 3, 7, 1, 9})
      bst.insert(v); // for (int 值 : new int[]{5, 3, 7, 1, 9}) bst 插入 值);
    boolean s7 = bst.search(7); // 把 bst.search(7); 写入 boolean s7
    boolean s4 = bst.search(4); // 把 bst.search(4); 写入 boolean s4
    int mst = kruskalMst(new int[][] {{0, 1, 4}, {0, 2, 3}, {1, 2, 1}, {1, 3, 2}});
    if (s7 != true) {
      System.out.println("FAIL search7");
      throw new RuntimeException("FAILED");
    }
    if (s4 != false) {
      System.out.println("FAIL search4");
      throw new RuntimeException("FAILED");
    }
    if (mst != 6) {
      System.out.println("FAIL mst " + mst);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
