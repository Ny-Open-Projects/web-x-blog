// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435
// LeetCode 3105. 最长的严格递增或递减子数组 — Dart 版（方案3）
int longestMonotonicSubarray(List<int> nums) {
  // 定义函数/方法 longestMonotonicSubarray
  if (nums.isEmpty) return 0; // 若 数组.isEmpty，直接返回 0
  var inc = 1, dec = 1, best = 1; // 把 1, dec 赋值为 1, 当前最优 赋值为 1 存入 inc
  for (var i = 1; i < nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    if (nums[i] > nums[i - 1]) {
      inc++;
      dec = 1;
    } // 若 数组[下标 i] 超过 数组[下标 i 减 1]) { inc 加一 ; dec 赋值为 1; }
    else if (nums[i] < nums[i - 1]) {
      dec++;
      inc = 1;
    } // 否则，若 数组[下标 i] 小于 数组[下标 i 减 1]) { dec 加一 ; inc 赋值为 1; }
    else {
      inc = 1;
      dec = 1;
    } // 否则
    if (inc > best) best = inc; // 若 inc 超过 当前最优) 当前最优 赋值为 inc;
    if (dec > best) best = dec; // 若 dec 超过 当前最优) 当前最优 赋值为 dec;
  }
  return best; // 返回 当前最优
}

void main() {
  if (longestMonotonicSubarray([1, 2, 3, 4, 5]) != 5) throw StateError('c1');
  if (longestMonotonicSubarray([5, 4, 3, 2, 1]) != 5) throw StateError('c2');
  if (longestMonotonicSubarray([1, 4, 3, 2, 5]) != 3) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
