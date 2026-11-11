// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
// LeetCode 1329. 将矩阵按对角线排序 — Dart 版

/// 方案2：优化版 —— 按 r-c 分组收集对角线，升序排序，写回时按 shift（取队首）取值
List<List<int>> diagonalSort(List<List<int>> mat) {
  // 定义函数/方法 diagonalSort
  final rows = mat.length,
      cols = mat[0].length; // 把 mat.长度, 列数 赋值为 mat[0].长度 存入 行数
  final diags = <int, List<int>>{}; // 把 小于 int, List 小于 int 超过 超过 {} 存入 diags
  for (var r = 0; r < rows; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    for (var c = 0; c < cols; c++) {
      // 让 字符 从 0 开始计数，字符 小于 列数 就继续
      diags.putIfAbsent(r - c, () => <int>[]).add(mat[r][c]);
    }
  }
  for (final arr in diags.values) {
    // for (final 数组 in diags.values) {
    arr.sort(); // 排序
  }
  final pos = <int, int>{}; // 把 小于 int, int 超过 {} 存入 pos
  for (var r = 0; r < rows; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    for (var c = 0; c < cols; c++) {
      // 让 字符 从 0 开始计数，字符 小于 列数 就继续
      final key = r - c; // 把 右指针 减 字符 存入 key
      final p = pos.update(key, (v) => v + 1, ifAbsent: () => 0);
      mat[r][c] = diags[key]![p]; // 把 diags[key]取反 [节点]; 写入 mat[r][c]
    }
  }
  return mat; // 返回 mat
}

bool eqMatrix(List<List<int>> a, List<List<int>> b) {
  // 定义函数/方法 eqMatrix
  if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i].length != b[i].length)
      return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
    for (var j = 0; j < a[i].length; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
      if (a[i][j] != b[i][j])
        return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
    }
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致（输入深拷贝，等价于 m.map(r => r.slice())）
  final m = <List<int>>[
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2],
  ];
  final input = m.map((r) => r.toList()).toList();
  final exp = <List<int>>[
    [1, 1, 1, 1],
    [1, 2, 2, 2],
    [1, 2, 3, 3],
  ];
  final got = diagonalSort(input); // 把 diagonalSort(input) 存入 got
  if (!eqMatrix(got, exp)) {
    // 若 取反 eqMatrix(got, exp
    throw StateError('FAILED'); // throw StateError('FAILED');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
