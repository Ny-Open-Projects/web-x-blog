// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527
// LeetCode 125. 验证回文串 — Dart 版（方案2）
bool isPalindrome(String s) {
  // 定义判定函数 isPalindrome
  final f = s.replaceAll(RegExp('[^a-zA-Z0-9]'), '').toLowerCase();
  var i = 0, j = f.length - 1; // 把 0, 下标 j 赋值为 f.长度 减 1 存入 下标 i
  while (i < j) {
    // 循环，直到不满足「下标 i 小于 下标 j」
    if (f[i] != f[j]) return false; // 若 f[下标 i] 不等于 f[下标 j]，直接返回 false
    i++; // 下标 i 加一
    j--; // 下标 j 减一
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!isPalindrome('A man, a plan, a canal: Panama')) throw StateError('c1');
  if (isPalindrome('race a car'))
    throw StateError(
      'c2',
    ); // 若 isPalindrome('race 数组 car')) throw StateError('c2');
  if (!isPalindrome(' '))
    throw StateError('c3'); // 若 取反 isPalindrome(' ')) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
