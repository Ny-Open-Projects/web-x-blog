// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189
// LeetCode 3. 无重复字符的最长子串 — Dart 版（方案5）
int lengthOfLongestSubstring(String s) {
  // 定义函数/方法 lengthOfLongestSubstring
  final set = <String>{}; // 把 小于 String 超过 {} 存入 set
  var left = 0; // 把 0 存入 左边界
  var maxLen = 0; // 把 0 存入 maxLen
  for (var right = 0; right < s.length; right++) {
    // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度 就继续
    final c = s[right]; // 把 字符串[右边界] 存入 字符
    while (set.contains(c)) {
      // 循环，直到不满足「set 是否包含 字符」
      set.remove(s[left]); // set 弹出 字符串[左边界]);
      left++; // 左边界 加一
    }
    set.add(c); // set 追加 字符);
    final len = right - left + 1; // 把 右边界 减 左边界 加 1 存入 长度
    if (len > maxLen) maxLen = len; // 若 长度 超过 maxLen) maxLen 赋值为 长度;
  }
  return maxLen; // 返回 maxLen
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (lengthOfLongestSubstring('abcabcbb') != 3) throw StateError('c1');
  if (lengthOfLongestSubstring('bbbbb') != 1) throw StateError('c2');
  if (lengthOfLongestSubstring('pwwkew') != 3) throw StateError('c3');
  if (lengthOfLongestSubstring('') != 0) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
