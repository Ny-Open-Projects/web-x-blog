// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
// 数据结构与算法之堆: 实现最大堆类及堆排序 — Dart 版（方案5）
List<int> maxHeapPopAll(List<int> input) {
  // 定义函数/方法 maxHeapPopAll
  final h = <int>[]; // 把 小于 int 超过 [] 存入 h
  void up(int i) {
    // 定义函数/方法 up
    while (i > 0) {
      // 循环，直到不满足「下标 i 超过 0」
      final p = (i - 1) ~/ 2; // 把 (下标 i 减 1) ~ 除以 2 存入 节点
      if (h[p] >= h[i]) break; // 若 h[节点] 不低于 h[下标 i]) break;
      final t = h[p]; // 把 h[节点] 存入 另一字符串
      h[p] = h[i]; // 把 h[下标 i]; 写入 h[p]
      h[i] = t; // 把 另一字符串; 写入 h[i]
      i = p; // 把 节点 存入 下标 i
    }
  }

  void down(int i) {
    // 定义函数/方法 down
    final n = h.length; // 把 h.长度 存入 元素个数
    while (true) {
      // 循环，直到不满足「true」
      final l = 2 * i + 1,
          r = 2 * i + 2; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2 存入 左指针
      var m = i; // 把 下标 i 存入 映射表
      if (l < n && h[l] > h[m])
        m = l; // 若 左指针 小于 元素个数 且 h[左指针] 超过 h[映射表]) 映射表 赋值为 左指针;
      if (r < n && h[r] > h[m])
        m = r; // 若 右指针 小于 元素个数 且 h[右指针] 超过 h[映射表]) 映射表 赋值为 右指针;
      if (m == i) break; // 若 映射表 等于 下标 i) break;
      final t = h[i]; // 把 h[下标 i] 存入 另一字符串
      h[i] = h[m]; // 把 h[映射表]; 写入 h[i]
      h[m] = t; // 把 另一字符串; 写入 h[m]
      i = m; // 把 映射表 存入 下标 i
    }
  }

  for (final v in input) {
    // for (final 值 in input) {
    h.add(v); // h 追加 值);
    up(h.length - 1); // up(h.长度 减 1);
  }
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  while (h.isNotEmpty) {
    // 循环，直到不满足「h.isNotEmpty」
    out.add(h[0]); // out 追加 h[0]);
    final last = h.removeLast(); // 把 h.removeLast() 存入 last
    if (h.isNotEmpty) {
      h[0] = last;
      down(0);
    } // 若 h.isNotEmpty) { h[0] 赋值为 last; down(0); }
  }
  return out; // 返回 out
}

void main() {
  if (maxHeapPopAll([3, 1, 6, 5, 2, 4]).toString() != '[6, 5, 4, 3, 2, 1]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
