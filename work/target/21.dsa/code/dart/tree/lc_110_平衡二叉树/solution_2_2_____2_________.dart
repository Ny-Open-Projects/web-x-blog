// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135170465
// LeetCode 110. 平衡二叉树 — Dart 版（方案2）
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

int height(TreeNode? n) {
  // 定义函数/方法 height
  if (n == null) return 0; // 若 元素个数 等于 null，直接返回 0
  return (height(n.left) > height(n.right) ? height(n.left) : height(n.right)) +
      1;
}

bool isBalanced(TreeNode? root) {
  // 定义判定函数 isBalanced
  if (root == null) return true; // 若 根节点 等于 null，直接返回 true
  final d =
      height(root.left) -
      height(root.right); // 把 height(根节点.左边界) 减 height(根节点.右边界) 存入 d
  if (d > 1 || d < -1) return false; // 若 d 超过 1 或 d 小于 减 1，直接返回 false
  return isBalanced(root.left) &&
      isBalanced(root.right); // 返回 isBalanced(根节点.左边界) 且 isBalanced(根节点.右边界)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!isBalanced(buildTree([3, 9, 20, null, null, 15, 7])))
    throw StateError('c1');
  if (isBalanced(buildTree([1, 2, 2, 3, 3, null, null, 4, 4])))
    throw StateError('c2');
  if (!isBalanced(null))
    throw StateError('c3'); // 若 取反 isBalanced(null)) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
