// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Java 版（方案1：深度优先-贪心）

package com.webfault.dsa;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

class Lcp10S1 { // 非 public class：文件名可以与类名不同
  static class TreeNode { // 二叉树节点：val 为自身执行时间（double 承载并行节省的 0.5）
    double val;
    TreeNode left;
    TreeNode right;

    TreeNode(double val) {
      this.val = val;
    }
  }

  // 层序数组建树，null 表示空节点
  static TreeNode buildTree(List<Double> vals) {
    if (vals.isEmpty()) return null;
    TreeNode root = new TreeNode(vals.get(0));
    Deque<TreeNode> queue = new ArrayDeque<>(); // 队列里只放非空节点
    queue.add(root);
    int i = 1;
    while (!queue.isEmpty() && i < vals.size()) {
      TreeNode node = queue.poll(); // 出队一个父节点
      if (i < vals.size() && vals.get(i) != null) { // 左孩子
        node.left = new TreeNode(vals.get(i));
        queue.add(node.left);
      }
      i++;
      if (i < vals.size() && vals.get(i) != null) { // 右孩子
        node.right = new TreeNode(vals.get(i));
        queue.add(node.right);
      }
      i++;
    }
    return root;
  }

  // dfs 返回 [子树总耗时, 两台机器并行可节省的耗时]
  static double[] dfs(TreeNode root) {
    if (root == null) return new double[] {0.0, 0.0}; // 空子树：总耗时 0，节省 0
    double[] left = dfs(root.left);
    double[] right = dfs(root.right);
    double a = left[0], b = left[1]; // a: 左子树总耗时, b: 左子树已节省
    double c = right[0], d = right[1]; // c: 右子树总耗时, d: 右子树已节省
    double saved;
    if ((c - 2 * d <= a && a <= c) || (a - 2 * b <= c && c <= a)) {
      // 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
      saved = (a + c) / 2.0; // 浮点除法：总和为奇数时会出现 0.5
    } else if (a - 2 * b > c) {
      // 左子树串行段太长：右子树整体塞进左边空闲的那台机器
      saved = b + c;
    } else {
      // 右子树占主导：左子树整体塞进右边空闲的那台机器
      saved = a + d;
    }
    return new double[] {a + c + root.val, saved}; // 加上当前节点自身的执行时间
  }

  // 答案 = 子树总和 - 并行节省
  static double minimalExecutionTime(TreeNode root) {
    double[] r = dfs(root);
    return r[0] - r[1];
  }

  public static void main(String[] args) { // 程序入口：跑内嵌自测用例（三个官方用例）
    List<List<Double>> cases =
        Arrays.asList(
            Arrays.asList(47.0, 74.0, 31.0),
            Arrays.asList(15.0, 21.0, null, 24.0, null, 27.0, 26.0),
            Arrays.asList(1.0, 3.0, 2.0, null, null, 4.0, 4.0));
    double[] wants = {121.0, 87.0, 7.5};
    for (int i = 0; i < cases.size(); i++) {
      double got = minimalExecutionTime(buildTree(cases.get(i)));
      if (Math.abs(got - wants[i]) >= 1e-6) { // 浮点比较用 1e-6 容差
        throw new RuntimeException("FAIL got=" + got + " want=" + wants[i]); // 失败抛异常（非零退出）
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
