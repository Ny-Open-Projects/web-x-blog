/**
 ** LeetCode 45. 跳跃游戏 II
 ** 方案：1 ) 方案1: 反向查找出发位置
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145241433
 */

export function jump(nums: number[]): number {
  // 定义函数/方法 jump
  let position = nums.length - 1; // 把 数组.长度 减 1 存入 position
  let steps = 0; // 把 0 存入 steps
  while (position > 0) {
    // 循环，直到不满足「position 超过 0」
    for (let i = 0; i < position; i++) {
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

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (jump([2, 3, 1, 1, 4]) !== 2)
    throw new Error('FAILED 1: ' + jump([2, 3, 1, 1, 4]));
  if (jump([2, 1]) !== 1) throw new Error('FAILED 2'); // 若 jump([2, 1]) 不等于 1) throw new Error(「FAILED 2」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
