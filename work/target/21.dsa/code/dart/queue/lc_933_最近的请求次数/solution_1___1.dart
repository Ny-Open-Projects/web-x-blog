// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — Dart 版

// 方案1：push + 真出队（removeAt(0) 等价 TS 数组 shift）
class RecentCounter {
  // 定义类型
  final _q = <int>[]; // 把 小于 int 超过 [] 存入 _q

  int ping(int t) {
    // 定义函数/方法 ping
    _q.add(t); // _q 追加 另一字符串);
    while (_q.isNotEmpty && _q.first < t - 3000) {
      // 循环，直到不满足「_q.isNotEmpty 且 _q.first 小于 另一字符串 减 3000」
      _q.removeAt(0); // 真出队
    }
    return _q.length; // 返回 _q.长度
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致
  final c = RecentCounter(); // 把 RecentCounter() 存入 字符
  final got = [c.ping(1), c.ping(100), c.ping(3001), c.ping(3002)];
  final want = [1, 2, 3, 3]; // 把 [1, 2, 3, 3] 存入 want
  for (var i = 0; i < want.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
    if (got[i] != want[i]) {
      // 若 got[下标 i] 不等于 want[下标 i]
      throw StateError('FAIL case $i got ${got[i]} want ${want[i]}');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
