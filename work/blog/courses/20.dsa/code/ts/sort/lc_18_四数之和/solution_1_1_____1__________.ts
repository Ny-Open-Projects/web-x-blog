// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
/**
 ** LeetCode 18. 四数之和
 ** 方案：方案1（排序 + 双指针）
 */

function fourSum(nums: number[], target: number): number[][] {
  // 定义函数/方法 fourSum
  const arr = nums.slice().sort((a, b) => a - b);
  const quadruplets: number[][] = []; // 把 []; 写入 const quadruplets: number[][]
  const n = arr.length; // 把 数组.长度 存入 元素个数
  for (let i = 0; i < n - 3; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 3 就继续
    if (i > 0 && arr[i] === arr[i - 1]) continue; // 若 下标 i 超过 0 且 数组[下标 i] 全等于 数组[下标 i 减 1]) continue;
    if (arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > target) break;
    if (arr[i] + arr[n - 3] + arr[n - 2] + arr[n - 1] < target) continue;
    for (let j = i + 1; j < n - 2; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 减 2 就继续
      if (j > i + 1 && arr[j] === arr[j - 1]) continue; // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 全等于 数组[下标 j 减 1]) continue;
      if (arr[i] + arr[j] + arr[j + 1] + arr[j + 2] > target) break;
      if (arr[i] + arr[j] + arr[n - 2] + arr[n - 1] < target) continue;
      let left = j + 1; // 把 下标 j 加 1 存入 左边界
      let right = n - 1; // 把 元素个数 减 1 存入 右边界
      while (left < right) {
        // 循环，直到不满足「左边界 小于 右边界」
        const s = arr[i] + arr[j] + arr[left] + arr[right]; // 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 字符串
        if (s === target) {
          // 若 字符串 全等于 目标值
          quadruplets.push([arr[i], arr[j], arr[left], arr[right]]); // 把 [数组[下标 i], 数组[下标 j], 数组[左边界], 数组[右边界]] 压入栈/数组尾部
          while (left < right && arr[left] === arr[left + 1]) left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 全等于 数组[左边界 加 1]) 左边界 加一 ;」
          while (left < right && arr[right] === arr[right - 1]) right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 全等于 数组[右边界 减 1]) 右边界 减一 ;」
          left++; // 左边界 加一
          right--; // 右边界 减一
        } else if (s < target) {
          // 否则，若 字符串 小于 目标值
          left++; // 左边界 加一
        } else {
          // 否则
          right--; // 右边界 减一
        }
      }
    }
  }
  return quadruplets; // 返回 quadruplets
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = fourSum([1, 2, 3], 1); // 把 fourSum([1, 2, 3], 1) 存入 got
  if (got.length !== 0) throw new Error('fourSum([1,2,3],1) should be []');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
