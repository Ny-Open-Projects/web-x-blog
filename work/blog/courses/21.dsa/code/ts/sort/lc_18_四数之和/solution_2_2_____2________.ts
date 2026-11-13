// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
/**
 ** LeetCode 18. 四数之和
 ** 方案：方案2（排序 + 深度优先搜索）
 */

function fourSum(nums: number[], target: number): number[][] {
  // 定义函数/方法 fourSum
  const arr = nums.slice().sort((a, b) => a - b);
  const result: number[][] = []; // 把 []; 写入 const result: number[][]
  const n = arr.length; // 把 数组.长度 存入 元素个数
  function dfs(
    start: number,
    k: number,
    remaining: number,
    path: number[],
  ): void {
    // 定义函数/方法 dfs
    if (k === 0) {
      // 若 下标 k 全等于 0
      if (remaining === 0) result.push(path.slice()); // 若 remaining 全等于 0) 结果 追加 当前路径 截取 ));
      return; // return;
    }
    for (let i = start; i <= n - k; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 不超过 元素个数 减 下标 k 就继续
      if (i > start && arr[i] === arr[i - 1]) continue; // 若 下标 i 超过 起点 且 数组[下标 i] 全等于 数组[下标 i 减 1]) continue;
      if (arr[i] * k > remaining) break; // 若 数组[下标 i] 乘 下标 k 超过 remaining) break;
      if (i + 1 < n && arr[i] + arr[i + 1] * (k - 1) > remaining) break; // 最小补全都超，后面只会更大
      if (arr[i] + arr[n - 1] * (k - 1) < remaining) continue; // 最大补都不足，跳过当前
      path.push(arr[i]); // 把 数组[下标 i] 压入栈/数组尾部
      dfs(i + 1, k - 1, remaining - arr[i], path); // dfs(下标 i 加 1, 下标 k 减 1, remaining 减 数组[下标 i], 当前路径);
      path.pop(); // 弹出栈顶元素
    }
  }
  dfs(0, 4, target, []); // dfs(0, 4, 目标值, []);
  return result; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = fourSum([1, 2, 3], 1); // 把 fourSum([1, 2, 3], 1) 存入 got
  if (got.length !== 0) throw new Error('fourSum([1,2,3],1) should be []');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
