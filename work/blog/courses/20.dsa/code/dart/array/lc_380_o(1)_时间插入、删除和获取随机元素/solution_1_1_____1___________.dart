// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301
// LeetCode 380. O(1)时间插入删除和获取随机元素 — Dart 版（方案1）
import 'dart:math'; // 引入依赖

class RandomizedSet {
  // 定义类型
  final List<int> vals = []; // 把 []; 写入 final List<int> vals
  final Map<int, int> pos = {}; // 把 {}; 写入 final Map<int, int> pos
  bool insert(int val) {
    // 定义函数/方法 insert
    if (pos.containsKey(val)) return false; // 若 pos.containsKey(值)，直接返回 false
    pos[val] = vals.length; // 把 vals.长度; 写入 pos[val]
    vals.add(val); // vals 追加 值);
    return true; // 返回 true
  }

  bool remove(int val) {
    // 定义函数/方法 remove
    final idx = pos[val]; // 把 pos[值] 存入 idx
    if (idx == null) return false; // 若 idx 等于 null，直接返回 false
    final last = vals.last; // 把 vals.last 存入 last
    vals[idx] = last; // 把 last; 写入 vals[idx]
    pos[last] = idx; // 把 idx; 写入 pos[last]
    vals.removeLast(); // vals.removeLast();
    pos.remove(val); // pos 弹出 值);
    return true; // 返回 true
  }

  int getRandom() => vals[Random().nextInt(vals.length)];
}

void main() {
  // 程序入口：跑内嵌自测用例
  final s = RandomizedSet(); // 把 RandomizedSet() 存入 字符串
  if (!s.insert(1))
    throw StateError('c1'); // 若 取反 字符串 插入 1)) throw StateError('c1');
  if (s.remove(2))
    throw StateError('c2'); // 若 字符串 弹出 2)) throw StateError('c2');
  if (!s.insert(2))
    throw StateError('c3'); // 若 取反 字符串 插入 2)) throw StateError('c3');
  final r = s.getRandom(); // 把 字符串.getRandom() 存入 右指针
  if (r != 1 && r != 2)
    throw StateError('c4'); // 若 右指针 不等于 1 且 右指针 不等于 2) throw StateError('c4');
  if (!s.remove(1))
    throw StateError('c5'); // 若 取反 字符串 弹出 1)) throw StateError('c5');
  if (s.insert(2))
    throw StateError('c6'); // 若 字符串 插入 2)) throw StateError('c6');
  if (s.getRandom() != 2)
    throw StateError('c7'); // 若 字符串.getRandom() 不等于 2) throw StateError('c7');
  print('PASS');
} // 全部用例通过，输出 PASS
