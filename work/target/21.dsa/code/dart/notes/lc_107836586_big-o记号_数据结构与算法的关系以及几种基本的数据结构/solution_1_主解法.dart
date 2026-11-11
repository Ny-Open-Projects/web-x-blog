// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
// LeetCode 107836586. Big-O 记号 — Dart 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
String classify(List<int> coeffs) {
  // 定义函数/方法 classify
  for (var deg = coeffs.length - 1; deg >= 0; deg--) {
    // 让 deg 从 coeffs.长度 减 1 开始计数，deg 不低于 0 就继续
    if (coeffs[deg] != 0) {
      // 若 coeffs[deg] 不等于 0
      if (deg > 1) return 'O(n^$deg)'; // 若 deg 超过 1，直接返回 'O(元素个数 按位异或 $deg)'
      if (deg == 1) return 'O(n)'; // 若 deg 等于 1，直接返回 'O(元素个数)'
      return 'O(1)'; // 返回 'O(1)'
    }
  }
  return 'O(1)'; // 返回 'O(1)'
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<int>, String>{
    // 把 小于 List 小于 int 超过 , String 超过 { 存入 cases
    [1, 0, 0, 0]: 'O(1)',
    [0, 0, 0, 35]: 'O(n^3)',
    [0, 0, 1, 0]: 'O(n^2)',
    [0, 1, 0, 0]: 'O(n)',
  };
  var idx = 0; // 把 0 存入 idx
  cases.forEach((coeffs, want) {
    // cases.forEach((coeffs, want) {
    final got = classify(coeffs); // 把 classify(coeffs) 存入 got
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++; // idx 加一
  }); // });
  print('PASS'); // 全部用例通过，输出 PASS
}
