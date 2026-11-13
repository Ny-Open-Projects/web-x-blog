// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Java 版（方案2：深度优先-优化）

package com.webfault.dsa;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

class Lcp10S2 { // 非 public class：文件名可以与类名不同
  static class TreeNode { // 二叉树节点：val 为自身执行时间（double 承载均摊的 0.5）
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

  // dfs 返回 [子树总耗时, 子树最小完成时间 maxExec]
  static double[] dfs(TreeNode root) {
    if (root == null) return new double[] {0.0, 0.0}; // 空子树
    double[] left = dfs(root.left); // 左子树的总耗时与最小完成时间
    double[] right = dfs(root.right); // 右子树的总耗时与最小完成时间
    // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
    // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    double parallel = (left[0] + right[0]) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
    double maxExec = root.val + Math.max(Math.max(left[1], right[1]), parallel);
    return new double[] {left[0] + right[0] + root.val, maxExec};
  }

  // 答案 = 整棵树的最小完成时间
  static double minimalExecutionTime(TreeNode root) {
    return dfs(root)[1];
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
