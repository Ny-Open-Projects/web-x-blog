// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891
// LeetCode 460. LFU缓存 — Dart 版（方案1）
class LfuSim {
  // 定义类型
  final int cap; // final int cap;
  final Map<int, int> vals = {}; // 把 {}; 写入 final Map<int, int> vals
  final Map<int, int> freq = {}; // 把 {}; 写入 final Map<int, int> freq
  final Map<int, int> stamp = {}; // 把 {}; 写入 final Map<int, int> stamp
  int clock = 0; // 把 0 存入 clock
  LfuSim(this.cap); // LfuSim(this.cap);
  int get(int k) {
    // 定义函数/方法 get
    clock++; // clock 加一
    if (vals.containsKey(k)) {
      // 若 vals.containsKey(下标 k
      freq[k] = freq[k]! + 1; // 把 频次表[下标 k]取反 加 1; 写入 freq[k]
      stamp[k] = clock; // 把 clock; 写入 stamp[k]
      return vals[k]!; // 返回 vals[下标 k]取反
    }
    return -1; // 返回 减 1
  }

  void put(int k, int v) {
    // 定义函数/方法 put
    clock++; // clock 加一
    if (vals.containsKey(k)) {
      // 若 vals.containsKey(下标 k
      vals[k] = v; // 把 值; 写入 vals[k]
      freq[k] = freq[k]! + 1; // 把 频次表[下标 k]取反 加 1; 写入 freq[k]
      stamp[k] = clock; // 把 clock; 写入 stamp[k]
      return; // return;
    }
    if (cap == 0) return; // 若 cap 等于 0) return;
    if (vals.length == cap) {
      // 若 vals.长度 等于 cap
      var evict = -1,
          bestF = -1,
          bestS = -1; // 把 减 1, bestF 赋值为 减 1, bestS 赋值为 减 1 存入 evict
      for (final k2 in vals.keys) {
        // for (final k2 in vals.keys) {
        final f = freq[k2]!,
            s = stamp[k2]!; // 把 频次表[k2]取反 , 字符串 赋值为 stamp[k2]取反 存入 f
        if (evict == -1 || f < bestF || (f == bestF && s < bestS)) {
          // 若 evict 等于 减 1 或 f 小于 bestF 或 (f 等于 bestF 且 字符串 小于 bestS
          evict = k2; // 把 k2 存入 evict
          bestF = f; // 把 f 存入 bestF
          bestS = s; // 把 字符串 存入 bestS
        }
      }
      vals.remove(evict); // vals 弹出 evict);
      freq.remove(evict); // 频次表 弹出 evict);
      stamp.remove(evict); // stamp 弹出 evict);
    }
    vals[k] = v; // 把 值; 写入 vals[k]
    freq[k] = 1; // 把 1; 写入 freq[k]
    stamp[k] = clock; // 把 clock; 写入 stamp[k]
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final lfu = LfuSim(2); // 把 LfuSim(2) 存入 lfu
  lfu.put(1, 1); // lfu.put(1, 1);
  lfu.put(2, 2); // lfu.put(2, 2);
  if (lfu.get(1) != 1)
    throw StateError('c1'); // 若 lfu 查找 1) 不等于 1) throw StateError('c1');
  lfu.put(3, 3); // lfu.put(3, 3);
  if (lfu.get(2) != -1)
    throw StateError('c2'); // 若 lfu 查找 2) 不等于 减 1) throw StateError('c2');
  if (lfu.get(3) != 3)
    throw StateError('c3'); // 若 lfu 查找 3) 不等于 3) throw StateError('c3');
  lfu.put(4, 4); // lfu.put(4, 4);
  if (lfu.get(1) != -1)
    throw StateError('c4'); // 若 lfu 查找 1) 不等于 减 1) throw StateError('c4');
  if (lfu.get(3) != 3 || lfu.get(4) != 4)
    throw StateError(
      'c5',
    ); // 若 lfu 查找 3) 不等于 3 或 lfu 查找 4) 不等于 4) throw StateError('c5');
  print('PASS'); // 全部用例通过，输出 PASS
}
