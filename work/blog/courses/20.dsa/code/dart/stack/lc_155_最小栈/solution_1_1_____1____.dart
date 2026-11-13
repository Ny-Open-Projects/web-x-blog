// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
// LeetCode 155. 最小栈 — Dart 版（方案1）
class MinStack {
  // 定义类型
  final List<int> vals = []; // 把 []; 写入 final List<int> vals
  final List<int> mins = []; // 把 []; 写入 final List<int> mins
  void push(int v) {
    // 定义函数/方法 push
    vals.add(v); // vals 追加 值);
    mins.add(mins.isEmpty ? v : (mins.last < v ? mins.last : v));
  }

  void pop() {
    vals.removeLast();
    mins.removeLast();
  } // void pop() { vals.removeLast(); mins.removeLast(); }

  int top() => vals.last;
  int getMin() => mins.last;
}

void main() {
  // 程序入口：跑内嵌自测用例
  final ms = MinStack(); // 把 MinStack() 存入 ms
  ms.push(-2);
  ms.push(0);
  ms.push(-3); // 把 减 2 压入栈/数组尾部
  if (ms.getMin() != -3)
    throw StateError('c1'); // 若 ms.getMin() 不等于 减 3) throw StateError('c1');
  ms.pop(); // 弹出栈顶元素
  if (ms.top() != 0)
    throw StateError('c2'); // 若 ms.top() 不等于 0) throw StateError('c2');
  if (ms.getMin() != -2)
    throw StateError('c3'); // 若 ms.getMin() 不等于 减 2) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
