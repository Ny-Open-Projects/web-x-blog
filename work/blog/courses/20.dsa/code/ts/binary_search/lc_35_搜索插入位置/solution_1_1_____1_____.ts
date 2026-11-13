/**
 ** LeetCode 35. 搜索插入位置
 ** 方案：1 ) 方案1：二分查找
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233077
 */

export function searchInsert(nums: number[], target: number): number {
  // 定义函数/方法 searchInsert
  let left = 0; // 把 0 存入 左边界
  let right = nums.length; // 把 数组.长度 存入 右边界
  while (left < right) {
    // 循环，直到不满足「左边界 小于 右边界」
    const mid = Math.floor((left + right) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 中点
    if (nums[mid] < target) {
      // 若 数组[中点] 小于 目标值
      left = mid + 1; // 把 中点 加 1 存入 左边界
    } else {
      // 否则
      right = mid; // 把 中点 存入 右边界
    }
  }
  return left; // 返回 左边界
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (searchInsert([1, 2, 3], 1) !== 0) throw new Error('FAILED');
  if (searchInsert([1, 3, 5, 6], 5) !== 2) throw new Error('FAILED');
  if (searchInsert([1, 3, 5, 6], 2) !== 1) throw new Error('FAILED');
  if (searchInsert([1, 3, 5, 6], 7) !== 4) throw new Error('FAILED');
  if (searchInsert([1, 3, 5, 6], 0) !== 0) throw new Error('FAILED');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
