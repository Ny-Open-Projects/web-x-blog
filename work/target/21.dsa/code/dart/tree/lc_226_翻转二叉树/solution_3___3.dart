// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134541657
// LeetCode 226. 翻转二叉树 — Dart 版（方案3）
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

TreeNode? invertTree(TreeNode? root) {
  // TreeNode? invertTree(TreeNode? 根节点) {
  if (root == null) return null; // 若 根节点 等于 null，直接返回 null
  final stack = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 栈
  while (stack.isNotEmpty) {
    // 循环，直到不满足「栈.isNotEmpty」
    final node = stack.removeLast(); // 把 栈.removeLast() 存入 节点
    final tmp = node.left; // 把 节点.左边界 存入 临时变量
    node.left = node.right; // 把 节点.右边界; 写入 左边界
    node.right = tmp; // 把 临时变量; 写入 右边界
    if (node.left != null)
      stack.add(node.left!); // 若 节点.左边界 不等于 null) 栈 追加 节点.左边界取反 );
    if (node.right != null)
      stack.add(node.right!); // 若 节点.右边界 不等于 null) 栈 追加 节点.右边界取反 );
  }
  return root; // 返回 根节点
}

void main() {
  // 程序入口：跑内嵌自测用例
  final t = invertTree(
    buildTree([4, 2, 7, 1, 3, 6, 9]),
  ); // 把 invertTree(buildTree([4, 2, 7, 1, 3, 6, 9])) 存入 另一字符串
  final flat = treeToLevels(t).map((l) => l.join(',')).join('|');
  if (flat != '4|7,2|9,6,3,1') throw StateError('invert failed: $flat');
  if (invertTree(null) != null) throw StateError('null failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
