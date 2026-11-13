// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416
// LeetCode 92. 反转链表II — Dart 版（方案1）
List<int> reverseBetween(List<int> vals, int left, int right) {
  // 定义函数/方法 reverseBetween
  final v = List<int>.from(vals); // 把 List 小于 int 超过 .from(vals) 存入 值
  var l = left - 1, r = right - 1; // 把 左边界 减 1, 右指针 赋值为 右边界 减 1 存入 左指针
  while (l < r) {
    // 循环，直到不满足「左指针 小于 右指针」
    final t = v[l]; // 把 值[左指针] 存入 另一字符串
    v[l] = v[r]; // 把 值[右指针]; 写入 v[l]
    v[r] = t; // 把 另一字符串; 写入 v[r]
    l++; // 左指针 加一
    r--; // 右指针 减一
  }
  return v; // 返回 值
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (reverseBetween([1, 2, 3, 4, 5], 2, 4).toString() != '[1, 4, 3, 2, 5]')
    throw StateError('c1');
  if (reverseBetween([1, 2, 3, 4, 5], 1, 4).toString() != '[4, 3, 2, 1, 5]')
    throw StateError('c2');
  if (reverseBetween([5], 1, 1).toString() != '[5]') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
