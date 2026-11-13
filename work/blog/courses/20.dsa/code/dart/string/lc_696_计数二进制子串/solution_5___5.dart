// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434
// LeetCode 696. 计数二进制子串 — Dart 版（方案5）
int countBinarySubstrings(String s) {
  // 定义函数/方法 countBinarySubstrings
  final groups = <int>[]; // 把 小于 int 超过 [] 存入 groups
  var i = 0; // 把 0 存入 下标 i
  final n = s.length; // 把 字符串.长度 存入 元素个数
  while (i < n) {
    // 循环，直到不满足「下标 i 小于 元素个数」
    final ch = s[i]; // 把 字符串[下标 i] 存入 字符
    var cnt = 0; // 把 0 存入 计数
    while (i < n && s[i] == ch) {
      // 循环，直到不满足「下标 i 小于 元素个数 且 字符串[下标 i] 等于 字符」
      cnt++; // 计数 加一
      i++; // 下标 i 加一
    }
    groups.add(cnt); // groups 追加 计数);
  }
  var ans = 0; // 把 0 存入 答案
  for (var k = 1; k < groups.length; k++) {
    // 让 下标 k 从 1 开始计数，下标 k 小于 groups.长度 就继续
    ans += groups[k - 1] < groups[k] ? groups[k - 1] : groups[k];
  }
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (countBinarySubstrings('00110011') != 6) throw StateError('c1');
  if (countBinarySubstrings('10101') != 4) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
