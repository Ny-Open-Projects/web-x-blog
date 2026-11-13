// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
// LeetCode 417. 太平洋大西洋水流问题 — Dart 版

/// 方案2（DFS 反向流动，从海洋边界出发）
List<List<int>> pacificAtlantic(List<List<int>>? matrix) {
  // 定义函数/方法 pacificAtlantic
  if (matrix == null || matrix.isEmpty || matrix[0].isEmpty)
    return []; // 若 矩阵 等于 null 或 矩阵.isEmpty 或 矩阵[0].isEmpty，直接返回 []
  final m = matrix.length; // 把 矩阵.长度 存入 映射表
  final n = matrix[0].length; // 把 矩阵[0].长度 存入 元素个数
  final pacific = List.generate(m, (_) => List.filled(n, false));
  final atlantic = List.generate(m, (_) => List.filled(n, false));

  void dfs(int r, int c, List<List<bool>> flow) {
    // 定义函数/方法 dfs
    flow[r][c] = true; // 把 true; 写入 flow[r][c]
    const dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    for (final d in dirs) {
      // for (final d in dirs) {
      final nr = r + d[0]; // 把 右指针 加 d[0] 存入 nr
      final nc = c + d[1]; // 把 字符 加 d[1] 存入 nc
      if (nr >= 0 &&
          nr < m &&
          nc >= 0 &&
          nc < n &&
          !flow[nr][nc] &&
          matrix[nr][nc] >= matrix[r][c]) {
        // 把 矩阵[右指针][字符]) { 写入 matrix[nr][nc] >
        dfs(nr, nc, flow); // dfs(nr, nc, flow);
      }
    }
  }

  for (var r = 0; r < m; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
    dfs(r, 0, pacific); // dfs(右指针, 0, pacific);
    dfs(r, n - 1, atlantic); // dfs(右指针, 元素个数 减 1, atlantic);
  }
  for (var c = 0; c < n; c++) {
    // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
    dfs(0, c, pacific); // dfs(0, 字符, pacific);
    dfs(m - 1, c, atlantic); // dfs(映射表 减 1, 字符, atlantic);
  }

  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  for (var r = 0; r < m; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
    for (var c = 0; c < n; c++) {
      // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (pacific[r][c] && atlantic[r][c])
        res.add([
          r,
          c,
        ]); // 若 pacific[右指针][字符] 且 atlantic[右指针][字符]) 结果 追加 [右指针, 字符]);
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
  ]); // ]);
  const expected = [
    [0, 4],
    [1, 3],
    [1, 4],
    [2, 2],
    [3, 0],
    [3, 1],
    [4, 0],
  ];
  if (got.length != expected.length)
    throw StateError(
      'length mismatch',
    ); // 若 got.长度 不等于 expected.长度) throw StateError('长度 mismatch');
  for (var i = 0; i < expected.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 expected.长度 就继续
    if (got[i][0] != expected[i][0] || got[i][1] != expected[i][1]) {
      throw StateError(
        'cell mismatch at $i',
      ); // throw StateError('cell mismatch at $下标 i');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
