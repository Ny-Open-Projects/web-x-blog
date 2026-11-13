// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996
// LeetCode 225. 用队列实现栈 — Dart 版（方案1）
class MyStack {
  // 定义类型
  final List<int> q = []; // 把 []; 写入 final List<int> q
  void push(int x) {
    q.insert(0, x);
  } // void push(int x) { 节点 插入 0, x); }

  int pop() {
    final v = q.removeAt(0);
    return v;
  } // 把 节点.removeAt(0); return 值; } 写入 int pop() { final v

  int top() => q.first;
  bool empty() => q.isEmpty;
}

void main() {
  // 程序入口：跑内嵌自测用例
  final ms = MyStack(); // 把 MyStack() 存入 ms
  ms.push(1);
  ms.push(2); // 把 1 压入栈/数组尾部
  if (ms.top() != 2)
    throw StateError('c1'); // 若 ms.top() 不等于 2) throw StateError('c1');
  if (ms.pop() != 2)
    throw StateError('c2'); // 若 ms 弹出 ) 不等于 2) throw StateError('c2');
  if (ms.empty()) throw StateError('c3'); // 若 ms 是否为空) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
