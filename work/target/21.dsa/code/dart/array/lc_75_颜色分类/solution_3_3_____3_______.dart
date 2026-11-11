// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756
// LeetCode 75. 颜色分类 — Dart 版（方案3）
void sortColors(List<int> nums) {
  // 定义函数/方法 sortColors
  var p0 = 0,
      cur = 0,
      p2 = nums.length - 1; // 把 0, 当前值 赋值为 0, p2 赋值为 数组.长度 减 1 存入 p0
  while (cur <= p2) {
    // 循环，直到不满足「当前值 不超过 p2」
    if (nums[cur] == 0) {
      // 若 数组[当前值] 等于 0
      final t = nums[p0]; // 把 数组[p0] 存入 另一字符串
      nums[p0] = nums[cur]; // 把 数组[当前值]; 写入 nums[p0]
      nums[cur] = t; // 把 另一字符串; 写入 nums[cur]
      p0++; // p0 加一
      cur++; // 当前值 加一
    } else if (nums[cur] == 2) {
      // 否则，若 数组[当前值] 等于 2
      final t = nums[cur]; // 把 数组[当前值] 存入 另一字符串
      nums[cur] = nums[p2]; // 把 数组[p2]; 写入 nums[cur]
      nums[p2] = t; // 把 另一字符串; 写入 nums[p2]
      p2--; // p2 减一
    } else {
      // 否则
      cur++; // 当前值 加一
    }
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final v = [2, 0, 2, 1, 1, 0]; // 把 [2, 0, 2, 1, 1, 0] 存入 值
  sortColors(v); // sortColors(值);
  if (v.toString() != '[0, 0, 1, 1, 2, 2]') throw StateError('c1');
  final v2 = [2, 0, 1]; // 把 [2, 0, 1] 存入 v2
  sortColors(v2); // sortColors(v2);
  if (v2.toString() != '[0, 1, 2]')
    throw StateError(
      'c2',
    ); // 若 v2.toString() 不等于 '[0, 1, 2]') throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
