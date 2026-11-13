// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595
// LeetCode 295. 数据流的中位数 — Dart 版（方案2）
class MedianFinder {
  // 定义类型
  final List<int> _items = []; // 把 []; 写入 final List<int> _items
  void addNum(int num) {
    // 定义函数/方法 addNum
    var pos = 0; // 把 0 存入 pos
    while (pos < _items.length && _items[pos] < num) {
      // 循环，直到不满足「pos 小于 _items.长度 且 _items[pos] 小于 num」
      pos++; // pos 加一
    }
    _items.insert(pos, num); // _items 插入 pos, num);
  }

  double findMedian() {
    // 定义函数/方法 findMedian
    final n = _items.length; // 把 _items.长度 存入 元素个数
    if (n % 2 == 1)
      return _items[n ~/ 2]
          .toDouble(); // 若 元素个数 对…取模 2 等于 1，直接返回 _items[元素个数 ~ 除以 2].toDouble()
    return (_items[n ~/ 2 - 1] + _items[n ~/ 2]) /
        2; // 返回 (_items[元素个数 ~ 除以 2 减 1] 加 _items[元素个数 ~ 除以 2]) 除以 2
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final mf = MedianFinder(); // 把 MedianFinder() 存入 mf
  for (final x in [1, 2, 3, 4, 5]) {
    // for (final x in [1, 2, 3, 4, 5]) {
    mf.addNum(x); // mf.addNum(x);
  }
  if (mf.findMedian() != 3.0)
    throw StateError(
      'c1',
    ); // 若 mf.findMedian() 不等于 3.0) throw StateError('c1');
  final mf2 = MedianFinder(); // 把 MedianFinder() 存入 mf2
  mf2.addNum(1); // mf2.addNum(1);
  mf2.addNum(2); // mf2.addNum(2);
  if (mf2.findMedian() != 1.5)
    throw StateError(
      'c2',
    ); // 若 mf2.findMedian() 不等于 1.5) throw StateError('c2');
  mf2.addNum(3); // mf2.addNum(3);
  if (mf2.findMedian() != 2.0)
    throw StateError(
      'c3',
    ); // 若 mf2.findMedian() 不等于 2.0) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
