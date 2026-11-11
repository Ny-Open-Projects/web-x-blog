// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838
// LeetCode 242. 有效的字母异位词 — Dart 版（方案2）
bool isAnagram(String s, String t) {
  // 定义判定函数 isAnagram
  if (s.length != t.length) return false; // 若 字符串.长度 不等于 另一字符串.长度，直接返回 false
  final a = s.split('')..sort(); // 把 字符串.split(''). 排序 ) 存入 数组
  final b = t.split('')..sort(); // 把 另一字符串.split(''). 排序 ) 存入 b
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!isAnagram('anagram', 'nagaram')) throw StateError('c1');
  if (isAnagram('rat', 'car'))
    throw StateError(
      'c2',
    ); // 若 isAnagram('rat', 'car')) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
