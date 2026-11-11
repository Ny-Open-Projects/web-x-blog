// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Dart 版（方案6）
int findKthLargest(List<int> nums, int k) {
  // 定义函数/方法 findKthLargest
  // 简易最大堆
  final h = <int>[]; // 把 小于 int 超过 [] 存入 h
  void up(int i) {
    // 定义函数/方法 up
    while (i > 0) {
      // 循环，直到不满足「下标 i 超过 0」
      final p = (i - 1) ~/ 2; // 把 (下标 i 减 1) ~ 除以 2 存入 节点
      if (h[i] <= h[p]) break; // 若 h[下标 i] 不超过 h[节点]) break;
      final t = h[i]; // 把 h[下标 i] 存入 另一字符串
      h[i] = h[p]; // 把 h[节点]; 写入 h[i]
      h[p] = t; // 把 另一字符串; 写入 h[p]
      i = p; // 把 节点 存入 下标 i
    }
  }

  void down(int i) {
    // 定义函数/方法 down
    while (true) {
      // 循环，直到不满足「true」
      final l = 2 * i + 1,
          r = 2 * i + 2; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2 存入 左指针
      var m = i; // 把 下标 i 存入 映射表
      if (l < h.length && h[l] > h[m])
        m = l; // 若 左指针 小于 h.长度 且 h[左指针] 超过 h[映射表]) 映射表 赋值为 左指针;
      if (r < h.length && h[r] > h[m])
        m = r; // 若 右指针 小于 h.长度 且 h[右指针] 超过 h[映射表]) 映射表 赋值为 右指针;
      if (m == i) break; // 若 映射表 等于 下标 i) break;
      final t = h[i]; // 把 h[下标 i] 存入 另一字符串
      h[i] = h[m]; // 把 h[映射表]; 写入 h[i]
      h[m] = t; // 把 另一字符串; 写入 h[m]
      i = m; // 把 映射表 存入 下标 i
    }
  }

  for (final v in nums) {
    // for (final 值 in 数组) {
    h.add(v); // h 追加 值);
    up(h.length - 1); // up(h.长度 减 1);
  }
  for (var t = 0; t + 1 < k; t++) {
    // 让 另一字符串 从 0 开始计数，另一字符串 加 1 小于 下标 k 就继续
    final last = h.removeLast(); // 把 h.removeLast() 存入 last
    if (h.isNotEmpty) {
      // 若 h.isNotEmpty
      h[0] = last; // 把 last; 写入 h[0]
      down(0); // down(0);
    }
  }
  return h.first; // 返回 h.first
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4)
    throw StateError('c2');
  if (findKthLargest([1], 1) != 1)
    throw StateError(
      'c3',
    ); // 若 findKthLargest([1], 1) 不等于 1) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
