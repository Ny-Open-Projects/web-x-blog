/**
 ** LeetCode 45. 跳跃游戏 II
 ** 方案：2 ) 方案2: 正向查找可到达的最大位置
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145241433
 */

export function jump(nums: number[]): number {
  // 定义函数/方法 jump
  const n = nums.length; // 把 数组.长度 存入 元素个数
  if (n <= 1) return 0; // 若 元素个数 不超过 1，直接返回 0
  let maxPos = 0; // 把 0 存入 maxPos
  let end = 0; // 把 0 存入 终点
  let steps = 0; // 把 0 存入 steps
  for (let i = 0; i < n - 1; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
    maxPos = Math.max(maxPos, i + nums[i]); // 把 Math.取较大值 maxPos, 下标 i 加 数组[下标 i]) 存入 maxPos
    if (i === end) {
      // 若 下标 i 全等于 终点
      end = maxPos; // 把 maxPos 存入 终点
      steps++; // steps 加一
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
