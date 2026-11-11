// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function removeDuplicates(nums: number[]): number {
    // 定义函数/方法 removeDuplicates
    if (nums.length === 0) return 0; // 若 数组.长度 全等于 0，直接返回 0
    let k = 1; // 把 1 存入 下标 k
    for (let i = 1; i < nums.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] !== nums[i - 1]) {
        nums[k] = nums[i];
        k++;
      }
    }
    return k; // 返回 下标 k
  }
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases = [
    { in: [1, 1, 2], k: 2, pre: [1, 2] },
    { in: [1, 2, 3], k: 3, pre: [1, 2, 3] },
    { in: [], k: 0, pre: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const nums = c.in.slice(); // 把 字符.in 截取 ) 存入 数组
    const got = removeDuplicates(nums); // 把 removeDuplicates(数组) 存入 got
    const prefix = nums.slice(0, got); // 把 数组 截取 0, got) 存入 prefix
    if (got !== c.k || !eqArr(prefix, c.pre)) {
      // 若 got 不等于 字符.下标 k 或 取反 eqArr(prefix, 字符.前缀和
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL removeDuplicates(' +
          JSON.stringify(c.in) +
          ') k=' +
          got +
          ' prefix=' +
          JSON.stringify(prefix),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
