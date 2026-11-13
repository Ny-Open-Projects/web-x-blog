// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
/**
 ** LeetCode 905. 按奇偶排序数组
 ** 方案2: 双指针 + 一次遍历
 */

function sortArrayByParity(nums: number[]): number[] {
  // 定义函数/方法 sortArrayByParity
  const n = nums.length; // 把 数组.长度 存入 元素个数
  const res: number[] = new Array(n).fill(0); // 把 new Array(元素个数).fill(0); 写入 const res: number[]
  let left = 0,
    right = n - 1; // 把 0, 右边界 赋值为 元素个数 减 1 存入 左边界
  for (const num of nums) {
    // for (const num of 数组) {
    if (num % 2 === 0) {
      // 若 num 对…取模 2 全等于 0
      res[left++] = num; // 把 num; 写入 res[left++]
    } else {
      // 否则
      res[right--] = num; // 把 num; 写入 res[right--]
    }
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: number[]; want: number[] }[] = [
    { in: [1, 2, 3], want: [2, 3, 1] },
    { in: [3, 1, 2, 4], want: [2, 4, 1, 3] },
    { in: [0], want: [0] },
    { in: [0, 1, 2], want: [0, 2, 1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = sortArrayByParity([...c.in]); // 把 sortArrayByParity([...字符.in]) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL sortArrayByParity(' +
          JSON.stringify(c.in) +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
