// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752
// LeetCode 234. 回文链表 — Dart 版（方案3）
bool isPalindromeList(List<int> v) {
  // 定义判定函数 isPalindromeList
  var i = 0, j = v.length - 1; // 把 0, 下标 j 赋值为 值.长度 减 1 存入 下标 i
  while (i < j) {
    // 循环，直到不满足「下标 i 小于 下标 j」
    if (v[i] != v[j]) return false; // 若 值[下标 i] 不等于 值[下标 j]，直接返回 false
    i++; // 下标 i 加一
    j--; // 下标 j 减一
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!isPalindromeList([]))
    throw StateError(
      'c0',
    ); // 若 取反 isPalindromeList([])) throw StateError('c0');
  if (!isPalindromeList([1, 2, 2, 1]))
    throw StateError(
      'c1',
    ); // 若 取反 isPalindromeList([1, 2, 2, 1])) throw StateError('c1');
  if (isPalindromeList([1, 2]))
    throw StateError(
      'c2',
    ); // 若 isPalindromeList([1, 2])) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
