// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412
// LeetCode 1494. 并行课程II — Dart 版（方案2）
int minNumberOfSemesters(int n, List<List<int>> relations, int k) {
  // 定义函数/方法 minNumberOfSemesters
  final prereq = List<int>.filled(
    n,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数, 0) 存入 prereq
  for (final r in relations) {
    // for (final 右指针 in relations) {
    prereq[r[1] - 1] |=
        1 << (r[0] - 1); // 把 1 小于 小于 (右指针[0] 减 1); 写入 prereq[r[1] - 1] |
  }
  int go(int done) {
    // 定义函数/方法 go
    if (done == (1 << n) - 1) return 0; // 若 done 等于 (1 小于 小于 元素个数) 减 1，直接返回 0
    var avail = 0; // 把 0 存入 avail
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if ((done & (1 << i)) == 0 && (done & prereq[i]) == prereq[i])
        avail |= 1 << i;
    }
    var cnt = 0, chosen = 0, a = avail; // 把 0, chosen 赋值为 0, 数组 赋值为 avail 存入 计数
    while (a != 0 && cnt < k) {
      // 循环，直到不满足「数组 不等于 0 且 计数 小于 下标 k」
      final low = a & (-a); // 把 数组 按位与 ( 减 数组) 存入 low
      chosen |= low; // 把 low; 写入 chosen |
      a ^= low; // 把 low; 写入 a ^
      cnt++; // 计数 加一
    }
    return 1 + go(done | chosen); // 返回 1 加 go(done 按位或 chosen)
  }

  return go(0); // 返回 go(0)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (minNumberOfSemesters(4, [
        [2, 1],
        [3, 1],
        [1, 4],
      ], 2) !=
      3)
    throw StateError('c1');
  if (minNumberOfSemesters(5, [
        [2, 1],
        [3, 1],
        [4, 1],
        [1, 5],
      ], 3) !=
      3)
    throw StateError('c2');
  if (minNumberOfSemesters(3, [], 2) != 2) throw StateError('c3');
  if (minNumberOfSemesters(4, [
        [1, 2],
        [2, 3],
      ], 1) !=
      4)
    throw StateError('c4');
  print('PASS');
} // 全部用例通过，输出 PASS
