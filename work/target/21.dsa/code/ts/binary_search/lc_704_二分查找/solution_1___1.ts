/**
 ** LeetCode 704. 二分查找
 ** 方案：方案1
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134221939
 */

export function search(nums: number[], target: number): number {
  // 定义函数/方法 search
  let left = 0; // 把 0 存入 左边界
  let right = nums.length - 1; // 把 数组.长度 减 1 存入 右边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    const mid = Math.floor((left + right) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 中点
    if (nums[mid] === target) {
      // 若 数组[中点] 全等于 目标值
      return mid; // 返回 中点
    } else if (nums[mid] < target) {
      // 否则，若 数组[中点] 小于 目标值
      left = mid + 1; // 把 中点 加 1 存入 左边界
    } else {
      // 否则
      right = mid - 1; // 把 中点 减 1 存入 右边界
    }
  }
  return -1; // 返回 减 1
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (search([1, 2, 3], 1) !== 0) throw new Error('FAILED'); // 若 search([1, 2, 3], 1) 不等于 0) throw new Error(「FAILED」);
  if (search([-1, 0, 3, 5, 9, 12], 9) !== 4) throw new Error('FAILED');
  if (search([-1, 0, 3, 5, 9, 12], 2) !== -1) throw new Error('FAILED');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
