// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Dart 版（方案1：深度优先-贪心）

import 'dart:io'; // 引入依赖（退出码用 exit）

class TreeNode {
  // 二叉树节点：val 为自身执行时间（double 承载并行节省的 0.5）
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

// dfs 返回 [子树总耗时, 两台机器并行可节省的耗时]
List<double> dfs(TreeNode? root) {
  if (root == null) return [0.0, 0.0]; // 空子树：总耗时 0，节省 0
  final left = dfs(root.left);
  final right = dfs(root.right);
  final a = left[0], b = left[1]; // a: 左子树总耗时, b: 左子树已节省
  final c = right[0], d = right[1]; // c: 右子树总耗时, d: 右子树已节省
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
  return [a + c + root.val, saved]; // 加上当前节点自身的执行时间
}

double minimalExecutionTime(TreeNode? root) {
  // 答案 = 子树总和 - 并行节省
  final r = dfs(root);
  return r[0] - r[1];
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
