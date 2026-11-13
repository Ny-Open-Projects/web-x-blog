// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maximumGap(nums: number[]): number {
    // 定义函数/方法 maximumGap
    const n = nums.length; // 把 数组.长度 存入 元素个数
    if (n < 2) return 0; // 若 元素个数 小于 2，直接返回 0
    const min_val = Math.min(...nums); // 把 Math.取较小值 ...数组) 存入 min_val
    const max_val = Math.max(...nums); // 把 Math.取较大值 ...数组) 存入 max_val
    const d = Math.max(1, Math.floor((max_val - min_val) / (n - 1))); // 把 Math.取较大值 1, 向下取整((max_val 减 min_val) 除以 (元素个数 减 1))) 存入 d
    const bucket_size = Math.floor((max_val - min_val) / d) + 1; // 把 向下取整((max_val 减 min_val) 除以 d) 加 1 存入 bucket_size
    const bucket: number[][] = []; // 把 []; 写入 const bucket: number[][]
    for (let i = 0; i < bucket_size; i++) bucket.push([-1, -1]); // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
    for (const num of nums) {
      // for (const num of 数组) {
      const idx = Math.floor((num - min_val) / d); // 把 向下取整((num 减 min_val) 除以 d) 存入 idx
      if (bucket[idx][0] === -1) {
        bucket[idx][0] = num;
        bucket[idx][1] = num;
      } else {
        bucket[idx][0] = Math.min(bucket[idx][0], num);
        bucket[idx][1] = Math.max(bucket[idx][1], num);
      } // 否则
    }
    let max_gap = 0; // 把 0 存入 max_gap
    let prev = -1; // 把 减 1 存入 前一个
    for (let i = 0; i < bucket_size; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
      if (bucket[i][0] === -1) continue; // 若 bucket[下标 i][0] 全等于 减 1) continue;
      if (prev !== -1)
        max_gap = Math.max(max_gap, bucket[i][0] - bucket[prev][1]);
      prev = i; // 把 下标 i 存入 前一个
    }
    return max_gap; // 返回 max_gap
  }
  function eq(a: number, b: number): boolean {
    return a === b;
  } // 定义函数/方法 eq
  const cases = [
    { in: [1, 2, 3], want: 1 },
    { in: [3, 6, 9, 1], want: 3 },
    { in: [10], want: 0 },
    { in: [], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maximumGap(c.in); // 把 maximumGap(字符.in) 存入 got
    if (!eq(c.want, got)) {
      fail = true;
      console.log(
        'FAIL maximumGap(' +
          JSON.stringify(c.in) +
          ')=' +
          got +
          ' want ' +
          c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
