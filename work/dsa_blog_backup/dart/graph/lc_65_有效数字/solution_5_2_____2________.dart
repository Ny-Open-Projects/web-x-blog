// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — Dart 版

/// 方案5（确定有限状态自动机 DFA，其余字符 lowercase）
bool isNumber(String s) {
  // 定义判定函数 isNumber
  const graph = <int, Map<String, int>>{
    // 把 小于 int, Map 小于 String, int 超过 超过 { 存入 graph
    0: {'blank': 0, 'sign': 1, '.': 2, 'digit': 6},
    1: {'digit': 6, '.': 2},
    2: {'digit': 3},
    3: {'digit': 3, 'e': 4},
    4: {'digit': 5, 'sign': 7},
    5: {'digit': 5},
    6: {'digit': 6, '.': 3, 'e': 4},
    7: {'digit': 5},
  };
  var state = 0; // 把 0 存入 state
  for (final ch in s.trim().split('')) {
    // for (final 字符 in 字符串.trim().split('')) {
    final code = ch.codeUnitAt(0); // 把 字符.codeUnitAt(0) 存入 code
    final String c; // final String 字符;
    if (code >= 0x30 && code <= 0x39) {
      // 若 code 不低于 0x30 且 code 不超过 0x39
      c = 'digit'; // 把 'digit' 存入 字符
    } else if (ch == ' ') {
      // 否则，若 字符 等于 ' '
      c = 'blank'; // 把 'blank' 存入 字符
    } else if (ch == '+' || ch == '-') {
      // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
      c = 'sign'; // 把 'sign' 存入 字符
    } else {
      // 否则
      c = ch.toLowerCase(); // 把 字符.toLowerCase() 存入 字符
    }
    final ns = graph[state]![c]; // 把 graph[state]取反 [字符] 存入 ns
    if (ns == null) return false; // 若 ns 等于 null，直接返回 false
    state = ns; // 把 ns 存入 state
  }
  return state == 3 ||
      state == 5 ||
      state == 6; // 返回 state 等于 3 或 state 等于 5 或 state 等于 6
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (isNumber('0') != true) throw StateError("isNumber('0') should be true");
  if (isNumber('abc') != false) {
    // 若 isNumber('abc') 不等于 false
    throw StateError(
      "isNumber('abc') should be false",
    ); // throw StateError(「isNumber('abc') should be false」);
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
