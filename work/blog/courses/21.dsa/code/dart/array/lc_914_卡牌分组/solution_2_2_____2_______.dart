// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324
// LeetCode 914. 卡牌分组 — Dart 版（方案2）
int gcd(int a, int b) {
  while (b != 0) {
    final t = a % b;
    a = b;
    b = t;
  }
  return a;
}

bool hasGroupsSizeX(List<int> deck) {
  // 定义函数/方法 hasGroupsSizeX
  final counts = <int, int>{}; // 把 小于 int, int 超过 {} 存入 counts
  for (final c in deck) {
    counts[c] = (counts[c] ?? 0) + 1;
  }
  var g = 0; // 把 0 存入 g
  for (final v in counts.values) {
    g = gcd(g, v);
  } // 把 gcd(g, 值); } 写入 for (final v in counts.values) { g
  return g >= 2; // 返回 g 不低于 2
}

void main() {
  if (!hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])) throw StateError('c1');
  if (hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])) throw StateError('c2');
  if (hasGroupsSizeX([1])) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
