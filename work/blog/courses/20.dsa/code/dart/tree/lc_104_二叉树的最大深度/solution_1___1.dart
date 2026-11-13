// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — Dart 版

class TreeNode {
  // 定义类型
  int val; // int 值;
  TreeNode? left; // TreeNode? 左边界;
  TreeNode? right; // TreeNode? 右边界;
  TreeNode(this.val); // TreeNode(this.值);
}

/// 层序数组构建二叉树，null 用 nullValue 哨兵（这里用 -1，测试输入均为非负）
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

/// 主解法：DFS，叶子节点时刷新最大深度（与 blog 方案1一致）
int maxDepth(TreeNode? root) {
  // 定义函数/方法 maxDepth
  var dep = 0; // 把 0 存入 dep
  void dfs(TreeNode? n, int l) {
    // 定义函数/方法 dfs
    if (n == null) return; // 若 元素个数 等于 null) return;
    if (n.left == null && n.right == null) {
      // 若 元素个数.左边界 等于 null 且 元素个数.右边界 等于 null
      if (l > dep) dep = l; // 若 左指针 超过 dep) dep 赋值为 左指针;
    }
    dfs(n.left, l + 1); // dfs(元素个数.左边界, 左指针 加 1);
    dfs(n.right, l + 1); // dfs(元素个数.右边界, 左指针 加 1);
  }

  dfs(root, 1); // dfs(根节点, 1);
  return dep; // 返回 dep
}

void main() {
  // 程序入口：跑内嵌自测用例
  final tests = <List<int?>, int>{
    // 把 小于 List 小于 int? 超过 , int 超过 { 存入 tests
    <int?>[]: 0,
    <int?>[1]: 1,
    <int?>[3, 9, 20, null, null, 15, 7]: 3,
    <int?>[1, null, 2, null, 3]: 3,
  };
  for (final entry in tests.entries) {
    // for (final entry in tests.entries) {
    final got = maxDepth(
      buildTree(entry.key),
    ); // 把 maxDepth(buildTree(entry.key)) 存入 got
    if (got != entry.value) {
      // 若 got 不等于 entry.value
      throw StateError('case failed: got $got want ${entry.value}');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
