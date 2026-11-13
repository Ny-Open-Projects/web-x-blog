// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538
// LeetCode 58. 最后一个单词的长度 — Dart 版（方案1）
int lengthOfLastWord(String s) {
  // 定义函数/方法 lengthOfLastWord
  var end = s.length - 1; // 把 字符串.长度 减 1 存入 终点
  while (end >= 0 && s[end] == ' ')
    end--; // 循环，直到不满足「终点 不低于 0 且 字符串[终点] 等于 ' ') 终点 减一 ;」
  if (end < 0) return 0; // 若 终点 小于 0，直接返回 0
  var start = end; // 把 终点 存入 起点
  while (start >= 0 && s[start] != ' ')
    start--; // 循环，直到不满足「起点 不低于 0 且 字符串[起点] 不等于 ' ') 起点 减一 ;」
  return end - start; // 返回 终点 减 起点
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (lengthOfLastWord('Hello World') != 5) throw StateError('c1');
  if (lengthOfLastWord(' ') != 0)
    throw StateError(
      'c2',
    ); // 若 lengthOfLastWord(' ') 不等于 0) throw StateError('c2');
  if (lengthOfLastWord('a') != 1)
    throw StateError(
      'c3',
    ); // 若 lengthOfLastWord('数组') 不等于 1) throw StateError('c3');
  if (lengthOfLastWord(' fly me to the moon ') != 4) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
