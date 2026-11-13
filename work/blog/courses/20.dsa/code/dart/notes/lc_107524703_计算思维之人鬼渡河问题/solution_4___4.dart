// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
const D = <List<int>>[
  [2, 0],
  [1, 0],
  [1, 1],
  [0, 1],
  [0, 2],
];

bool safe(int r, int g) {
  // 定义函数/方法 safe
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

List<List<int>> solve() {
  // 定义函数/方法 solve
  final path = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 当前路径
  final visited = <String>{}; // 把 小于 String 超过 {} 存入 已访问集合

  bool jump(int dir, int r, int g, int step) {
    // 定义函数/方法 jump
    if (r == 0 && g == 0 && step % 2 == 0)
      return true; // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0，直接返回 true
    final key = '$r,$g,${step % 2}'; // 把 '$右指针,$g,${步数 对…取模 2}' 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    for (final d in D) {
      // for (final d in D) {
      final dr = d[0], dg = d[1]; // 把 d[0], dg 赋值为 d[1] 存入 dr
      final nr = r + dir * dr; // 把 右指针 加 dir 乘 dr 存入 nr
      final ng = g + dir * dg; // 把 g 加 dir 乘 dg 存入 ng
      if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
      if (jump(-dir, nr, ng, step + 1)) {
        // 若 jump( 减 dir, nr, ng, 步数 加 1
        path.add([dr, dg]); // 当前路径 追加 [dr, dg]);
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  jump(-1, 3, 3, 0); // jump( 减 1, 3, 3, 0);
  return path.reversed.toList(); // 返回 当前路径.reversed.toList()
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
  final got = solve(); // 把 solve() 存入 got
  if (got.isNotEmpty) throw StateError('FAIL: got ${got.length} moves');
  print('PASS'); // 全部用例通过，输出 PASS
}
