// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
// LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — Dart 版（方案1）
bool verifyPostorder(List<int> postorder) {
  // 定义函数/方法 verifyPostorder
  bool check(int lo, int hi) {
    // 定义判定函数 check
    if (hi - lo <= 1) return true; // 若 右边界 减 左边界 不超过 1，直接返回 true
    final root = postorder[hi]; // 把 postorder[右边界] 存入 根节点
    var i = lo; // 把 左边界 存入 下标 i
    while (i < hi && postorder[i] < root) {
      i++;
    }
    for (var j = i; j < hi; j++) {
      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 右边界 就继续
      if (postorder[j] < root)
        return false; // 若 postorder[下标 j] 小于 根节点，直接返回 false
    }
    return check(lo, i - 1) &&
        check(i, hi - 1); // 返回 check(左边界, 下标 i 减 1) 且 check(下标 i, 右边界 减 1)
  }

  return check(0, postorder.length - 1); // 返回 check(0, postorder.长度 减 1)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (verifyPostorder([1, 6, 3, 2, 5]))
    throw StateError(
      'c1',
    ); // 若 verifyPostorder([1, 6, 3, 2, 5])) throw StateError('c1');
  if (!verifyPostorder([1, 3, 2, 4, 5])) throw StateError('c2');
  if (!verifyPostorder([4, 6, 5, 9, 8, 7])) throw StateError('c3');
  if (!verifyPostorder([1, 2, 3]))
    throw StateError(
      'c4',
    ); // 若 取反 verifyPostorder([1, 2, 3])) throw StateError('c4');
  print('PASS');
} // 全部用例通过，输出 PASS
