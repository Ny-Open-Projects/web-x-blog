// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
// LeetCode 556. 下一个更大元素 III — Dart 版（方案1）
int nextGreaterElement(int n) {
  // 定义函数/方法 nextGreaterElement
  final d = <int>[]; // 把 小于 int 超过 [] 存入 d
  var x = n; // 把 元素个数 存入 x
  while (x > 0) {
    d.add(x % 10);
    x = x ~/ 10;
  } // 循环，直到不满足「x 超过 0) { d 追加 x 对…取模 10); x 赋值为 x ~ 除以 10; }」
  // 转正序
  final dd = d.reversed.toList(); // 把 d.reversed.toList() 存入 dd
  final m = dd.length; // 把 dd.长度 存入 映射表
  if (m < 2) return -1; // 若 映射表 小于 2，直接返回 减 1
  var i = m - 2; // 把 映射表 减 2 存入 下标 i
  while (i >= 0 && dd[i] >= dd[i + 1])
    i--; // 循环，直到不满足「下标 i 不低于 0 且 dd[下标 i] 不低于 dd[下标 i 加 1]) 下标 i 减一 ;」
  if (i < 0) return -1; // 若 下标 i 小于 0，直接返回 减 1
  var j = m - 1; // 把 映射表 减 1 存入 下标 j
  while (dd[j] <= dd[i]) j--; // 循环，直到不满足「dd[下标 j] 不超过 dd[下标 i]) 下标 j 减一 ;」
  final t = dd[i]; // 把 dd[下标 i] 存入 另一字符串
  dd[i] = dd[j]; // 把 dd[下标 j]; 写入 dd[i]
  dd[j] = t; // 把 另一字符串; 写入 dd[j]
  var l = i + 1, r = m - 1; // 把 下标 i 加 1, 右指针 赋值为 映射表 减 1 存入 左指针
  while (l < r) {
    // 循环，直到不满足「左指针 小于 右指针」
    final t2 = dd[l]; // 把 dd[左指针] 存入 t2
    dd[l] = dd[r]; // 把 dd[右指针]; 写入 dd[l]
    dd[r] = t2; // 把 t2; 写入 dd[r]
    l++; // 左指针 加一
    r--; // 右指针 减一
  }
  var res = 0; // 把 0 存入 结果
  for (final v in dd) {
    res = res * 10 + v;
  } // 把 结果 乘 10 加 值; } 写入 for (final v in dd) { res
  return res > 2147483647 ? -1 : res; // 返回 结果 超过 2147483647 ? 减 1 : 结果
}

void main() {
  if (nextGreaterElement(12) != 21) throw StateError('c1');
  if (nextGreaterElement(21) != -1) throw StateError('c2');
  if (nextGreaterElement(1) != -1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
