// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359
// LeetCode 337. 打家劫舍III — Dart 版（方案2）
int robTree(List<int?> vals) {
  // 定义函数/方法 robTree
  if (vals.isEmpty) return 0; // 若 vals.isEmpty，直接返回 0
  List<int> dfs(int i) {
    // 定义函数/方法 dfs
    if (i >= vals.length || vals[i] == null)
      return [0, 0]; // 若 下标 i 不低于 vals.长度 或 vals[下标 i] 等于 null，直接返回 [0, 0]
    final l = dfs(2 * i + 1); // 把 dfs(2 乘 下标 i 加 1) 存入 左指针
    final r = dfs(2 * i + 2); // 把 dfs(2 乘 下标 i 加 2) 存入 右指针
    final include =
        vals[i]! + l[1] + r[1]; // 把 vals[下标 i]取反 加 左指针[1] 加 右指针[1] 存入 include
    final exclude = (l[0] > l[1] ? l[0] : l[1]) + (r[0] > r[1] ? r[0] : r[1]);
    return [include, exclude]; // 返回 [include, exclude]
  }

  final r = dfs(0); // 把 dfs(0) 存入 右指针
  return r[0] > r[1] ? r[0] : r[1]; // 返回 右指针[0] 超过 右指针[1] ? 右指针[0] : 右指针[1]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (robTree([3, 2, 3, null, 3, null, 1]) != 7) throw StateError('c1');
  if (robTree([3, 4, 5, 1, 3, null, 1]) != 9) throw StateError('c2');
  if (robTree([]) != 0)
    throw StateError('c3'); // 若 robTree([]) 不等于 0) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
