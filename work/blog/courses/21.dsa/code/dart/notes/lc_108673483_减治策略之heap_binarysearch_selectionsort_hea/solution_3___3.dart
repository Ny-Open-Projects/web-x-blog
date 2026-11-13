// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Dart 版（方案3：Boyer-Moore 摩尔投票求多数元素）
int majorityElement(List<int> arr) {
  // 定义函数/方法 majorityElement
  int? candidate; // int? candidate;
  var count = 0; // 把 0 存入 计数
  for (final num in arr) {
    // for (final num in 数组) {
    if (count == 0) candidate = num; // 若 计数 等于 0) candidate 赋值为 num;
    if (num == candidate) {
      // 若 num 等于 candidate
      count++; // 计数 加一
    } else {
      // 否则
      count--; // 计数 减一
    }
  }
  var cnt = 0; // 把 0 存入 计数
  for (final num in arr) {
    // for (final num in 数组) {
    if (num == candidate) cnt++; // 若 num 等于 candidate) 计数 加一 ;
  }
  if (cnt > arr.length ~/ 2)
    return candidate!; // 若 计数 超过 数组.长度 ~ 除以 2，直接返回 candidate取反
  return -1; // 返回 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<int>, int>{
    // 把 小于 List 小于 int 超过 , int 超过 { 存入 cases
    [2, 2, 1, 1, 1, 1, 1]: 1,
    [1, 2, 3]: -1,
    [3, 3, 4]: 3,
  };
  var idx = 0; // 把 0 存入 idx
  cases.forEach((arr, want) {
    // cases.forEach((数组, want) {
    final got = majorityElement(arr); // 把 majorityElement(数组) 存入 got
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++; // idx 加一
  }); // });
  print('PASS'); // 全部用例通过，输出 PASS
}
