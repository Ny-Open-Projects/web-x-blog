// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462
// LeetCode 605. 种花问题 — Dart 版（方案7）
bool canPlaceFlowers(List<int> bed, int n) {
  // 定义函数/方法 canPlaceFlowers
  final v = List<int>.from(bed); // 把 List 小于 int 超过 .from(bed) 存入 值
  var count = 0; // 把 0 存入 计数
  for (var i = 0; i < v.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 值.长度 就继续
    final leftOk =
        i == 0 || v[i - 1] == 0; // 把 下标 i 等于 0 或 值[下标 i 减 1] 等于 0 存入 leftOk
    final rightOk =
        i == v.length - 1 ||
        v[i + 1] == 0; // 把 下标 i 等于 值.长度 减 1 或 值[下标 i 加 1] 等于 0 存入 rightOk
    if (v[i] == 0 && leftOk && rightOk) {
      // 若 值[下标 i] 等于 0 且 leftOk 且 rightOk
      v[i] = 1; // 把 1; 写入 v[i]
      count++; // 计数 加一
    }
  }
  return count >= n; // 返回 计数 不低于 元素个数
}

void main() {
  if (!canPlaceFlowers([1, 0, 0, 0, 1], 1)) throw StateError('c1');
  if (canPlaceFlowers([1, 0, 0, 0, 1], 2)) throw StateError('c2');
  if (!canPlaceFlowers([0, 0, 1, 0, 0], 1)) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
