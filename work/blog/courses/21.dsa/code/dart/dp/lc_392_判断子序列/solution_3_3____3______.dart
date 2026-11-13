// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613
// LeetCode 392. 判断子序列 — Dart 版（方案3）
bool isSubsequence(String s, String t) {
  // 定义判定函数 isSubsequence
  var i = 0; // 把 0 存入 下标 i
  for (final c in t.split('')) {
    // for (final 字符 in 另一字符串.split('')) {
    if (i < s.length && s[i] == c)
      i++; // 若 下标 i 小于 字符串.长度 且 字符串[下标 i] 等于 字符) 下标 i 加一 ;
  }
  return i == s.length; // 返回 下标 i 等于 字符串.长度
}

void main() {
  if (!isSubsequence('abc', 'ahbgdc')) throw StateError('c1');
  if (isSubsequence('axc', 'ahbgdc')) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
