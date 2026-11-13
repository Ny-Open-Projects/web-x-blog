// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
// LeetCode 622. 设计循环队列 — Dart 版

// 方案5：数组 + front/rear/size 循环队列
class MyCircularQueue {
  // 定义类型
  final int capacity; // final int capacity;
  final List<int> data; // final List 小于 int 超过 data;
  int front; // int front;
  int rear; // int rear;
  int size; // int 大小;

  MyCircularQueue(int k) // MyCircularQueue(int 下标 k)
    : capacity = k,
      data = List<int>.filled(k, 0),
      front = 0,
      rear = 0,
      size = 0; // 把 0 存入 大小

  bool enQueue(int value) {
    // 定义函数/方法 enQueue
    if (isFull()) return false; // 若 isFull()，直接返回 false
    data[rear] = value; // 把 value; 写入 data[rear]
    rear = (rear + 1) % capacity; // 把 (rear 加 1) 对…取模 capacity 存入 rear
    size += 1; // 大小累加 1
    return true; // 返回 true
  }

  bool deQueue() {
    // 定义函数/方法 deQueue
    if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
    front = (front + 1) % capacity; // 把 (front 加 1) 对…取模 capacity 存入 front
    size -= 1; // 大小累减 1
    return true; // 返回 true
  }

  int Front() {
    // 定义函数/方法 Front
    if (isEmpty()) return -1; // 若 isEmpty()，直接返回 减 1
    return data[front]; // 返回 data[front]
  }

  int Rear() {
    // 定义函数/方法 Rear
    if (isEmpty()) return -1; // 若 isEmpty()，直接返回 减 1
    return data[(rear - 1 + capacity) %
        capacity]; // 返回 data[(rear 减 1 加 capacity) 对…取模 capacity]
  }

  bool isEmpty() => size == 0;
  bool isFull() => size == capacity;
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致
  final q = MyCircularQueue(3); // 把 MyCircularQueue(3) 存入 节点
  final got = <Object>[
    q.enQueue(1),
    q.enQueue(2),
    q.enQueue(3),
    q.enQueue(4),
    q.Rear(),
    q.isFull(),
    q.deQueue(),
    q.enQueue(4),
    q.Rear(),
  ];
  final want = <Object>[true, true, true, false, 3, true, true, true, 4];
  if (got.length != want.length) {
    // 若 got.长度 不等于 want.长度
    throw StateError(
      'FAIL length got ${got.length}',
    ); // throw StateError('FAIL 长度 got ${got.长度}');
  }
  for (var i = 0; i < want.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
    if (got[i] != want[i]) {
      // 若 got[下标 i] 不等于 want[下标 i]
      throw StateError('FAIL idx $i got ${got[i]} want ${want[i]}');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
