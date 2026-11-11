// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
/**
 ** LeetCode 15. 三数之和
 ** 方案：方案2（排序 + 双指针，i/left/right 去重）
 */

function threeSum(nums: number[]): number[][] {
  // 定义函数/方法 threeSum
  const arr = nums.slice().sort((a, b) => a - b);
  const result: number[][] = []; // 把 []; 写入 const result: number[][]
  const n = arr.length; // 把 数组.长度 存入 元素个数
  for (let i = 0; i < n - 2; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 2 就继续
    if (i > 0 && arr[i] === arr[i - 1]) continue; // 若 下标 i 超过 0 且 数组[下标 i] 全等于 数组[下标 i 减 1]) continue;
    let left = i + 1; // 把 下标 i 加 1 存入 左边界
    let right = n - 1; // 把 元素个数 减 1 存入 右边界
    while (left < right) {
      // 循环，直到不满足「左边界 小于 右边界」
      const total = arr[i] + arr[left] + arr[right]; // 把 数组[下标 i] 加 数组[左边界] 加 数组[右边界] 存入 总和
      if (total < 0) {
        // 若 总和 小于 0
        left++; // 左边界 加一
      } else if (total > 0) {
        // 否则，若 总和 超过 0
        right--; // 右边界 减一
      } else {
        // 否则
        result.push([arr[i], arr[left], arr[right]]); // 把 [数组[下标 i], 数组[左边界], 数组[右边界]] 压入栈/数组尾部
        while (left < right && arr[left] === arr[left + 1]) left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 全等于 数组[左边界 加 1]) 左边界 加一 ;」
        while (left < right && arr[right] === arr[right - 1]) right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 全等于 数组[右边界 减 1]) 右边界 减一 ;」
        left++; // 左边界 加一
        right--; // 右边界 减一
      }
    }
  }
  return result; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = threeSum([1, 2, 3]); // 把 threeSum([1, 2, 3]) 存入 got
  if (got.length !== 0) throw new Error('threeSum([1,2,3]) should be []');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
