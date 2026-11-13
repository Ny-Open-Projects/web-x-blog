/**
 ** LeetCode 153. 寻找旋转排序数组中的最小值
 ** 方案：1 ）方案1: 二分查找
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233483
 */

export function findMin(nums: number[]): number {
  // 定义函数/方法 findMin
  let low = 0; // 把 0 存入 low
  let high = nums.length - 1; // 把 数组.长度 减 1 存入 high
  while (low < high) {
    // 循环，直到不满足「low 小于 high」
    const pivot = low + Math.floor((high - low) / 2); // 把 low 加 向下取整((high 减 low) 除以 2) 存入 pivot
    if (nums[pivot] < nums[high]) {
      // 若 数组[pivot] 小于 数组[high]
      high = pivot; // 把 pivot 存入 high
    } else {
      // 否则
      low = pivot + 1; // 把 pivot 加 1 存入 low
    }
  }
  return nums[low]; // 返回 数组[low]
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (findMin([1, 2, 3]) !== 1) throw new Error('FAILED'); // 若 findMin([1, 2, 3]) 不等于 1) throw new Error(「FAILED」);
  if (findMin([3, 4, 5, 1, 2]) !== 1) throw new Error('FAILED'); // 若 findMin([3, 4, 5, 1, 2]) 不等于 1) throw new Error(「FAILED」);
  if (findMin([4, 5, 6, 7, 0, 1, 2]) !== 0) throw new Error('FAILED');
  if (findMin([11, 13, 15, 17]) !== 11) throw new Error('FAILED');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
