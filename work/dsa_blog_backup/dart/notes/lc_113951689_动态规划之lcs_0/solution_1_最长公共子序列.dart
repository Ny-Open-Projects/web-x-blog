// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — Dart 版（最长公共子序列：DP 填表 + 回溯构造）
List<List<int>> lcsTable(String a, String b) {
  // 定义函数/方法 lcsTable
  final m = a.length, n = b.length; // 把 数组.长度, 元素个数 赋值为 b.长度 存入 映射表
  final dp = List.generate(m + 1, (_) => List<int>.filled(n + 1, 0));
  for (var i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (var j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      if (a[i - 1] == b[j - 1]) {
        // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
        dp[i][j] =
            dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
      } else {
        // 否则
        dp[i][j] = dp[i - 1][j] >= dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
      }
    }
  }
  return dp; // 返回 DP 表
}

int lcsLength(String a, String b) {
  // 定义函数/方法 lcsLength
  final dp = lcsTable(a, b); // 把 lcsTable(数组, b) 存入 DP 表
  return dp[a.length][b.length]; // 返回 DP 表[数组.长度][b.长度]
}

String lcsString(String a, String b) {
  // 定义函数/方法 lcsString
  final dp = lcsTable(a, b); // 把 lcsTable(数组, b) 存入 DP 表
  var i = a.length, j = b.length; // 把 数组.长度, 下标 j 赋值为 b.长度 存入 下标 i
  final out = StringBuffer(); // 把 StringBuffer() 存入 out
  final stack = <String>[]; // 把 小于 String 超过 [] 存入 栈
  while (i > 0 && j > 0) {
    // 循环，直到不满足「下标 i 超过 0 且 下标 j 超过 0」
    if (a[i - 1] == b[j - 1]) {
      // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
      stack.add(a[i - 1]); // 栈 追加 数组[下标 i 减 1]);
      i--; // 下标 i 减一
      j--; // 下标 j 减一
    } else if (dp[i - 1][j] >= dp[i][j - 1]) {
      // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
      i--; // 下标 i 减一
    } else {
      // 否则
      j--; // 下标 j 减一
    }
  }
  for (var k = stack.length - 1; k >= 0; k--) {
    // 让 下标 k 从 栈.长度 减 1 开始计数，下标 k 不低于 0 就继续
    out.write(stack[k]); // out.write(栈[下标 k]);
  }
  return out.toString(); // 返回 out.toString()
}

bool isCommonSub(String a, String b, String s) {
  // 定义判定函数 isCommonSub
  var ia = 0, ib = 0; // 把 0, ib 赋值为 0 存入 ia
  for (var k = 0; k < s.length; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 字符串.长度 就继续
    final ch = s[k]; // 把 字符串[下标 k] 存入 字符
    while (ia < a.length && a[ia] != ch) {
      // 循环，直到不满足「ia 小于 数组.长度 且 数组[ia] 不等于 字符」
      ia++; // ia 加一
    }
    while (ib < b.length && b[ib] != ch) {
      // 循环，直到不满足「ib 小于 b.长度 且 b[ib] 不等于 字符」
      ib++; // ib 加一
    }
    if (ia >= a.length || ib >= b.length)
      return false; // 若 ia 不低于 数组.长度 或 ib 不低于 b.长度，直接返回 false
    ia++; // ia 加一
    ib++; // ib 加一
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<dynamic>>[
    ['ABCBDAB', 'BDCABA', 4],
    ['AGGTAB', 'GXTXAYB', 4],
    ['abc', 'abc', 3],
    ['', 'abc', 0],
    ['abc', 'xyz', 0],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    final got = lcsLength(
      c[0] as String,
      c[1] as String,
    ); // 把 lcsLength(字符[0] as String, 字符[1] as String) 存入 got
    if (got != c[2] as int) {
      // 若 got 不等于 字符[2] as int
      throw StateError('case $idx failed: got $got want ${c[2]}');
    }
  }
  for (final p in [
    ['ABCBDAB', 'BDCABA'],
    ['AGGTAB', 'GXTXAYB'],
  ]) {
    final s = lcsString(
      p[0] as String,
      p[1] as String,
    ); // 把 lcsString(节点[0] as String, 节点[1] as String) 存入 字符串
    if (s.length != lcsLength(p[0] as String, p[1] as String) ||
        !isCommonSub(p[0] as String, p[1] as String, s)) {
      // 取反 isCommonSub(节点[0] as String, 节点[1] as String, 字符串)) {
      throw StateError(
        'lcsString failed: $s',
      ); // throw StateError('lcsString failed: $字符串');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
