// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317
// LeetCode 18. 四数之和 — Dart 版（方案2）
List<List<int>> fourSum(List<int> nums, int target) {
  // 定义函数/方法 fourSum
  final arr = List<int>.from(nums)
    ..sort(); // 把 List 小于 int 超过 .from(数组). 排序 ) 存入 数组
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  final n = arr.length; // 把 数组.长度 存入 元素个数
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (i > 0 && arr[i] == arr[i - 1])
      continue; // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
    for (var j = i + 1; j < n; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
      if (j > i + 1 && arr[j] == arr[j - 1])
        continue; // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]) continue;
      var left = j + 1, right = n - 1; // 把 下标 j 加 1, 右边界 赋值为 元素个数 减 1 存入 左边界
      while (left < right) {
        // 循环，直到不满足「左边界 小于 右边界」
        final s =
            arr[i] +
            arr[j] +
            arr[left] +
            arr[right]; // 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 字符串
        if (s == target) {
          // 若 字符串 等于 目标值
          res.add([
            arr[i],
            arr[j],
            arr[left],
            arr[right],
          ]); // 结果 追加 [数组[下标 i], 数组[下标 j], 数组[左边界], 数组[右边界]]);
          left++; // 左边界 加一
          right--; // 右边界 减一
          while (left < right && arr[left] == arr[left - 1])
            left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 等于 数组[左边界 减 1]) 左边界 加一 ;」
          while (left < right && arr[right] == arr[right + 1])
            right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 等于 数组[右边界 加 1]) 右边界 减一 ;」
        } else if (s < target) {
          // 否则，若 字符串 小于 目标值
          left++; // 左边界 加一
        } else {
          // 否则
          right--; // 右边界 减一
        }
      }
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (fourSum([1, 0, -1, 0, -2, 2], 0).length != 3) throw StateError('c1');
  print('PASS'); // 全部用例通过，输出 PASS
}
