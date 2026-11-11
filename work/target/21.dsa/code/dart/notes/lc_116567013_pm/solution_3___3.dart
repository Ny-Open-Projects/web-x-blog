// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Dart 版（方案3：KMP，next 表失配大步跳跃）
List<int> buildNext(String p) {
  // 定义函数/方法 buildNext
  final m = p.length; // 把 节点.长度 存入 映射表
  final N = List<int>.filled(m, -1); // 把 List 小于 int 超过 .filled(映射表, 减 1) 存入 N
  var j = 0, t = -1; // 把 0, 另一字符串 赋值为 减 1 存入 下标 j
  while (j < m - 1) {
    // 循环，直到不满足「下标 j 小于 映射表 减 1」
    if (t < 0 || p[j] == p[t]) {
      // 若 另一字符串 小于 0 或 节点[下标 j] 等于 节点[另一字符串]
      j++;
      t++; // 下标 j 加一 ; 另一字符串 加一 ;
      N[j] = t; // 把 另一字符串; 写入 N[j]
    } else {
      // 否则
      t = N[t]; // 把 N[另一字符串] 存入 另一字符串
    }
  }
  return N; // 返回 N
}

int kmpMatch(String p, String t) {
  // 定义函数/方法 kmpMatch
  final N = buildNext(p); // 把 buildNext(节点) 存入 N
  final n = t.length, m = p.length; // 把 另一字符串.长度, 映射表 赋值为 节点.长度 存入 元素个数
  var i = 0, j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
  while (j < m && i < n) {
    // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
    if (j < 0 || t[i] == p[j]) {
      // 若 下标 j 小于 0 或 另一字符串[下标 i] 等于 节点[下标 j]
      i++;
      j++; // 下标 i 加一 ; 下标 j 加一 ;
    } else {
      // 否则
      j = N[j]; // 把 N[下标 j] 存入 下标 j
    }
  }
  return j == m ? i - j : -1; // 返回 下标 j 等于 映射表 ? 下标 i 减 下标 j : 减 1
}

bool eqArr(List<int> a, List<int> b) {
  // 定义函数/方法 eqArr
  if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  const T = 'now is the time for all good people to come'; // 把 'now is the time for all good people to come' 存入 T
  final cases = <List<dynamic>>[
    ['people', T, 29],
    ['all', T, 20],
    ['no', T, 0],
    ['xyz', T, -1],
    ['a', '', -1],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    if (kmpMatch(c[0] as String, c[1] as String) != c[2] as int) {
      throw StateError(
        'case $idx failed',
      ); // throw StateError('case $idx failed');
    }
  }
  if (kmpMatch('aaaa', 'aaaaa') != 0) throw StateError('overlap failed');
  if (kmpMatch('aaab', 'aaabaaa') != 0) throw StateError('reuse failed');
  if (!eqArr(buildNext('ababaca'), [-1, 0, 0, 1, 2, 3, 0]))
    throw StateError('next ababaca failed');
  if (!eqArr(buildNext('aaaa'), [-1, 0, 1, 2]))
    throw StateError('next aaaa failed');
  if (!eqArr(buildNext('abcd'), [-1, 0, 0, 0]))
    throw StateError('next abcd failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
