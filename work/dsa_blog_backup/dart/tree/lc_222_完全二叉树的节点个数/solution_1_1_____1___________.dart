// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136210437
// LeetCode 222. 完全二叉树的节点个数 — Dart 版（方案1）
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

int countNodes(TreeNode? root) {
  // 定义函数/方法 countNodes
  if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
  var lh = 0; // 把 0 存入 lh
  var r = root.left; // 把 根节点.左边界 存入 右指针
  while (r != null) {
    // 循环，直到不满足「右指针 不等于 null」
    lh++; // lh 加一
    r = r.left; // 把 右指针.左边界 存入 右指针
  }
  var rh = 0; // 把 0 存入 rh
  r = root.right; // 把 根节点.右边界 存入 右指针
  while (r != null) {
    // 循环，直到不满足「右指针 不等于 null」
    rh++; // rh 加一
    r = r.right; // 把 右指针.右边界 存入 右指针
  }
  if (lh == rh)
    return (1 << (lh + 1)) - 1; // 若 lh 等于 rh，直接返回 (1 小于 小于 (lh 加 1)) 减 1
  return 1 +
      countNodes(root.left) +
      countNodes(
        root.right,
      ); // 返回 1 加 countNodes(根节点.左边界) 加 countNodes(根节点.右边界)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (countNodes(buildTree([1, 2, 3, 4, 5, 6])) != 6) throw StateError('c1');
  if (countNodes(null) != 0)
    throw StateError('c2'); // 若 countNodes(null) 不等于 0) throw StateError('c2');
  if (countNodes(buildTree([1])) != 1)
    throw StateError(
      'c3',
    ); // 若 countNodes(buildTree([1])) 不等于 1) throw StateError('c3');
  if (countNodes(buildTree([1, 2, 3, 4, 5, 6, 7, 8])) != 8)
    throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
