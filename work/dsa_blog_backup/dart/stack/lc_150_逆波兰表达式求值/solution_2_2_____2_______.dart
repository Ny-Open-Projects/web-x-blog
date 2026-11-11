// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302
// LeetCode 150. 逆波兰表达式求值 — Dart 版（方案2）
int evalRPN(List<String> tokens) {
  // 定义函数/方法 evalRPN
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (final t in tokens) {
    // for (final 另一字符串 in tokens) {
    if (t == '+' || t == '-' || t == '*' || t == '/') {
      final b = st.removeLast(); // 把 st.removeLast() 存入 b
      final a = st.removeLast(); // 把 st.removeLast() 存入 数组
      if (t == '+') {
        st.add(a + b);
      } // 若 另一字符串 等于 ' 加 ') { st 追加 数组 加 b); }
      else if (t == '-') {
        st.add(a - b);
      } // 否则，若 另一字符串 等于 ' 减 ') { st 追加 数组 减 b); }
      else if (t == '*') {
        st.add(a * b);
      } // 否则，若 另一字符串 等于 ' 乘 ') { st 追加 数组 乘 b); }
      else {
        // 否则
        final q = a / b; // 把 数组 除以 b 存入 节点
        st.add(
          q >= 0 ? q.floor() : q.ceil(),
        ); // 把 0 ? 节点.floor() : 节点.ceil()); 写入 st.add(q >
      }
    } else {
      // 否则
      st.add(int.parse(t)); // st 追加 int.parse(另一字符串));
    }
  }
  return st[0]; // 返回 st[0]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (evalRPN(['2', '1', '+', '3', '*']) != 9) throw StateError('c1');
  if (evalRPN(['4', '13', '5', '/', '+']) != 6) throw StateError('c2');
  if (evalRPN([
        '10',
        '6',
        '9',
        '3',
        '+',
        '-11',
        '*',
        '/',
        '*',
        '17',
        '+',
        '5',
        '+',
      ]) !=
      22)
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
