// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案B：增量扫描）
int maxSubArrayIc(List<int> arr) {
  // 定义函数/方法 maxSubArrayIc
  if (arr.isEmpty) return 0; // 若 数组.isEmpty，直接返回 0
  var gs = arr[0]; // 把 数组[0] 存入 gs
  for (var i = 0; i < arr.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    var s = 0; // 把 0 存入 字符串
    for (var j = i; j < arr.length; j++) {
      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 数组.长度 就继续
      s += arr[j]; // 字符串累加 数组[下标 j]
      if (gs < s) gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
    }
  }
  return gs; // 返回 gs
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (maxSubArrayIc([-2, 1, -3, 4, -1, 2, 1]) != 6)
    throw StateError('ms1 failed');
  if (maxSubArrayIc([-1, -2, -3]) != -1) throw StateError('ms2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
