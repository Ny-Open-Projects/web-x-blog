// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
// 实现LRU缓存算法功能 — Dart 版（方案2）
class NoteLru {
  // 定义类型
  final int cap; // final int cap;
  final List<int> keys = []; // 把 []; 写入 final List<int> keys
  final Map<int, int> vals = {}; // 把 {}; 写入 final Map<int, int> vals
  NoteLru(this.cap); // NoteLru(this.cap);
  int get(int k) {
    // 定义函数/方法 get
    if (vals.containsKey(k)) {
      // 若 vals.containsKey(下标 k
      keys.remove(k); // keys 弹出 下标 k);
      keys.add(k); // keys 追加 下标 k);
      return vals[k]!; // 返回 vals[下标 k]取反
    }
    return -1; // 返回 减 1
  }

  void put(int k, int v) {
    // 定义函数/方法 put
    if (vals.containsKey(k)) {
      // 若 vals.containsKey(下标 k
      keys.remove(k); // keys 弹出 下标 k);
    } else if (keys.length == cap) {
      // 否则，若 keys.长度 等于 cap
      vals.remove(keys.removeAt(0)); // vals 弹出 keys.removeAt(0));
    }
    keys.add(k); // keys 追加 下标 k);
    vals[k] = v; // 把 值; 写入 vals[k]
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final c = NoteLru(2); // 把 NoteLru(2) 存入 字符
  c.put(1, 1); // 字符.put(1, 1);
  c.put(2, 2); // 字符.put(2, 2);
  if (c.get(1) != 1)
    throw StateError('c1'); // 若 字符 查找 1) 不等于 1) throw StateError('c1');
  c.put(3, 3); // 字符.put(3, 3);
  if (c.get(2) != -1)
    throw StateError('c2'); // 若 字符 查找 2) 不等于 减 1) throw StateError('c2');
  c.put(4, 4); // 字符.put(4, 4);
  if (c.get(1) != -1)
    throw StateError('c3'); // 若 字符 查找 1) 不等于 减 1) throw StateError('c3');
  if (c.get(3) != 3 || c.get(4) != 4)
    throw StateError(
      'c4',
    ); // 若 字符 查找 3) 不等于 3 或 字符 查找 4) 不等于 4) throw StateError('c4');
  print('PASS');
} // 全部用例通过，输出 PASS
