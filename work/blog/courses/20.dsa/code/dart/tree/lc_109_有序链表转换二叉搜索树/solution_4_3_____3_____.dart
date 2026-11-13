// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549
// LeetCode 109. 有序链表转换二叉搜索树 — Dart 版（方案4）
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

class LNode {
  // 定义类型
  final int val; // final int 值;
  LNode? next; // LNode? 下一个;
  LNode(this.val); // LNode(this.值);
}

LNode? buildList(List<int> vals) {
  // LNode? buildList(List 小于 int 超过 vals) {
  LNode? head; // LNode? 头节点;
  LNode? cur; // LNode? 当前值;
  for (final v in vals) {
    // for (final 值 in vals) {
    final n = LNode(v); // 把 LNode(值) 存入 元素个数
    if (head == null) {
      // 若 头节点 等于 null
      head = n; // 把 元素个数 存入 头节点
    } else {
      // 否则
      cur!.next = n; // 把 元素个数; 写入 下一个
    }
    cur = n; // 把 元素个数 存入 当前值
  }
  return head; // 返回 头节点
}

TreeNode? buildBst(List<int> nodes, int left, int right) {
  // TreeNode? buildBst(List 小于 int 超过 nodes, int 左边界, int 右边界) {
  if (left > right) return null; // 若 左边界 超过 右边界，直接返回 null
  final mid = left + (right - left) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 中点
  final root = TreeNode(nodes[mid]); // 把 TreeNode(nodes[中点]) 存入 根节点
  root.left = buildBst(
    nodes,
    left,
    mid - 1,
  ); // 把 buildBst(nodes, 左边界, 中点 减 1); 写入 左边界
  root.right = buildBst(
    nodes,
    mid + 1,
    right,
  ); // 把 buildBst(nodes, 中点 加 1, 右边界); 写入 右边界
  return root; // 返回 根节点
}

TreeNode? sortedListToBST(LNode? head) {
  // TreeNode? sortedListToBST(LNode? 头节点) {
  final nodes = <int>[]; // 把 小于 int 超过 [] 存入 nodes
  var cur = head; // 把 头节点 存入 当前值
  while (cur != null) {
    // 循环，直到不满足「当前值 不等于 null」
    nodes.add(cur.val); // nodes 追加 当前值.值);
    cur = cur.next; // 把 当前值.下一个 存入 当前值
  }
  if (nodes.isEmpty) return null; // 若 nodes.isEmpty，直接返回 null
  return buildBst(
    nodes,
    0,
    nodes.length - 1,
  ); // 返回 buildBst(nodes, 0, nodes.长度 减 1)
}

void inorder(TreeNode? n, List<int> out) {
  // 定义函数/方法 inorder
  if (n == null) return; // 若 元素个数 等于 null) return;
  inorder(n.left, out); // inorder(元素个数.左边界, out);
  out.add(n.val); // out 追加 元素个数.值);
  inorder(n.right, out); // inorder(元素个数.右边界, out);
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (sortedListToBST(null) != null)
    throw StateError(
      'c0',
    ); // 若 sortedListToBST(null) 不等于 null) throw StateError('c0');
  final t = sortedListToBST(
    buildList([1, 2, 3]),
  ); // 把 sortedListToBST(buildList([1, 2, 3])) 存入 另一字符串
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  inorder(t, out); // inorder(另一字符串, out);
  if (out.toString() != '[1, 2, 3]')
    throw StateError(
      'c1',
    ); // 若 out.toString() 不等于 '[1, 2, 3]') throw StateError('c1');
  if (t!.val != 2 || t.left!.val != 1 || t.right!.val != 3)
    throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
