// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131302535
// LeetCode 637. 二叉树的层平均值 — Dart 版（方案1）
class TreeNode {
  // 定义类型
  int val; // int 值;
  TreeNode? left; // TreeNode? 左边界;
  TreeNode? right; // TreeNode? 右边界;
  TreeNode(this.val); // TreeNode(this.值);
}

TreeNode? buildTree(List<int?> vals) {
  // TreeNode? buildTree(List 小于 int? 超过 vals) {
  if (vals.isEmpty || vals[0] == null)
    return null; // 若 vals.isEmpty 或 vals[0] 等于 null，直接返回 null
  final root = TreeNode(vals[0]!); // 把 TreeNode(vals[0]取反 ) 存入 根节点
  final queue = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 队列
  var head = 0; // 把 0 存入 头节点
  var i = 1; // 把 1 存入 下标 i
  while (head < queue.length && i < vals.length) {
    // 循环，直到不满足「头节点 小于 队列.长度 且 下标 i 小于 vals.长度」
    final node = queue[head++]; // 把 队列[头节点 加一 ] 存入 节点
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.left = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 左边界
        queue.add(node.left!); // 队列 追加 节点.左边界取反 );
      }
      i++; // 下标 i 加一
    }
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.right = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 右边界
        queue.add(node.right!); // 队列 追加 节点.右边界取反 );
      }
      i++; // 下标 i 加一
    }
  }
  return root; // 返回 根节点
}

List<List<int>> treeToLevels(TreeNode? root) {
  // 定义函数/方法 treeToLevels
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var level = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 level
  while (level.isNotEmpty) {
    // 循环，直到不满足「level.isNotEmpty」
    final vals = <int>[]; // 把 小于 int 超过 [] 存入 vals
    final nxt = <TreeNode>[]; // 把 小于 TreeNode 超过 [] 存入 nxt
    for (final n in level) {
      // for (final 元素个数 in level) {
      vals.add(n.val); // vals 追加 元素个数.值);
      if (n.left != null)
        nxt.add(n.left!); // 若 元素个数.左边界 不等于 null) nxt 追加 元素个数.左边界取反 );
      if (n.right != null)
        nxt.add(n.right!); // 若 元素个数.右边界 不等于 null) nxt 追加 元素个数.右边界取反 );
    }
    res.add(vals); // 结果 追加 vals);
    level = nxt; // 把 nxt 存入 level
  }
  return res; // 返回 结果
}

List<double> averageOfLevels(TreeNode? root) {
  // 定义函数/方法 averageOfLevels
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <double>[]; // 把 小于 double 超过 [] 存入 结果
  var q = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 节点
  while (q.isNotEmpty) {
    // 循环，直到不满足「节点.isNotEmpty」
    final size = q.length; // 把 节点.长度 存入 大小
    var sum = 0; // 把 0 存入 累计和
    final nxt = <TreeNode>[]; // 把 小于 TreeNode 超过 [] 存入 nxt
    for (final n in q) {
      // for (final 元素个数 in 节点) {
      sum += n.val; // 累计和累加 元素个数.值
      if (n.left != null)
        nxt.add(n.left!); // 若 元素个数.左边界 不等于 null) nxt 追加 元素个数.左边界取反 );
      if (n.right != null)
        nxt.add(n.right!); // 若 元素个数.右边界 不等于 null) nxt 追加 元素个数.右边界取反 );
    }
    res.add(sum / size); // 结果 追加 累计和 除以 大小);
    q = nxt; // 把 nxt 存入 节点
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final a = averageOfLevels(
    buildTree([3, 9, 20, 15, 7]),
  ); // 把 averageOfLevels(buildTree([3, 9, 20, 15, 7])) 存入 数组
  if (a.length != 3 ||
      (a[0] - 3).abs() > 1e-9 ||
      (a[1] - 14.5).abs() > 1e-9 ||
      (a[2] - 11).abs() > 1e-9)
    throw StateError('c1');
  final b = averageOfLevels(
    buildTree([1]),
  ); // 把 averageOfLevels(buildTree([1])) 存入 b
  if (b.length != 1 || (b[0] - 1).abs() > 1e-9) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
