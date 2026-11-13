/**
 ** LeetCode 922. 按奇偶排序数组 II
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134394571
 ** 方案：方案4（双指针原地交换）
 */

function sortArrayByParityII(nums: number[]): number[] {
  // 定义函数/方法 sortArrayByParityII
  const n = nums.length; // 把 数组.长度 存入 元素个数
  let j = 1; // 把 1 存入 下标 j
  for (let i = 0; i < n; i += 2) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (nums[i] % 2 === 1) {
      // 若 数组[下标 i] 对…取模 2 全等于 1
      while (nums[j] % 2 === 1) j += 2; // 循环，直到不满足「数组[下标 j] 对…取模 2 全等于 1) 下标 j 累加 2;」
      const tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
      nums[i] = nums[j]; // 把 数组[下标 j]; 写入 nums[i]
      nums[j] = tmp; // 把 临时变量; 写入 nums[j]
    }
  }
  return nums; // 返回 数组
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const a = sortArrayByParityII([4, 2, 5, 7]); // 把 sortArrayByParityII([4, 2, 5, 7]) 存入 数组
  if (a.join(',') !== '4,5,2,7') throw new Error('case1 mismatch: ' + a); // 若 数组.join(「,」) 不等于 「,」) throw new Error(「,」 加 数组);
  const b = sortArrayByParityII([2, 3]); // 把 sortArrayByParityII([2, 3]) 存入 b
  if (b.join(',') !== '2,3') throw new Error('case2 mismatch: ' + b); // 若 b.join(「,」) 不等于 「,」) throw new Error(「,」 加 b);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
