// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742
// LeetCode 283. 移动零 — Dart 版（方案1）
void moveZeroes(List<int> nums) {
  // 定义函数/方法 moveZeroes
  var pos = 0; // 把 0 存入 pos
  for (var i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (nums[i] != 0) {
      // 若 数组[下标 i] 不等于 0
      final t = nums[pos]; // 把 数组[pos] 存入 另一字符串
      nums[pos] = nums[i]; // 把 数组[下标 i]; 写入 nums[pos]
      nums[i] = t; // 把 另一字符串; 写入 nums[i]
      pos++; // pos 加一
    }
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final v = [0, 1, 0, 3, 12]; // 把 [0, 1, 0, 3, 12] 存入 值
  moveZeroes(v); // moveZeroes(值);
  if (v.toString() != '[1, 3, 12, 0, 0]') throw StateError('c1');
  final v2 = [0]; // 把 [0] 存入 v2
  moveZeroes(v2); // moveZeroes(v2);
  if (v2.toString() != '[0]')
    throw StateError(
      'c2',
    ); // 若 v2.toString() 不等于 '[0]') throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
