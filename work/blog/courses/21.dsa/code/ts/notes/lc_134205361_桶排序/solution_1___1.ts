// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function getIndex(arr: number[], k: number): number {
    // 定义函数/方法 getIndex
    if (!arr || arr.length === 0) return -1; // 若 取反 数组 或 数组.长度 全等于 0，直接返回 减 1
    const min_val = Math.min.apply(null, arr),
      max_val = Math.max.apply(null, arr);
    const bucket_size = Math.max(
      1,
      Math.floor((max_val - min_val) / arr.length) + 1,
    );
    const bucket_count = Math.floor((max_val - min_val) / bucket_size) + 1;
    const buckets: number[][] = []; // 把 []; 写入 const buckets: number[][]
    for (let i = 0; i < bucket_count; i++) buckets.push([]); // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_count 就继续
    for (const num of arr) {
      // for (const num of 数组) {
      const idx = Math.floor((num - min_val) / bucket_size); // 把 向下取整((num 减 min_val) 除以 bucket_size) 存入 idx
      buckets[idx].push(num); // 把 num 压入栈/数组尾部
    }
    for (const bucket of buckets) bucket.sort((x, y) => x - y);
    for (const bucket of buckets) {
      // for (const bucket of buckets) {
      for (const num of bucket) {
        // for (const num of bucket) {
        k -= 1; // 下标 k累减 1
        if (k === 0) return num; // 若 下标 k 全等于 0，直接返回 num
      }
    }
    return -1; // 返回 减 1
  }
  const cases = [
    { a: [1, 2, 3], k: 1, want: 1 },
    { a: [1, 2, 3], k: 2, want: 2 },
    { a: [1, 2, 3], k: 3, want: 3 },
    { a: [3, 1, 2], k: 2, want: 2 },
    { a: [], k: 1, want: -1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = getIndex(c.a, c.k); // 把 getIndex(字符.数组, 字符.下标 k) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
