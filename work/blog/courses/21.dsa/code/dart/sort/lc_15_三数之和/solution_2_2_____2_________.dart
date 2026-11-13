// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474
// LeetCode 15. 三数之和 — Dart 版（方案2）
List<List<int>> threeSum(List<int> nums) {
  // 定义函数/方法 threeSum
  final arr = List<int>.from(nums)
    ..sort(); // 把 List 小于 int 超过 .from(数组). 排序 ) 存入 数组
  final ans = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 答案
  final n = arr.length; // 把 数组.长度 存入 元素个数
  for (var first = 0; first < n; first++) {
    // 让 first 从 0 开始计数，first 小于 元素个数 就继续
    if (first > 0 && arr[first] == arr[first - 1])
      continue; // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1]) continue;
    var third = n - 1; // 把 元素个数 减 1 存入 third
    final target = -arr[first]; // 把 减 数组[first] 存入 目标值
    for (var second = first + 1; second < n; second++) {
      // 让 second 从 first 加 1 开始计数，second 小于 元素个数 就继续
      if (second > first + 1 && arr[second] == arr[second - 1]) continue;
      while (second < third && arr[second] + arr[third] > target) third--;
      if (second == third) break; // 若 second 等于 third) break;
      if (arr[second] + arr[third] == target) {
        // 若 数组[second] 加 数组[third] 等于 目标值
        ans.add([
          arr[first],
          arr[second],
          arr[third],
        ]); // 答案 追加 [数组[first], 数组[second], 数组[third]]);
      }
    }
  }
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = threeSum([
    -1,
    0,
    1,
    2,
    -1,
    -4,
  ]); // 把 threeSum([ 减 1, 0, 1, 2, 减 1, 减 4]) 存入 got
  if (got.length != 2)
    throw StateError('cnt'); // 若 got.长度 不等于 2) throw StateError('计数');
  if (got[0].toString() != '[-1, -1, 2]' || got[1].toString() != '[-1, 0, 1]')
    throw StateError('t');
  final g2 = threeSum([0, 0, 0]); // 把 threeSum([0, 0, 0]) 存入 g2
  if (g2.length != 1 || g2[0].toString() != '[0, 0, 0]') throw StateError('z');
  print('PASS'); // 全部用例通过，输出 PASS
}
