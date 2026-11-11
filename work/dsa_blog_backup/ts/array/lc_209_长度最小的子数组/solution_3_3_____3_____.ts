// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function minSubArrayLen(target: number, nums: number[]): number {
    // 定义函数/方法 minSubArrayLen
    let l = 0,
      best = nums.length + 1,
      sum = 0; // 把 0, 当前最优 赋值为 数组.长度 加 1, 累计和 赋值为 0 存入 左指针
    for (let r = 0; r < nums.length; r++) {
      // 让 右指针 从 0 开始计数，右指针 小于 数组.长度 就继续
      sum += nums[r]; // 累计和累加 数组[右指针]
      while (sum >= target) {
        // 循环，直到不满足「累计和 不低于 目标值」
        if (r - l + 1 < best) best = r - l + 1; // 若 右指针 减 左指针 加 1 小于 当前最优) 当前最优 赋值为 右指针 减 左指针 加 1;
        sum -= nums[l++]; // 累计和累减 数组[左指针 加一 ]
      }
    }
    return best === nums.length + 1 ? 0 : best; // 返回 当前最优 全等于 数组.长度 加 1 ? 0 : 当前最优
  }
  const cases = [
    { t: 7, nums: [2, 3, 1, 2, 4, 3], want: 2 },
    { t: 4, nums: [1, 4, 4], want: 1 },
    { t: 11, nums: [1, 1, 1, 1, 1, 1, 1, 1], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = minSubArrayLen(c.t, c.nums); // 把 minSubArrayLen(字符.另一字符串, 字符.数组) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
