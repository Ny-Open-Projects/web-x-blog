// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案C：分治 best/prefix/suffix/total）
List<int> helper(List<int> arr, int lo, int hi) {
  // 定义函数/方法 helper
  if (hi - lo == 1) {
    // 若 右边界 减 左边界 等于 1
    final v = arr[lo]; // 把 数组[左边界] 存入 值
    return [v, v, v, v]; // 返回 [值, 值, 值, 值]
  }
  final mi = (lo + hi) ~/ 2; // 把 (左边界 加 右边界) ~ 除以 2 存入 mi
  final l = helper(arr, lo, mi); // 把 helper(数组, 左边界, mi) 存入 左指针
  final r = helper(arr, mi, hi); // 把 helper(数组, mi, 右边界) 存入 右指针
  final crossing = l[2] + r[1]; // 把 左指针[2] 加 右指针[1] 存入 crossing
  final best = [l[0], r[0], crossing].reduce((a, b) => a > b ? a : b);
  final prefix = l[1] > l[3] + r[1] ? l[1] : l[3] + r[1];
  final suffix = r[2] > r[3] + l[2] ? r[2] : r[3] + l[2];
  return [
    best,
    prefix,
    suffix,
    l[3] + r[3],
  ]; // 返回 [当前最优, prefix, suffix, 左指针[3] 加 右指针[3]]
}

int maxSubArrayDc(List<int> arr) {
  // 定义函数/方法 maxSubArrayDc
  if (arr.isEmpty) return 0; // 若 数组.isEmpty，直接返回 0
  return helper(arr, 0, arr.length)[0]; // 返回 helper(数组, 0, 数组.长度)[0]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (maxSubArrayDc([-2, 1, -3, 4, -1, 2, 1]) != 6)
    throw StateError('ms1 failed');
  if (maxSubArrayDc([1, 2, 3]) != 6) throw StateError('ms2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
