// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
// 数据结构与算法之数组操作 — Dart 版（方案1）
List<int> twoSum(List<int> nums, int target) {
  // 定义函数/方法 twoSum
  for (var i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    for (var j = i + 1; j < nums.length; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 数组.长度 就继续
      if (nums[i] + nums[j] == target)
        return [i, j]; // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值，直接返回 [下标 i, 下标 j]
    }
  }
  return []; // 返回 []
}

int maxSubArray(List<int> nums) {
  // 定义函数/方法 maxSubArray
  var best = nums[0], cur = nums[0]; // 把 数组[0], 当前值 赋值为 数组[0] 存入 当前最优
  for (var i = 1; i < nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    cur = cur > 0
        ? cur + nums[i]
        : nums[i]; // 把 当前值 超过 0 ? 当前值 加 数组[下标 i] : 数组[下标 i] 存入 当前值
    if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
  }
  return best; // 返回 当前最优
}

List<int> rotateArray(List<int> nums, int k) {
  // 定义函数/方法 rotateArray
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final kk = k % n; // 把 下标 k 对…取模 元素个数 存入 kk
  return [
    ...nums.sublist(n - kk),
    ...nums.sublist(0, n - kk),
  ]; // 返回 [...数组.sublist(元素个数 减 kk), ...数组.sublist(0, 元素个数 减 kk)]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (twoSum([2, 7, 11, 15], 9).toString() != '[0, 1]') throw StateError('c1');
  if (maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) != 6) throw StateError('c2');
  if (rotateArray([1, 2, 3, 4, 5, 6, 7], 3).toString() !=
      '[5, 6, 7, 1, 2, 3, 4]')
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
