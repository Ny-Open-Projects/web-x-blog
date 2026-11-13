// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383
// LeetCode 164. 最大间距 — Dart 版（方案7）
int maximumGap(List<int> nums) {
  // 定义函数/方法 maximumGap
  final n = nums.length; // 把 数组.长度 存入 元素个数
  if (n < 2) return 0; // 若 元素个数 小于 2，直接返回 0
  var minVal = nums[0], maxVal = nums[0]; // 把 数组[0], maxVal 赋值为 数组[0] 存入 minVal
  for (final x in nums) {
    // for (final x in 数组) {
    if (x < minVal) minVal = x; // 若 x 小于 minVal) minVal 赋值为 x;
    if (x > maxVal) maxVal = x; // 若 x 超过 maxVal) maxVal 赋值为 x;
  }
  if (minVal == maxVal) return 0; // 若 minVal 等于 maxVal，直接返回 0
  var d =
      (maxVal - minVal) ~/ (n - 1); // 把 (maxVal 减 minVal) ~ 除以 (元素个数 减 1) 存入 d
  if (d < 1) d = 1; // 若 d 小于 1) d 赋值为 1;
  final bucketSize =
      (maxVal - minVal) ~/ d +
      1; // 把 (maxVal 减 minVal) ~ 除以 d 加 1 存入 bucketSize
  final buckets = List.generate(bucketSize, (_) => <int>[-1, -1]);
  for (final x in nums) {
    // for (final x in 数组) {
    final idx = (x - minVal) ~/ d; // 把 (x 减 minVal) ~ 除以 d 存入 idx
    if (buckets[idx][0] == -1) {
      // 若 buckets[idx][0] 等于 减 1
      buckets[idx][0] = x; // 把 x; 写入 buckets[idx][0]
      buckets[idx][1] = x; // 把 x; 写入 buckets[idx][1]
    } else {
      // 否则
      if (x < buckets[idx][0])
        buckets[idx][0] = x; // 若 x 小于 buckets[idx][0]) buckets[idx][0] 赋值为 x;
      if (x > buckets[idx][1])
        buckets[idx][1] = x; // 若 x 超过 buckets[idx][1]) buckets[idx][1] 赋值为 x;
    }
  }
  var ans = 0; // 把 0 存入 答案
  var prevMax = -1; // 把 减 1 存入 prevMax
  for (final b in buckets) {
    // for (final b in buckets) {
    if (b[0] == -1) continue; // 若 b[0] 等于 减 1) continue;
    if (prevMax != -1 && b[0] - prevMax > ans) ans = b[0] - prevMax;
    prevMax = b[1]; // 把 b[1] 存入 prevMax
  }
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (maximumGap([1, 2, 3]) != 1)
    throw StateError(
      'c1',
    ); // 若 maximumGap([1, 2, 3]) 不等于 1) throw StateError('c1');
  if (maximumGap([3, 6, 9, 1]) != 3)
    throw StateError(
      'c2',
    ); // 若 maximumGap([3, 6, 9, 1]) 不等于 3) throw StateError('c2');
  if (maximumGap([10]) != 0)
    throw StateError('c3'); // 若 maximumGap([10]) 不等于 0) throw StateError('c3');
  if (maximumGap([]) != 0)
    throw StateError('c4'); // 若 maximumGap([]) 不等于 0) throw StateError('c4');
  if (maximumGap([1, 10000000]) != 9999999) throw StateError('c5');
  print('PASS'); // 全部用例通过，输出 PASS
}
