// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
// 数据结构与算法之排序: 冒泡排序 — Dart 版（方案6）
List<int> gnomeSortBubble(List<int> nums) {
  // 定义函数/方法 gnomeSortBubble
  final v = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 值
  final n = v.length; // 把 值.长度 存入 元素个数
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = 0; j < n - 1 - i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 减 下标 i 就继续
      if (v[j] > v[j + 1]) {
        // 若 值[下标 j] 超过 值[下标 j 加 1]
        final t = v[j]; // 把 值[下标 j] 存入 另一字符串
        v[j] = v[j + 1]; // 把 值[下标 j 加 1]; 写入 v[j]
        v[j + 1] = t; // 把 另一字符串; 写入 v[j + 1]
      }
    }
  }
  return v; // 返回 值
}

void main() {
  if (gnomeSortBubble([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  if (gnomeSortBubble([3, 1, 2]).toString() != '[1, 2, 3]')
    throw StateError('c2');
  if (gnomeSortBubble([]).isNotEmpty) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
