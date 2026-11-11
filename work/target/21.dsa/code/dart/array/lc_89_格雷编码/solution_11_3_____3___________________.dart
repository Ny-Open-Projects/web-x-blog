// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839
// LeetCode 89. 格雷编码 — Dart 版（方案11）
List<int> grayCode(int n) {
  // 定义函数/方法 grayCode
  final m = 1 << n; // 把 1 小于 小于 元素个数 存入 映射表
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  for (var i = 0; i < m; i++) {
    out.add(i ^ (i >> 1));
  } // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
  return out; // 返回 out
}

void main() {
  if (grayCode(2).toString() != '[0, 1, 3, 2]') throw StateError('c1');
  if (grayCode(1).toString() != '[0, 1]') throw StateError('c2');
  if (grayCode(3).length != 8) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
