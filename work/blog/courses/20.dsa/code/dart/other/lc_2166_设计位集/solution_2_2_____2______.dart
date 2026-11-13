// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343
// LeetCode 2166. 设计位集 — Dart 版（方案2）
class Bitset {
  // 定义类型
  final int n; // final int 元素个数;
  final List<int> words; // final List 小于 int 超过 单词列表;
  int ones = 0; // 把 0 存入 ones
  int reverse = 0; // 把 0 存入 reverse
  Bitset(this.n) : words = List.filled((n + 31) ~/ 32, 0);
  int getBit(int idx) => ((words[idx >> 5] >> (idx & 31)) & 1) ^ reverse;
  void fix(int idx) {
    // 定义函数/方法 fix
    if (getBit(idx) == 0) {
      // 若 getBit(idx) 等于 0
      words[idx >> 5] |=
          1 << (idx & 31); // 把 1 小于 小于 (idx 按位与 31); 写入 words[idx >> 5] |
      ones++; // ones 加一
    }
  }

  void unfix(int idx) {
    // 定义函数/方法 unfix
    if (getBit(idx) == 1) {
      // 若 getBit(idx) 等于 1
      words[idx >> 5] &=
          ~(1 << (idx & 31)); // 把 ~(1 小于 小于 (idx 按位与 31)); 写入 words[idx >> 5] &
      ones--; // ones 减一
    }
  }

  void flip() {
    // 定义函数/方法 flip
    reverse ^= 1; // 把 1; 写入 reverse ^
    ones = n - ones; // 把 元素个数 减 ones 存入 ones
  }

  bool all() => ones == n;
  bool one() => ones > 0;
  int count() => ones;
  String toString() {
    // 定义函数/方法 toString
    final sb = StringBuffer(); // 把 StringBuffer() 存入 sb
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      sb.write(getBit(i)); // sb.write(getBit(下标 i));
    }
    return sb.toString(); // 返回 sb.toString()
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final bs = Bitset(5); // 把 Bitset(5) 存入 bs
  bs.fix(0);
  bs.fix(3); // bs.fix(0); bs.fix(3);
  if (bs.toString() != '10010')
    throw StateError(
      's1',
    ); // 若 bs.toString() 不等于 '10010') throw StateError('s1');
  if (bs.count() != 2)
    throw StateError('c1'); // 若 bs.计数() 不等于 2) throw StateError('c1');
  bs.flip(); // bs.flip();
  if (bs.toString() != '01101')
    throw StateError(
      's2',
    ); // 若 bs.toString() 不等于 '01101') throw StateError('s2');
  if (bs.count() != 3)
    throw StateError('c2'); // 若 bs.计数() 不等于 3) throw StateError('c2');
  bs.unfix(0); // bs.unfix(0);
  if (bs.toString() != '01101')
    throw StateError(
      's3',
    ); // 若 bs.toString() 不等于 '01101') throw StateError('s3');
  if (bs.all() || !bs.one())
    throw StateError('ao'); // 若 bs.all() 或 取反 bs.one()) throw StateError('ao');
  print('PASS'); // 全部用例通过，输出 PASS
}
