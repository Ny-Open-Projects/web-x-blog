// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913
// LeetCode 739. 每日温度 — Dart 版（方案2）
List<int> dailyTemperatures(List<int> temps) {
  // 定义函数/方法 dailyTemperatures
  final n = temps.length; // 把 temps.长度 存入 元素个数
  final res = List<int>.filled(n, 0); // 把 List 小于 int 超过 .filled(元素个数, 0) 存入 结果
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    while (st.isNotEmpty && temps[st.last] < temps[i]) {
      // 循环，直到不满足「st.isNotEmpty 且 temps[st.last] 小于 temps[下标 i]」
      final idx = st.removeLast(); // 把 st.removeLast() 存入 idx
      res[idx] = i - idx; // 把 下标 i 减 idx; 写入 res[idx]
    }
    st.add(i); // st 追加 下标 i);
  }
  return res; // 返回 结果
}

void main() {
  if (dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]).toString() !=
      '[1, 1, 4, 2, 1, 1, 0, 0]')
    throw StateError('c1');
  if (dailyTemperatures([30, 40, 50, 60]).toString() != '[1, 1, 1, 0]')
    throw StateError('c2');
  if (dailyTemperatures([30, 60, 90]).toString() != '[1, 1, 0]')
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
