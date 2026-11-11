// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — Dart 版

// 方案2：front 指针懒删除（不真正移除元素，仅移动队头下标）
class RecentCounter {
  // 定义类型
  final _queue = <int>[]; // 把 小于 int 超过 [] 存入 _queue
  int _front = 0; // 把 0 存入 _front

  int ping(int t) {
    // 定义函数/方法 ping
    _queue.add(t); // _queue 追加 另一字符串);
    while (_queue[_front] < t - 3000) {
      // 循环，直到不满足「_queue[_front] 小于 另一字符串 减 3000」
      _front++; // _front 加一
    }
    return _queue.length - _front; // 返回 _queue.长度 减 _front
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
