// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886
// LeetCode 165. 比较版本号 — Dart 版（方案1）
int compareVersion(String v1, String v2) {
  // 定义函数/方法 compareVersion
  final p1 = v1
      .split('.')
      .map(int.parse)
      .toList(); // 把 v1.split('.').映射表(int.parse).toList() 存入 p1
  final p2 = v2
      .split('.')
      .map(int.parse)
      .toList(); // 把 v2.split('.').映射表(int.parse).toList() 存入 p2
  final n = p1.length > p2.length
      ? p1.length
      : p2.length; // 把 p1.长度 超过 p2.长度 ? p1.长度 : p2.长度 存入 元素个数
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    final a = i < p1.length ? p1[i] : 0; // 把 下标 i 小于 p1.长度 ? p1[下标 i] : 0 存入 数组
    final b = i < p2.length ? p2[i] : 0; // 把 下标 i 小于 p2.长度 ? p2[下标 i] : 0 存入 b
    if (a < b) return -1; // 若 数组 小于 b，直接返回 减 1
    if (a > b) return 1; // 若 数组 超过 b，直接返回 1
  }
  return 0; // 返回 0
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (compareVersion('1.01', '1.001') != 0) throw StateError('c1');
  if (compareVersion('1.0', '1.0.0') != 0) throw StateError('c2');
  if (compareVersion('0.1', '1.1') != -1) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
