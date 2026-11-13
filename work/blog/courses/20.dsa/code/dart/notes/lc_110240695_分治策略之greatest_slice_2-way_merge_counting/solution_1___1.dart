// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案A：暴力枚举所有子段）
int maxSubArrayBf(List<int> arr) {
  // 定义函数/方法 maxSubArrayBf
  var best = 0; // 把 0 存入 当前最优
  var first = true; // 把 true 存入 first
  for (var i = 0; i < arr.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    var s = 0; // 把 0 存入 字符串
    for (var j = i; j < arr.length; j++) {
      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 数组.长度 就继续
      s += arr[j]; // 字符串累加 数组[下标 j]
      if (first || s > best) {
        // 若 first 或 字符串 超过 当前最优
        best = s; // 把 字符串 存入 当前最优
        first = false; // 把 false 存入 first
      }
    }
  }
  return best; // 返回 当前最优
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<int>, int>{
    // 把 小于 List 小于 int 超过 , int 超过 { 存入 cases
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]: 6,
    [1]: 1,
    [-1, -2, -3]: -1,
    [5, 4, -1, 7, 8]: 23,
  };
  var idx = 0; // 把 0 存入 idx
  cases.forEach((arr, want) {
    // cases.forEach((数组, want) {
    if (maxSubArrayBf(arr) != want) throw StateError('case $idx failed');
    idx++; // idx 加一
  }); // });
  print('PASS'); // 全部用例通过，输出 PASS
}
