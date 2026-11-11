/**
 ** LeetCode 55. 跳跃游戏
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145241347
 */

export function canJump(nums: number[]): boolean {
  // 定义函数/方法 canJump
  let maxReach = 0; // 把 0 存入 maxReach
  for (let i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (i > maxReach) return false; // 若 下标 i 超过 maxReach，直接返回 false
    maxReach = Math.max(maxReach, i + nums[i]); // 把 Math.取较大值 maxReach, 下标 i 加 数组[下标 i]) 存入 maxReach
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!canJump([2, 3, 1, 1, 4])) throw new Error('FAILED 1'); // 若 取反 canJump([2, 3, 1, 1, 4])) throw new Error(「FAILED 1」);
  if (canJump([3, 2, 1, 0, 4])) throw new Error('FAILED 2'); // 若 canJump([3, 2, 1, 0, 4])) throw new Error(「FAILED 2」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
