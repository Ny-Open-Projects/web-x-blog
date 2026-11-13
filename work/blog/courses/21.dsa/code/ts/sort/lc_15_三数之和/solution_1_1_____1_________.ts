// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
/**
 ** LeetCode 15. 三数之和
 ** 方案：方案1（排序 + 双指针，first/second 循环）
 */

function threeSum(nums: number[]): number[][] {
  // 定义函数/方法 threeSum
  const arr = nums.slice().sort((a, b) => a - b);
  const ans: number[][] = []; // 把 []; 写入 const ans: number[][]
  const n = arr.length; // 把 数组.长度 存入 元素个数
  for (let first = 0; first < n; first++) {
    // 让 first 从 0 开始计数，first 小于 元素个数 就继续
    if (first > 0 && arr[first] === arr[first - 1]) continue; // 若 first 超过 0 且 数组[first] 全等于 数组[first 减 1]) continue;
    let third = n - 1; // 把 元素个数 减 1 存入 third
    const target = -arr[first]; // 把 减 数组[first] 存入 目标值
    for (let second = first + 1; second < n; second++) {
      // 让 second 从 first 加 1 开始计数，second 小于 元素个数 就继续
      if (second > first + 1 && arr[second] === arr[second - 1]) continue;
      while (second < third && arr[second] + arr[third] > target) third--; // 循环，直到不满足「second 小于 third 且 数组[third] 超过 目标值) third 减一 ;」
      if (second === third) break; // 若 second 全等于 third) break;
      if (arr[second] + arr[third] === target)
        // 若 数组[second] 加 数组[third] 全等于 目标值
        ans.push([arr[first], arr[second], arr[third]]); // 把 [数组[first], 数组[second], 数组[third]] 压入栈/数组尾部
    }
  }
  return ans; // 返回 答案
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = threeSum([1, 2, 3]); // 把 threeSum([1, 2, 3]) 存入 got
  if (got.length !== 0) throw new Error('threeSum([1,2,3]) should be []');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
