// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nextGreaterElement(n: number): number {
    // 定义函数/方法 nextGreaterElement
    const MAX = 2147483647; // 把 2147483647 存入 MAX
    let nums = String(n).split(''); // 把 String(元素个数).split('') 存入 数组
    let i = nums.length - 2; // 把 数组.长度 减 2 存入 下标 i
    while (i >= 0 && nums[i] >= nums[i + 1]) i--; // 循环，直到不满足「下标 i 不低于 0 且 数组[下标 i] 不低于 数组[下标 i 加 1]) 下标 i 减一 ;」
    if (i < 0) return -1; // 若 下标 i 小于 0，直接返回 减 1
    let j = nums.length - 1; // 把 数组.长度 减 1 存入 下标 j
    while (nums[j] <= nums[i]) j--; // 循环，直到不满足「数组[下标 j] 不超过 数组[下标 i]) 下标 j 减一 ;」
    const t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
    let left = i + 1,
      right = nums.length - 1; // 把 下标 i 加 1, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left < right) {
      const tt = nums[left];
      nums[left] = nums[right];
      nums[right] = tt;
      left++;
      right--;
    }
    const ans = parseInt(nums.join(''), 10); // 把 转整数(数组.join(''), 10) 存入 答案
    return ans <= MAX ? ans : -1; // 返回 答案 不超过 MAX ? 答案 : 减 1
  }
  const cases = [
    { in: 1, want: -1 },
    { in: 12, want: 21 },
    { in: 21, want: -1 },
    { in: 123, want: 132 },
    { in: 321, want: -1 },
    { in: 1234, want: 1243 },
    { in: 4321, want: -1 },
    { in: 230241, want: 230412 },
    { in: 1999999999, want: -1 }, // { in: 1999999999, want: 减 1 }
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = nextGreaterElement(c.in); // 把 nextGreaterElement(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL nextGreaterElement(' + c.in + ')=' + got + ' want ' + c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
