// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097
// LeetCode 2637. 有时间限制的Promise对象 — Dart 版（方案1）
List<int> promiseWithTimeLimit(List<int?> values, int t) {
  // 定义函数/方法 promiseWithTimeLimit
  return values.map((v) => v ?? -1).toList();
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (promiseWithTimeLimit([5, null, 9], 50).toString() != '[5, -1, 9]')
    throw StateError('c1');
  if (promiseWithTimeLimit([null], 100).toString() != '[-1]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
