// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
// LeetCode 面试题 03.05. 栈排序 — Dart 版（方案2）
List<int> sortedStack(List<int> input) {
  // 定义函数/方法 sortedStack
  final stk = List<int>.from(input); // 把 List 小于 int 超过 .from(input) 存入 栈
  final temp = <int>[]; // 把 小于 int 超过 [] 存入 临时变量
  final output = <int>[]; // 把 小于 int 超过 [] 存入 输出
  while (stk.isNotEmpty) {
    // 循环，直到不满足「栈.isNotEmpty」
    final v = stk.removeLast(); // 把 栈.removeLast() 存入 值
    while (temp.isNotEmpty && temp.last > v) {
      // 循环，直到不满足「临时变量.isNotEmpty 且 临时变量.last 超过 值」
      output.add(temp.removeLast()); // 输出 追加 临时变量.removeLast());
    }
    temp.add(v); // 临时变量 追加 值);
  }
  while (temp.isNotEmpty) {
    // 循环，直到不满足「临时变量.isNotEmpty」
    output.add(temp.removeLast()); // 输出 追加 临时变量.removeLast());
  }
  output.sort(); // 排序
  return output; // 返回 输出
}

void main() {
  if (sortedStack([5, 2, 1, 4, 3]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
