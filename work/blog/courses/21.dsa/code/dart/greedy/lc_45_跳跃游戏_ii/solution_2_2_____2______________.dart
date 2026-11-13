// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745
// LeetCode 45. 跳跃游戏II — Dart 版（方案2）
int jump(List<int> nums) {
  // 定义函数/方法 jump
  var position = nums.length - 1; // 把 数组.长度 减 1 存入 position
  var steps = 0; // 把 0 存入 steps
  while (position > 0) {
    // 循环，直到不满足「position 超过 0」
    for (var i = 0; i < position; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 position 就继续
      if (i + nums[i] >= position) {
        // 若 下标 i 加 数组[下标 i] 不低于 position
        position = i; // 把 下标 i 存入 position
        steps++; // steps 加一
        break; // 跳出循环
      }
    }
  }
  return steps; // 返回 steps
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (jump([2, 3, 1, 1, 4]) != 2)
    throw StateError(
      'c1',
    ); // 若 jump([2, 3, 1, 1, 4]) 不等于 2) throw StateError('c1');
  if (jump([2, 3, 0, 1, 4]) != 2)
    throw StateError(
      'c2',
    ); // 若 jump([2, 3, 0, 1, 4]) 不等于 2) throw StateError('c2');
  if (jump([1]) != 0)
    throw StateError('c3'); // 若 jump([1]) 不等于 0) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
