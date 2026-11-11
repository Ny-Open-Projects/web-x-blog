// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — Dart 版（方案3：分治递归（紧凑版，附层序/相同树/中序辅助函数））
// harness：层序数组建树，null 表示空节点

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

// 辅助：层序遍历按层分组
List<List<int>> levelList(TreeNode? root) {
  // 定义函数/方法 levelList
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var level = <TreeNode?>[root]; // 把 小于 TreeNode? 超过 [根节点] 存入 level
  while (level.isNotEmpty) {
    // 循环，直到不满足「level.isNotEmpty」
    final vals = <int>[]; // 把 小于 int 超过 [] 存入 vals
    final nxt = <TreeNode?>[]; // 把 小于 TreeNode? 超过 [] 存入 nxt
    for (final n in level) {
      // for (final 元素个数 in level) {
      if (n == null) continue; // 若 元素个数 等于 null) continue;
      vals.add(n.val); // vals 追加 元素个数.值);
      nxt.add(n.left); // nxt 追加 元素个数.左边界);
      nxt.add(n.right); // nxt 追加 元素个数.右边界);
    }
    res.add(vals); // 结果 追加 vals);
    level = nxt; // 把 nxt 存入 level
  }
  return res; // 返回 结果
}

// 辅助：判断两棵树是否相同
bool sameTree(TreeNode? a, TreeNode? b) {
  // 定义函数/方法 sameTree
  if (a == null && b == null) return true; // 若 数组 等于 null 且 b 等于 null，直接返回 true
  if (a == null || b == null)
    return false; // 若 数组 等于 null 或 b 等于 null，直接返回 false
  return a.val == b.val &&
      sameTree(a.left, b.left) &&
      sameTree(a.right, b.right);
}

// 辅助：中序遍历
List<int> inorderT(TreeNode? n) {
  // 定义函数/方法 inorderT
  if (n == null) return []; // 若 元素个数 等于 null，直接返回 []
  return [
    ...inorderT(n.left),
    n.val,
    ...inorderT(n.right),
  ]; // 返回 [...inorderT(元素个数.左边界), 元素个数.值, ...inorderT(元素个数.右边界)]
}

// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
int maxDepth(TreeNode? root) {
  // 定义函数/方法 maxDepth
  if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
  final l = maxDepth(root.left); // 把 maxDepth(根节点.左边界) 存入 左指针
  final r = maxDepth(root.right); // 把 maxDepth(根节点.右边界) 存入 右指针
  return 1 + (l > r ? l : r); // 返回 1 加 (左指针 超过 右指针 ? 左指针 : 右指针)
}

void main() {
  // 程序入口：跑内嵌自测用例
  final tests = <List<int?>, int>{
    // 把 小于 List 小于 int? 超过 , int 超过 { 存入 tests
    <int?>[3, 9, 20, null, null, 15, 7]: 3,
    <int?>[1, 2, 3, 4, 5, null, null, null, 6]: 4,
    <int?>[]: 0,
  };
  var idx = 0; // 把 0 存入 idx
  for (final entry in tests.entries) {
    // for (final entry in tests.entries) {
    final got = maxDepth(
      buildTree(entry.key),
    ); // 把 maxDepth(buildTree(entry.key)) 存入 got
    if (got != entry.value) {
      // 若 got 不等于 entry.value
      throw StateError('case $idx failed: got $got want ${entry.value}');
    }
    idx++; // idx 加一
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
