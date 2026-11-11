// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
// 数据结构与算法之排序: 堆排序 — Dart 版（方案1）
List<int> heapSort(List<int> nums) {
  // 定义函数/方法 heapSort
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  final n = v.length; // 把 值.长度 存入 元素个数
  if (n == 0) return v; // 若 元素个数 等于 0，直接返回 值
  void sift(int start, int end) {
    // 定义函数/方法 sift
    var root = start; // 把 起点 存入 根节点
    while (true) {
      // 循环，直到不满足「true」
      final child = 2 * root + 1; // 把 2 乘 根节点 加 1 存入 子节点
      if (child > end) break; // 若 子节点 超过 终点) break;
      var swap = root; // 把 根节点 存入 swap
      if (v[swap] < v[child])
        swap = child; // 若 值[swap] 小于 值[子节点]) swap 赋值为 子节点;
      if (child + 1 <= end && v[swap] < v[child + 1])
        swap =
            child +
            1; // 若 子节点 加 1 不超过 终点 且 值[swap] 小于 值[子节点 加 1]) swap 赋值为 子节点 加 1;
      if (swap == root) break; // 若 swap 等于 根节点) break;
      final t = v[root]; // 把 值[根节点] 存入 另一字符串
      v[root] = v[swap]; // 把 值[swap]; 写入 v[root]
      v[swap] = t; // 把 另一字符串; 写入 v[swap]
      root = swap; // 把 swap 存入 根节点
    }
  }

  for (var i = n ~/ 2 - 1; i >= 0; i--) {
    sift(i, n - 1);
  } // 让 下标 i 从 元素个数 ~ 除以 2 减 1 开始计数，下标 i 不低于 0 就继续
  for (var end = n - 1; end >= 1; end--) {
    // 让 终点 从 元素个数 减 1 开始计数，终点 不低于 1 就继续
    final t = v[0]; // 把 值[0] 存入 另一字符串
    v[0] = v[end]; // 把 值[终点]; 写入 v[0]
    v[end] = t; // 把 另一字符串; 写入 v[end]
    sift(0, end - 1); // sift(0, 终点 减 1);
  }
  return v; // 返回 值
}

void main() {
  if (heapSort([5, 2, 4, 6, 1, 3]).toString() != '[1, 2, 3, 4, 5, 6]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
