// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547
// LeetCode 384. 打乱数组 — Dart 版（方案1）
import 'dart:math'; // 引入依赖

class ShuffleArray {
  // 定义类型
  final List<int> orig; // final List 小于 int 超过 orig;
  List<int> cur; // List 小于 int 超过 当前值;
  ShuffleArray(this.orig) : cur = List<int>.from(orig);
  List<int> reset() {
    cur = List<int>.from(orig);
    return cur;
  }

  List<int> shuffle() {
    // 定义函数/方法 shuffle
    final n = cur.length; // 把 当前值.长度 存入 元素个数
    for (var i = n - 1; i > 0; i--) {
      // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 0 就继续
      final j = Random().nextInt(i + 1); // 把 Random().nextInt(下标 i 加 1) 存入 下标 j
      final t = cur[i]; // 把 当前值[下标 i] 存入 另一字符串
      cur[i] = cur[j]; // 把 当前值[下标 j]; 写入 cur[i]
      cur[j] = t; // 把 另一字符串; 写入 cur[j]
    }
    return cur; // 返回 当前值
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final sa = ShuffleArray([1, 2, 3]); // 把 ShuffleArray([1, 2, 3]) 存入 sa
  final sh = sa.shuffle(); // 把 sa.shuffle() 存入 sh
  if (sh.length != 3)
    throw StateError('len'); // 若 sh.长度 不等于 3) throw StateError('长度');
  final sorted = List<int>.from(sh)
    ..sort(); // 把 List 小于 int 超过 .from(sh). 排序 ) 存入 sorted
  if (sorted.toString() != '[1, 2, 3]') throw StateError('perm');
  final r = sa.reset(); // 把 sa.reset() 存入 右指针
  if (r.toString() != '[1, 2, 3]')
    throw StateError(
      'reset',
    ); // 若 右指针.toString() 不等于 '[1, 2, 3]') throw StateError('reset');
  print('PASS');
} // 全部用例通过，输出 PASS
