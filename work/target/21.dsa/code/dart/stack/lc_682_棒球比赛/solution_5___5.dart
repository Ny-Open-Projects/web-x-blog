// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
// LeetCode 682. 棒球比赛 — Dart 版（方案5）
int calPoints(List<String> ops) {
  // 定义函数/方法 calPoints
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (final op in ops) {
    // for (final op in ops) {
    if (op == '+') {
      // 若 op 等于 ' 加 '
      st.add(
        st[st.length - 1] + st[st.length - 2],
      ); // st 追加 st[st.长度 减 1] 加 st[st.长度 减 2]);
    } else if (op == 'D') {
      // 否则，若 op 等于 'D'
      st.add(st.last * 2); // st 追加 st.last 乘 2);
    } else if (op == 'C') {
      // 否则，若 op 等于 'C'
      st.removeLast(); // st.removeLast();
    } else {
      // 否则
      st.add(int.parse(op)); // st 追加 int.parse(op));
    }
  }
  var sum = 0; // 把 0 存入 累计和
  for (final v in st) {
    sum += v;
  } // 把 值; } 写入 for (final v in st) { sum +
  return sum; // 返回 累计和
}

void main() {
  if (calPoints(['5', '2', 'C', 'D', '+']) != 30) throw StateError('c1');
  if (calPoints(['5', '-2', '4', 'C', 'D', '9', '+', '+']) != 27)
    throw StateError('c2');
  if (calPoints(['1', 'C']) != 0) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
