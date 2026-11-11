// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
// 求直方图最大面积算法分析 — Dart 版（方案2）
int getResult(int n, List<int> h) {
  // 定义函数/方法 getResult
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  var best = 0; // 把 0 存入 当前最优
  for (var i = 0; i <= h.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 不超过 h.长度 就继续
    final cur = i < h.length ? h[i] : 0; // 把 下标 i 小于 h.长度 ? h[下标 i] : 0 存入 当前值
    while (st.isNotEmpty && h[st.last] >= cur) {
      // 循环，直到不满足「st.isNotEmpty 且 h[st.last] 不低于 当前值」
      final t = h[st.removeLast()]; // 把 h[st.removeLast()] 存入 另一字符串
      final left = st.isEmpty
          ? -1
          : st.last; // 把 st.isEmpty ? 减 1 : st.last 存入 左边界
      final width = i - left - 1; // 把 下标 i 减 左边界 减 1 存入 width
      final area = t * width; // 把 另一字符串 乘 width 存入 area
      if (area > best) best = area; // 若 area 超过 当前最优) 当前最优 赋值为 area;
    }
    st.add(i); // st 追加 下标 i);
  }
  return best; // 返回 当前最优
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (getResult(5, [0, 2, 3, 3, 3, 2, 0]) != 10) throw StateError('c1');
  if (getResult(6, [0, 2, 1, 5, 6, 2, 3, 0]) != 10) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
