// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Dart 版（方案2：深度优先-优化）

import 'dart:io'; // 引入依赖（退出码用 exit）
import 'dart:math' show max; // 引入依赖（取最大值）

class TreeNode {
  // 二叉树节点：val 为自身执行时间（double 承载均摊的 0.5）
  double val;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.val);
}

TreeNode? buildTree(List<double?> vals) {
  // 层序数组建树，null 表示空节点
  if (vals.isEmpty) return null;
  final root = TreeNode(vals[0]!);
  final queue = <TreeNode>[root]; // 队列里只放非空节点
  int i = 1;
  while (queue.isNotEmpty && i < vals.length) {
    final node = queue.removeAt(0); // 出队一个父节点
    if (i < vals.length && vals[i] != null) {
      // 左孩子
      node.left = TreeNode(vals[i]!);
      queue.add(node.left!);
    }
    i++;
    if (i < vals.length && vals[i] != null) {
      // 右孩子
      node.right = TreeNode(vals[i]!);
      queue.add(node.right!);
    }
    i++;
  }
  return root;
}

// dfs 返回 [子树总耗时, 子树最小完成时间 maxExec]
List<double> dfs(TreeNode? root) {
  if (root == null) return [0.0, 0.0]; // 空子树
  final left = dfs(root.left); // 左子树的总耗时与最小完成时间
  final right = dfs(root.right); // 右子树的总耗时与最小完成时间
  // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
  // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
  final parallel = (left[0] + right[0]) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
  final maxExec = root.val + max(max(left[1], right[1]), parallel);
  return [left[0] + right[0] + root.val, maxExec];
}

double minimalExecutionTime(TreeNode? root) {
  // 答案 = 整棵树的最小完成时间
  return dfs(root)[1];
}

void main() {
  // 程序入口：跑内嵌自测用例（三个官方用例）
  final cases = <List<dynamic>>[
    [
      <double?>[47, 74, 31],
      121.0,
    ],
    [
      <double?>[15, 21, null, 24, null, 27, 26],
      87.0,
    ],
    [
      <double?>[1, 3, 2, null, null, 4, 4],
      7.5,
    ],
  ];
  var fail = false;
  for (final tc in cases) {
    final vals = tc[0] as List<double?>;
    final want = tc[1] as double;
    final got = minimalExecutionTime(buildTree(vals));
    if ((got - want).abs() >= 1e-6) {
      // 浮点比较用 1e-6 容差
      print('FAIL got $got want $want'); // 失败打印 FAIL
      fail = true;
    }
  }
  if (fail) exit(1); // 非零退出
  print('PASS'); // 全部用例通过，输出 PASS
}
