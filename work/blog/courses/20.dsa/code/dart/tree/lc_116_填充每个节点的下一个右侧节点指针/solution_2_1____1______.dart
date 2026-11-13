// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
// LeetCode 116. 填充每个节点的下一个右侧节点指针 — Dart 版（方案2）
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

class NNode {
  // 定义类型
  final int val; // final int 值;
  NNode? left, right, next; // NNode? 左边界, 右边界, 下一个;
  NNode(this.val); // NNode(this.值);
}

NNode? buildNTree(List<int> vals) {
  // NNode? buildNTree(List 小于 int 超过 vals) {
  if (vals.isEmpty) return null; // 若 vals.isEmpty，直接返回 null
  final root = NNode(vals[0]); // 把 NNode(vals[0]) 存入 根节点
  final q = <NNode>[root]; // 把 小于 NNode 超过 [根节点] 存入 节点
  var head = 0; // 把 0 存入 头节点
  var i = 1; // 把 1 存入 下标 i
  while (head < q.length && i < vals.length) {
    // 循环，直到不满足「头节点 小于 节点.长度 且 下标 i 小于 vals.长度」
    final node = q[head++]; // 把 节点[头节点 加一 ] 存入 节点
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      node.left = NNode(vals[i]); // 把 NNode(vals[下标 i]); 写入 左边界
      q.add(node.left!); // 节点 追加 节点.左边界取反 );
      i++; // 下标 i 加一
    }
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      node.right = NNode(vals[i]); // 把 NNode(vals[下标 i]); 写入 右边界
      q.add(node.right!); // 节点 追加 节点.右边界取反 );
      i++; // 下标 i 加一
    }
  }
  return root; // 返回 根节点
}

NNode? connect(NNode? root) {
  // NNode? connect(NNode? 根节点) {
  if (root == null) return null; // 若 根节点 等于 null，直接返回 null
  final q = <NNode>[root]; // 把 小于 NNode 超过 [根节点] 存入 节点
  var head = 0; // 把 0 存入 头节点
  while (head < q.length) {
    // 循环，直到不满足「头节点 小于 节点.长度」
    final size = q.length - head; // 把 节点.长度 减 头节点 存入 大小
    NNode? prev; // NNode? 前一个;
    for (var k = 0; k < size; k++) {
      // 让 下标 k 从 0 开始计数，下标 k 小于 大小 就继续
      final node = q[head++]; // 把 节点[头节点 加一 ] 存入 节点
      if (prev != null) prev.next = node; // 若 前一个 不等于 null) 前一个.下一个 赋值为 节点;
      prev = node; // 把 节点 存入 前一个
      if (node.left != null)
        q.add(node.left!); // 若 节点.左边界 不等于 null) 节点 追加 节点.左边界取反 );
      if (node.right != null)
        q.add(node.right!); // 若 节点.右边界 不等于 null) 节点 追加 节点.右边界取反 );
    }
  }
  return root; // 返回 根节点
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (connect(null) != null)
    throw StateError('c0'); // 若 connect(null) 不等于 null) throw StateError('c0');
  final root = connect(
    buildNTree([1, 2, 3, 4, 5, 6, 7]),
  )!; // 把 connect(buildNTree([1, 2, 3, 4, 5, 6, 7]))取反 存入 根节点
  final levels = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 levels
  NNode? cur = root; // 把 根节点; 写入 NNode? cur
  while (cur != null) {
    // 循环，直到不满足「当前值 不等于 null」
    final vals = <int>[]; // 把 小于 int 超过 [] 存入 vals
    NNode? node = cur; // 把 当前值; 写入 NNode? node
    while (node != null) {
      // 循环，直到不满足「节点 不等于 null」
      vals.add(node.val); // vals 追加 节点.值);
      node = node.next; // 把 节点.下一个 存入 节点
    }
    levels.add(vals); // levels 追加 vals);
    cur = cur.left; // 把 当前值.左边界 存入 当前值
  }
  if (levels.length != 3)
    throw StateError(
      'levels',
    ); // 若 levels.长度 不等于 3) throw StateError('levels');
  if (levels[0].toString() != '[1]' ||
      levels[1].toString() != '[2, 3]' ||
      levels[2].toString() != '[4, 5, 6, 7]')
    throw StateError('vals');
  print('PASS'); // 全部用例通过，输出 PASS
}
