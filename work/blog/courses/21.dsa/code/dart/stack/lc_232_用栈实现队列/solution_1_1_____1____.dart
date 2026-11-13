// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
// LeetCode 232. 用栈实现队列 — Dart 版（方案1）
class MyQueue {
  // 定义类型
  final List<int> inStack = []; // 把 []; 写入 final List<int> inStack
  final List<int> outStack = []; // 把 []; 写入 final List<int> outStack
  void in2out() {
    // 定义函数/方法 in2out
    while (inStack.isNotEmpty) {
      outStack.add(inStack.removeLast());
    }
  }

  void push(int x) {
    inStack.add(x);
  } // void push(int x) { inStack 追加 x); }

  int pop() {
    // 定义函数/方法 pop
    if (outStack.isEmpty) in2out(); // 若 outStack.isEmpty) in2out();
    return outStack.removeLast(); // 返回 outStack.removeLast()
  }

  int peek() {
    // 定义函数/方法 peek
    if (outStack.isEmpty) in2out(); // 若 outStack.isEmpty) in2out();
    return outStack.last; // 返回 outStack.last
  }

  bool empty() => inStack.isEmpty && outStack.isEmpty;
}

void main() {
  // 程序入口：跑内嵌自测用例
  final mq = MyQueue(); // 把 MyQueue() 存入 mq
  mq.push(1);
  mq.push(2); // 把 1 压入栈/数组尾部
  if (mq.peek() != 1)
    throw StateError('c1'); // 若 mq.peek() 不等于 1) throw StateError('c1');
  if (mq.pop() != 1)
    throw StateError('c2'); // 若 mq 弹出 ) 不等于 1) throw StateError('c2');
  if (mq.empty()) throw StateError('c3'); // 若 mq 是否为空) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
