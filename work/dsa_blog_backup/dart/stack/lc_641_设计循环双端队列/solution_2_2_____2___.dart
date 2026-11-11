// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774
// LeetCode 641. 设计循环双端队列 — Dart 版（方案2）
class MyCircularDeque {
  // 定义类型
  final List<int> data; // final List 小于 int 超过 data;
  int head = 0, tail = 0, size = 0; // 把 0, 尾节点 赋值为 0, 大小 赋值为 0 存入 头节点
  final int cap; // final int cap;
  MyCircularDeque(this.cap) : data = List<int>.filled(cap, 0);
  bool insertFront(int v) {
    // 定义函数/方法 insertFront
    if (size == cap) return false; // 若 大小 等于 cap，直接返回 false
    head = (head + cap - 1) % cap; // 把 (头节点 加 cap 减 1) 对…取模 cap 存入 头节点
    data[head] = v; // 把 值; 写入 data[head]
    size++; // 大小 加一
    return true; // 返回 true
  }

  bool insertLast(int v) {
    // 定义函数/方法 insertLast
    if (size == cap) return false; // 若 大小 等于 cap，直接返回 false
    data[tail] = v; // 把 值; 写入 data[tail]
    tail = (tail + 1) % cap; // 把 (尾节点 加 1) 对…取模 cap 存入 尾节点
    size++; // 大小 加一
    return true; // 返回 true
  }

  bool deleteFront() {
    // 定义函数/方法 deleteFront
    if (size == 0) return false; // 若 大小 等于 0，直接返回 false
    head = (head + 1) % cap; // 把 (头节点 加 1) 对…取模 cap 存入 头节点
    size--; // 大小 减一
    return true; // 返回 true
  }

  bool deleteLast() {
    // 定义函数/方法 deleteLast
    if (size == 0) return false; // 若 大小 等于 0，直接返回 false
    tail = (tail + cap - 1) % cap; // 把 (尾节点 加 cap 减 1) 对…取模 cap 存入 尾节点
    size--; // 大小 减一
    return true; // 返回 true
  }

  int getFront() => size == 0 ? -1 : data[head];
  int getRear() => size == 0 ? -1 : data[(tail + cap - 1) % cap];
  bool isEmpty() => size == 0;
  bool isFull() => size == cap;
}

void main() {
  // 程序入口：跑内嵌自测用例
  final d = MyCircularDeque(3); // 把 MyCircularDeque(3) 存入 d
  if (!d.insertLast(1))
    throw StateError('c1'); // 若 取反 d.insertLast(1)) throw StateError('c1');
  if (!d.insertLast(2))
    throw StateError('c2'); // 若 取反 d.insertLast(2)) throw StateError('c2');
  if (!d.insertFront(3))
    throw StateError('c3'); // 若 取反 d.insertFront(3)) throw StateError('c3');
  if (d.insertFront(4))
    throw StateError('c4'); // 若 d.insertFront(4)) throw StateError('c4');
  if (d.getRear() != 2)
    throw StateError('c5'); // 若 d.getRear() 不等于 2) throw StateError('c5');
  if (!d.isFull())
    throw StateError('c6'); // 若 取反 d.isFull()) throw StateError('c6');
  if (!d.deleteLast())
    throw StateError('c7'); // 若 取反 d.deleteLast()) throw StateError('c7');
  if (!d.insertFront(4))
    throw StateError('c8'); // 若 取反 d.insertFront(4)) throw StateError('c8');
  if (d.getFront() != 4)
    throw StateError('c9'); // 若 d.getFront() 不等于 4) throw StateError('c9');
  print('PASS');
} // 全部用例通过，输出 PASS
