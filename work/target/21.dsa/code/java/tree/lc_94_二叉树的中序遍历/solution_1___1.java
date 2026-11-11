// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

/** LeetCode 94. 二叉树的中序遍历 方案1：递归中序（对齐博客 Ts/Python 版算法：left → node → right）。 */
class lc94_solution_1 { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode() { // TreeNode() {
    }

    TreeNode(int v) { // TreeNode(int 值) {
      this.val = v; // 把 值; 写入 值
    }
  }

  static List<Integer> inorderTraversal(TreeNode root) { // 定义函数/方法 inorderTraversal
    List<Integer> result =
        new ArrayList<Integer>(); // 把 new ArrayList 小于 Integer 超过 (); 写入 List<Integer> result
    inorderHandler(root, result); // inorderHandler(根节点, 结果);
    return result; // 返回 结果
  }

  static void inorderHandler(TreeNode root, List<Integer> result) { // 定义函数/方法 inorderHandler
    if (root == null) { // 若 根节点 等于 null
      return; // return;
    }
    inorderHandler(root.left, result); // inorderHandler(根节点.左边界, 结果);
    result.add(root.val); // 结果 追加 根节点.值);
    inorderHandler(root.right, result); // inorderHandler(根节点.右边界, 结果);
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals == null
        || vals.length == 0
        || vals[0] == null) { // 若 vals 等于 null 或 vals.长度 等于 0 或 vals[0] 等于 null
      return null; // 返回 null
    }
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    List<TreeNode> q =
        new ArrayList<TreeNode>(); // 把 new ArrayList 小于 TreeNode 超过 (); 写入 List<TreeNode> q
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (i < vals.length) { // 循环，直到不满足「下标 i 小于 vals.长度」
      TreeNode node = q.remove(0); // 把 节点 弹出 0); 写入 TreeNode node
      if (vals[i] != null) { // 若 vals[下标 i] 不等于 null
        node.left = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 左边界
        q.add(node.left); // 节点 追加 节点.左边界);
      }
      i++; // 下标 i 加一
      if (i < vals.length) { // 若 下标 i 小于 vals.长度
        if (vals[i] != null) { // 若 vals[下标 i] 不等于 null
          node.right = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 右边界
          q.add(node.right); // 节点 追加 节点.右边界);
        }
        i++; // 下标 i 加一
      }
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!inorderTraversal(null).isEmpty()) { // 若 取反 inorderTraversal(null).isEmpty(
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL inorderTraversal(null) 非空"); // 打印输出
    }
    TreeNode t1 = buildTree(new Integer[] {1, null, 2, null, 3});
    if (!inorderTraversal(t1)
        .equals(List.of(1, 2, 3))) { // 若 取反 inorderTraversal(t1).equals(List.of(1, 2, 3
      ok = false; // 把 false; 写入 ok
      System.out.println(
          "FAIL inorderTraversal(1,null,2,null,3)="
              + inorderTraversal(t1)
              + " want [1, 2, 3]"); // 打印输出
    }
    TreeNode t2 =
        buildTree(
            new Integer[] {1, 2, 3, 4}); // 把 buildTree(new Integer[] {1, 2, 3, 4}); 写入 TreeNode t2
    if (!inorderTraversal(t2)
        .equals(List.of(4, 2, 1, 3))) { // 若 取反 inorderTraversal(t2).equals(List.of(4, 2, 1, 3
      ok = false; // 把 false; 写入 ok
      System.out.println(
          "FAIL inorderTraversal(1,2,3,4)=" + inorderTraversal(t2) + " want [4, 2, 1, 3]"); // 打印输出
    }
    TreeNode t3 = buildTree(new Integer[] {1}); // 把 buildTree(new Integer[] {1}); 写入 TreeNode t3
    if (!inorderTraversal(t3).equals(List.of(1))) { // 若 取反 inorderTraversal(t3).equals(List.of(1
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL inorderTraversal(1)=" + inorderTraversal(t3) + " want [1]"); // 打印输出
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
