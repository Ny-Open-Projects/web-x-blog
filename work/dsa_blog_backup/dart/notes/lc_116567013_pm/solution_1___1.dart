// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Dart 版（方案1：Brute-Force 主串指针回退）
int matchV1(String p, String t) {
  // 定义函数/方法 matchV1
  final n = t.length, m = p.length; // 把 另一字符串.长度, 映射表 赋值为 节点.长度 存入 元素个数
  var i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
  while (j < m && i < n) {
    // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
    if (t[i] == p[j]) {
      // 若 另一字符串[下标 i] 等于 节点[下标 j]
      i++;
      j++; // 下标 i 加一 ; 下标 j 加一 ;
    } else {
      // 否则
      i -= j - 1; // 主串回退到本次对齐的下一位置
      j = 0; // 把 0 存入 下标 j
    }
  }
  return j == m ? i - j : -1; // 返回 下标 j 等于 映射表 ? 下标 i 减 下标 j : 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  const T = 'now is the time for all good people to come'; // 把 'now is the time for all good people to come' 存入 T
  final cases = <List<dynamic>>[
    ['people', T, 29],
    ['good', T, 24],
    ['xyz', T, -1],
    ['a', '', -1],
    ['is', T, 4],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    final got = matchV1(
      c[0] as String,
      c[1] as String,
    ); // 把 matchV1(字符[0] as String, 字符[1] as String) 存入 got
    if (got != c[2] as int)
      throw StateError('case $idx failed: matchV1(${c[0]})=$got want ${c[2]}');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
