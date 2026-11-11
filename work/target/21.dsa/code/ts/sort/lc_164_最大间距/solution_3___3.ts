// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maximumGap(nums: number[]): number {
    // 定义函数/方法 maximumGap
    if (nums.length < 2) return 0; // 若 数组.长度 小于 2，直接返回 0
    let minv = nums[0],
      maxv = nums[0]; // 把 数组[0], 最大值 赋值为 数组[0] 存入 最小值
    for (const v of nums) {
      if (v < minv) minv = v;
      if (v > maxv) maxv = v;
    }
    if (minv === maxv) return 0; // 若 最小值 全等于 最大值，直接返回 0
    const n = nums.length; // 把 数组.长度 存入 元素个数
    let bs = Math.floor((maxv - minv) / (n - 1));
    if (bs < 1) bs = 1;
    const bc = Math.floor((maxv - minv) / bs) + 1; // 把 向下取整((最大值 减 最小值) 除以 bs) 加 1 存入 bc
    const bMin = new Array(bc),
      bMax = new Array(bc);
    const has = new Array(bc).fill(false);
    for (const v of nums) {
      // for (const 值 of 数组) {
      const idx = Math.floor((v - minv) / bs); // 把 向下取整((值 减 最小值) 除以 bs) 存入 idx
      if (!has[idx]) {
        bMin[idx] = v;
        bMax[idx] = v;
        has[idx] = true;
      } else {
        if (v < bMin[idx]) bMin[idx] = v;
        if (v > bMax[idx]) bMax[idx] = v;
      } // 否则
    }
    let ans = 0,
      prev = minv; // 把 0, 前一个 赋值为 最小值 存入 答案
    for (let i = 0; i < bc; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 bc 就继续
      if (!has[i]) continue; // 若 取反 has[下标 i]) continue;
      if (bMin[i] - prev > ans) ans = bMin[i] - prev; // 若 bMin[下标 i] 减 前一个 超过 答案) 答案 赋值为 bMin[下标 i] 减 前一个;
      prev = bMax[i]; // 把 bMax[下标 i] 存入 前一个
    }
    return ans; // 返回 答案
  }
  const cases = [
    { in: [3, 6, 9, 1], want: 3 },
    { in: [10], want: 0 },
    { in: [1, 10000000], want: 9999999 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maximumGap(c.in); // 把 maximumGap(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
