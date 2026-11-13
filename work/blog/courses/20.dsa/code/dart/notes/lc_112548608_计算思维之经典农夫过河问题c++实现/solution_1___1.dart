// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
// LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）

bool invalid(List<int> st) {
  // 定义函数/方法 invalid
  final h = st[0],
      w = st[1],
      s = st[2],
      v = st[3]; // 把 st[0], 权重 赋值为 st[1], 字符串 赋值为 st[2], 值 赋值为 st[3] 存入 h
  if (h != s && s == w) return true; // 若 h 不等于 字符串 且 字符串 等于 权重，直接返回 true
  if (h != s && s == v) return true; // 若 h 不等于 字符串 且 字符串 等于 值，直接返回 true
  return false; // 返回 false
}

const roleIdx = {
  'W': 1,
  'S': 2,
  'V': 3,
}; // 把 {'W': 1, 'S': 2, 'V': 3} 存入 roleIdx

List<String> solveFarmer() {
  // 定义函数/方法 solveFarmer
  final path = <String>[]; // 把 小于 String 超过 [] 存入 当前路径
  final visited = <String>{}; // 把 小于 String 超过 {} 存入 已访问集合

  bool go(List<int> st) {
    // 定义函数/方法 go
    if (st[0] == 1 && st[1] == 1 && st[2] == 1 && st[3] == 1) return true;
    final key = st.join(','); // 把 st.join(',') 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    for (final role in ['-', 'W', 'S', 'V']) {
      // for (final role in [' 减 ', 'W', 'S', 'V']) {
      final ns = List<int>.from(st); // 把 List 小于 int 超过 .from(st) 存入 ns
      ns[0] = 1 - ns[0]; // 农夫总是过河
      if (role != '-') {
        // 若 role 不等于 ' 减 '
        final idx = roleIdx[role]!; // 把 roleIdx[role]取反 存入 idx
        if (st[0] != st[idx]) continue; // 出发前同岸
        ns[idx] = 1 - ns[idx]; // 把 1 减 ns[idx]; 写入 ns[idx]
      }
      if (invalid(ns)) continue; // 若 invalid(ns)) continue;
      if (go(ns)) {
        // 若 go(ns
        path.add(role); // 当前路径 追加 role);
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  go(<int>[0, 0, 0, 0]); // go( 小于 int 超过 [0, 0, 0, 0]);
  return path.reversed.toList(); // 返回 当前路径.reversed.toList()
}

bool simulate(List<String> path) {
  // 定义函数/方法 simulate
  final st = <int>[0, 0, 0, 0]; // 把 小于 int 超过 [0, 0, 0, 0] 存入 st
  for (final role in path) {
    // for (final role in 当前路径) {
    final before = List<int>.from(st); // 把 List 小于 int 超过 .from(st) 存入 before
    st[0] = 1 - st[0]; // 把 1 减 st[0]; 写入 st[0]
    if (role != '-') {
      // 若 role 不等于 ' 减 '
      final idx = roleIdx[role]!; // 把 roleIdx[role]取反 存入 idx
      if (before[0] != before[idx])
        return false; // 若 before[0] 不等于 before[idx]，直接返回 false
      st[idx] = 1 - st[idx]; // 把 1 减 st[idx]; 写入 st[idx]
    }
    if (invalid(st)) return false; // 若 invalid(st)，直接返回 false
  }
  return st[0] == 1 &&
      st[1] == 1 &&
      st[2] == 1 &&
      st[3] == 1; // 返回 st[0] 等于 1 且 st[1] 等于 1 且 st[2] 等于 1 且 st[3] 等于 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  final wantPath = <String>['S', '-', 'W', 'S', 'V', '-', 'S'];
  final wantReadable =
      'HS H HW HS HV H HS'; // 把 'HS H HW HS HV H HS' 存入 wantReadable

  final gotPath = solveFarmer(); // 把 solveFarmer() 存入 gotPath

  // case1: 路径一致
  if (gotPath.toString() != wantPath.toString()) {
    // 若 gotPath.toString() 不等于 wantPath.toString(
    throw StateError('FAIL path mismatch: ' + gotPath.toString());
  }

  // case2: 可读方案串
  final gotReadable = gotPath.map((r) => r != '-' ? 'H' + r : 'H').join(' ');
  if (gotReadable != wantReadable) {
    // 若 gotReadable 不等于 wantReadable
    throw StateError(
      'FAIL readable: ' + gotReadable,
    ); // throw StateError('FAIL readable: ' 加 gotReadable);
  }

  // case3: 7 步
  if (gotPath.length != 7)
    throw StateError(
      'FAIL steps',
    ); // 若 gotPath.长度 不等于 7) throw StateError('FAIL steps');

  // case4: 模拟校验
  if (!simulate(gotPath))
    throw StateError(
      'FAIL simulate',
    ); // 若 取反 simulate(gotPath)) throw StateError('FAIL simulate');

  print('PASS'); // 全部用例通过，输出 PASS
}
